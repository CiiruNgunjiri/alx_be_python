#ask the user to input current weather condition

weather = input("What's the weather like today? (sunny/rainy/cold):")

#set conditions for different types of weather
#print the output of the recommendation

if weather == 'sunny':
    recommendation = 'Wear a t-shirt and sunglasses.'
    print (recommendation)
elif weather == 'rainy':
    recommendation = "Don't forget your umbrella and a raincoat." 
    print (recommendation)  
elif weather == 'cold':
    recommendation = 'Make sure to wear a warm coat and a scarf.'
    print (recommendation) 
else:
    recommendation = "Sorry, I don't have recommendations for this weather."       
    print (recommendation)


