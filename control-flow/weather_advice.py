#ask the user to input current weather condition

user = input("What's the weather like today? (sunny/rainy/cold):")
weather = user

#set conditions for different types of weather

if weather == 'sunny':
    recommendation = 'Wear a t-shirt and sunglasses.'
elif weather == 'rainy':
    recommendation = "Don't forget your umbrella and a raincoat."   
elif weather == 'cold':
    recommendation = 'Make sure to wear a warm coat and a scarf.' 
else:
    recommendation = "Sorry, I don't have recommendations for this weather."       

#print the output of the recommendation
print (recommendation)
