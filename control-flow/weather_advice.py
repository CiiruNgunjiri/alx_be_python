#ask the user to input current weather condition

user = input("What's the weather like today? (sunny/rainy/cold):")
weather = user

#set conditions for different types of weather

if weather == 'sunny':
    print ('Wear a t-shirt and sunglasses.')
elif weather == 'rainy':
    print ("Don't forget your umbrella and a raincoat.")   
elif weather == 'cold':
    print ('Make sure to wear a warm coat and a scarf.') 
else:
    print ("Sorry, I don't have recommendations for this weather.")       