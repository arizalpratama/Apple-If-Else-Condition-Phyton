apple_price = 2
money = 100
input_count = input('How much do you want buy apple?: ')
count = int(input_count)
total_price = apple_price * count

print('You will buy ' + str(count) + ' apple')
print('The total price is ' + str(total_price) + ' dollar')

if money > total_price:
    print('You will buy ' + str(count) + ' apple')
    print('The total price is ' + str(total_price) + 'dollar')
elif money == total_price:
    print('You had buy ' + str(count) + ' apple')
    print('Your wallet is empty now')
else:
    print('Your money is not enough')
    print("You can't buy that many apples")