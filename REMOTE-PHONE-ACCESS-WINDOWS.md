# Remote Phone Access to opencode — Windows Setup Runbook

Self-contained runbook to rebuild this machine's "access opencode from your phone" setup on a
**Windows** computer. Mirrors the existing Linux setup exactly — same credentials, same port,
same tailnet.

Hand this file to your opencode agent on the Windows machine and it can execute the steps
top-to-bottom.

- **Target:** Windows 10 or 11 (x64)
- **Credentials (reuse the SAME ones as Linux):**
  - Username: `opencode`
  - Password: `kingfresh2026`
- **Port:** `4096` (bound to `127.0.0.1` only — never `0.0.0.0`, never `--mdns`)
- **Tailnet:** `tail6a788d.ts.net` (owner: `kingfresh1000upgrades@gmail.com`)
- **Serve URL on Windows:** `https://<WINDOWS-HOSTNAME>.tail6a788d.ts.net`
  (`<WINDOWS-HOSTNAME>` is the Windows machine's MagicDNS name — see Step 0)

---

## Architecture

```
┌────────────┐   WireGuard (Tailscale VPN)   ┌───────────────────────────────┐
│  Phone     │ ─────────────────────────────▶│  Windows PC                    │
│ (Android)  │   https://<pc>.tail6a788d.ts.net                            │
│ OpenRemote │                               │  tailscaled ── serve ── HTTPS │
│ MobileCode │                               │     │                        │
└────────────┘                               │     ▼                        │
                                             │  http://127.0.0.1:4096       │
                                             │  opencode web (auth req.)    │
                                             └───────────────────────────────┘
```

- Only devices in your tailnet can reach the serve URL.
- `opencode web` listens on loopback only → not exposed on LAN.
- Tailscale terminates HTTPS at the tailnet edge (automatic TLS cert).

---

## Prerequisites

1. Windows 10/11 x64, an **Administrator terminal** (Windows+X → Terminal (Admin)) for Tailscale steps.
2. A Tailscale account already logged into the tailnet (login works via browser code).
3. The phone with either app installed (both connect to the same URL):
   - **OpenRemote** (preferred): APK from `https://github.com/blairhudson/openremote/releases/latest`
   - **MobileCode** (alternative): Google Play, `https://play.google.com/apps/testing/io.apuyou.mobilecode`
4. `winget` (comes with Windows 10/11 by default).

---

## Step 0 — Install & log into Tailscale

Run in an **Admin** terminal (or install from https://tailscale.com/download/windows):

```powershell
winget install Tailscale.Tailscale --accept-package-agreements --accept-source-agreements
```

After install, sign in:

```powershell
tailscale up
```

A browser URL opens — sign in with the tailnet owner account. Confirm the machine is registered
and HTTPS + MagicDNS are enabled:

```powershell
tailscale status
tailscale cert-status
```

Expected:

- The Windows machine appears in `tailscale status` alongside `redmi-13` and `fedora`.
- HTTPS must be enabled for `tailscale serve` (if the serve command later asks you to enable it,
  it will print an admin URL — visit it once).

Note your machine's MagicDNS name for Step 5/6:

```powershell
tailscale status | Select-String "<"
```

It will look like `<WINDOWS-HOSTNAME>.tail6a788d.ts.net`.

---

## Step 1 — Install opencode

Recommended (native binary, no Node needed):

```powershell
winget install -e --id SST.opencode
```

> **Note:** the winget manifest is community-maintained (not official) and can lag a version.
> If the version below is too old, use one of the alternatives.

Alternatives (pick ONE):

```powershell
npm install -g opencode-ai          # official, needs Node.js installed first
scoop install opencode              # if you use Scoop
choco install opencode              # if you use Chocolatey
```

Verify (reopen the terminal first):

```powershell
opencode --version
```

Should print something like `1.18.13` or newer.

---

## Step 2 — Create the opencode web wrapper script

`opencode web` needs two environment variables (`OPENCODE_SERVER_USERNAME`,
`OPENCODE_SERVER_PASSWORD`) and specific CLI flags. On Windows there is no systemd, so we create a
small `.cmd` wrapper that sets them, then register it as a scheduled task.

Create the file `C:\Users\<YOU>\.opencode\opencode-web.cmd` with this exact content:

```bat
@echo off
set OPENCODE_SERVER_USERNAME=opencode
set OPENCODE_SERVER_PASSWORD=kingfresh2026
opencode web --hostname 127.0.0.1 --port 4096
```

Create the folder first if it does not exist:

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.opencode"
```

---

## Step 3 — Register & start the scheduled task

Register a task that starts `opencode web` at every logon (mirrors the Linux systemd unit):

```powershell
schtasks /Create /TN "opencode-web" /TR "C:\Users\<YOU>\.opencode\opencode-web.cmd" /SC ONLOGON /F
```

Start it immediately:

```powershell
schtasks /Run /TN "opencode-web"
```

Check it is running:

```powershell
schtasks /Query /TN "opencode-web"
```

---

## Step 4 — Verify opencode web locally

From a normal (non-admin) PowerShell:

```powershell
Invoke-WebRequest -Uri http://127.0.0.1:4096 -UseBasicParsing | Select-Object StatusCode
```

Expected: `401` (authentication required) — this is correct, the server is up and locked.

Then with credentials:

```powershell
$sec = ConvertTo-SecureString "kingfresh2026" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("opencode", $sec)
Invoke-WebRequest -Uri http://127.0.0.1:4096 -UseBasicParsing -Credential $cred | Select-Object StatusCode
```

Expected: `200`.

> If you get a connection error here, the task is not running — check Step 3 (`schtasks /Query`)
> and the event log. Do NOT proceed to Step 5 until this returns 401/200.

---

## Step 5 — Expose over Tailscale (HTTPS)

In the **Admin** terminal (Windows uses the same command, no `sudo`):

```powershell
tailscale serve --bg --https=443 http://127.0.0.1:4096
```

Verify the config:

```powershell
tailscale serve status
```

Expected output:

```
Available within your tailnet:
https://<WINDOWS-HOSTNAME>.tail6a788d.ts.net

|-- / proxy http://127.0.0.1:4096
```

The `--bg` flag persists across reboots (same as the Linux setup).

---

## Step 6 — Verify from the phone

1. Make sure the phone's Tailscale is up (the `redmi-13` device).
2. Open **OpenRemote** (or MobileCode) and add a server:
   - **URL:** `https://<WINDOWS-HOSTNAME>.tail6a788d.ts.net`
   - **Username:** `opencode`
   - **Password:** `kingfresh2026`
3. Confirm you see the session list / can open a session.

Test the raw endpoint from any tailnet device as a sanity check:

```powershell
# on another device, or from PowerShell with creds
Invoke-WebRequest -Uri "https://<WINDOWS-HOSTNAME>.tail6a788d.ts.net/session/status" -Credential $cred -UseBasicParsing
```

Expected: `200` with JSON (`{"healthy":true,...}`).

---

## Step 7 — Boot persistence checklist

Everything should come up on its own after a reboot:

- [ ] Tailscale service is set to **Automatic**:
      `Get-Service Tailscale | Select StartType` → `Automatic`
- [ ] `tailscale serve status` still shows the proxy (serve config persists).
- [ ] Scheduled task `opencode-web` still exists:
      `schtasks /Query /TN "opencode-web"`
- [ ] After logon, `http://127.0.0.1:4096` returns 401 unauth / 200 with creds.

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `tailscale serve` asks to enable HTTPS / prints admin URL | HTTPS not enabled in tailnet | Open the printed URL, approve HTTPS, re-run the serve command |
| Phone gets connection refused / timeout | Phone Tailscale off, or wrong hostname | `tailscale status` on phone; confirm `redmi-13` is up; use the exact `...tail6a788d.ts.net` name |
| Phone gets 401/403 | Wrong creds | Use `opencode` / `kingfresh2026` |
| `http://127.0.0.1:4096` connection refused | `opencode-web` task not running | `schtasks /Query /TN "opencode-web"`, then `/Run`; check the `.cmd` path is correct |
| 502 from serve URL | backend down or loopback mismatch | Confirm Step 4 works; re-run `tailscale serve --bg --https=443 http://127.0.0.1:4096` |
| `opencode` command not found after install | PATH not refreshed | Reopen the terminal |
| winget version too old | Community manifest lag | `npm install -g opencode-ai` or grab the binary from GitHub releases |
| Firewall prompts | none needed | No Windows Firewall rule is required — the server binds loopback, tailscaled owns 443. Do NOT open 4096 to the network. |

---

## Security notes

- **Loopback only:** `opencode web` binds `127.0.0.1:4096`. Never use `0.0.0.0` or `--mdns`.
- **Tailnet-only:** `tailscale serve` (not `tailscale funnel`) — the URL is private to your tailnet.
- **Shared password:** both Linux and Windows use the same `opencode`/`kingfresh2026`.
  Anyone in your tailnet with these creds can drive your opencode. Rotate the password in the
  wrapper script (and the Linux `.env`) if ever leaked.
- **Same port both machines:** the Linux box and Windows box both use `4096` — they are separate
  machines, so there is no conflict; just use each machine's own serve URL.

---

## Optional: OpenRemote plugin (SKIP)

The `opencode-openremote` npm plugin adds QR pairing, keep-awake, and permission approval — but
every one of those features lives in its TUI plugin and requires an interactive TUI. Under headless
`opencode web` (this setup) it produces nothing but a log line. **Do not install it.**

The OpenRemote **app** works fully via the manual URL above without the plugin.

---

## Change log

- 2026-08-05 — Initial runbook, mirrors Linux setup (Fedora 44 + opencode 1.18.13 + Tailscale 1.102.2).
