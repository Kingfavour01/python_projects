import sys
import os
import pygame
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton,
                             QListWidget, QVBoxLayout, QHBoxLayout, QWidget,
                             QFileDialog)
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont


class MusicPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Music Player")
        self.setGeometry(700, 300, 450, 500)

        pygame.mixer.init()

        self.current_track = None
        self.is_playing = False
        self.is_paused = False
        self.playlist = []

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.title_label = QLabel("No track loaded")
        self.title_label.setFont(QFont("Arial", 16, QFont.Bold))
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("color: #333; padding: 10px;")

        self.status_label = QLabel("")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("color: #777;")

        self.playlist_widget = QListWidget()
        self.playlist_widget.setFont(QFont("Arial", 11))
        self.playlist_widget.itemDoubleClicked.connect(self.play_selected)

        self.play_btn = QPushButton("▶ Play")
        self.pause_btn = QPushButton("⏸ Pause")
        self.stop_btn = QPushButton("⏹ Stop")
        self.prev_btn = QPushButton("⏮ Prev")
        self.next_btn = QPushButton("⏭ Next")
        self.add_btn = QPushButton("＋ Add")

        for btn in (self.play_btn, self.pause_btn, self.stop_btn,
                     self.prev_btn, self.next_btn, self.add_btn):
            btn.setFont(QFont("Arial", 12))

        self.play_btn.clicked.connect(self.play)
        self.pause_btn.clicked.connect(self.pause)
        self.stop_btn.clicked.connect(self.stop)
        self.prev_btn.clicked.connect(self.previous)
        self.next_btn.clicked.connect(self.next_track)
        self.add_btn.clicked.connect(self.add_files)

        controls_top = QHBoxLayout()
        controls_top.addWidget(self.play_btn)
        controls_top.addWidget(self.pause_btn)
        controls_top.addWidget(self.stop_btn)

        controls_bottom = QHBoxLayout()
        controls_bottom.addWidget(self.prev_btn)
        controls_bottom.addWidget(self.next_btn)

        add_layout = QHBoxLayout()
        add_layout.addStretch()
        add_layout.addWidget(self.add_btn)
        add_layout.addStretch()

        layout = QVBoxLayout()
        layout.addWidget(self.title_label)
        layout.addWidget(self.status_label)
        layout.addWidget(self.playlist_widget)
        layout.addLayout(controls_top)
        layout.addLayout(controls_bottom)
        layout.addLayout(add_layout)
        central_widget.setLayout(layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_status)
        self.timer.start(1000)

    def add_files(self):
        files, _ = QFileDialog.getOpenFileNames(
            self, "Add Music", "", "Audio Files (*.mp3 *.wav *.ogg)"
        )
        for f in files:
            if f not in self.playlist:
                self.playlist.append(f)
                self.playlist_widget.addItem(os.path.basename(f))

    def play_selected(self, item):
        if self.playlist_widget.currentRow() >= 0:
            self.current_track = self.playlist[self.playlist_widget.currentRow()]
            self._play_track()

    def _play_track(self):
        if not self.current_track:
            return
        pygame.mixer.music.load(self.current_track)
        pygame.mixer.music.play()
        self.is_playing = True
        self.is_paused = False
        self.title_label.setText(os.path.basename(self.current_track))
        self.status_label.setText("Playing")

    def play(self):
        if self.is_paused and self.current_track:
            pygame.mixer.music.unpause()
            self.is_playing = True
            self.is_paused = False
            self.status_label.setText("Playing")
        elif self.playlist_widget.currentRow() >= 0:
            self.play_selected(None)

    def pause(self):
        if self.is_playing:
            pygame.mixer.music.pause()
            self.is_playing = False
            self.is_paused = True
            self.status_label.setText("Paused")

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False
        self.is_paused = False
        self.status_label.setText("Stopped")

    def next_track(self):
        if not self.playlist:
            return
        idx = self.playlist_widget.currentRow()
        next_idx = (idx + 1) % len(self.playlist)
        self.playlist_widget.setCurrentRow(next_idx)
        self.current_track = self.playlist[next_idx]
        self._play_track()

    def previous(self):
        if not self.playlist:
            return
        idx = self.playlist_widget.currentRow()
        prev_idx = (idx - 1) % len(self.playlist)
        self.playlist_widget.setCurrentRow(prev_idx)
        self.current_track = self.playlist[prev_idx]
        self._play_track()

    def update_status(self):
        if self.is_playing and pygame.mixer.music.get_busy():
            pos_ms = pygame.mixer.music.get_pos()
            minutes = pos_ms // 60000
            seconds = (pos_ms % 60000) // 1000
            self.status_label.setText(f"Playing  {minutes:02d}:{seconds:02d}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = MusicPlayer()
    player.show()
    sys.exit(app.exec_())
