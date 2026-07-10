card_no = str(input("input your card number: "))
card_carrier = str(input("input your card carriers name: "))

c1,c2,c3 =card_carrier.lower() , card_no.isdigit() , card_carrier.isalpha()
card_length = len(card_no)
valid_card_length = card_length == 16

c4 =bool( card_no == valid_card_length )
print(card_length,c4, valid_card_length)


if c1 == "visa" or  c1 == "mastercard":
 pass
elif not c3:
    print(f"{card_carrier}  this is not a valid card carrier ")


