
sum_odd_digits = 0
sum_even_digits= 0
total = 0

card_num = str(input("enter your credit card number: "))
card_num = card_num.replace("-"or" ","")
card_num = card_num[::-1]

for odd_value in card_num[::2]:
    sum_odd_digits += int(odd_value)
for even_value in card_num[1::2]:
   even_value = int (even_value) * 2
   if even_value >= 10 :
       sum_even_digits += (1 + (even_value % 10))
   else:
       sum_even_digits += even_value

total = sum_even_digits + sum_odd_digits

if total % 10 == 0:
    print("valid")
else:
    print("invalid")