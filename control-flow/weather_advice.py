#ask the user to input current weather condition

weather = input("What's the weather like today? (sunny/rainy/cold):")

#set conditions for different types of weather
#print the output of the weather recommendation

if weather == 'sunny':
     print('Wear a t-shirt and sunglasses.')
   
elif weather == 'rainy':
    print("Don't forget your umbrella and a raincoat.") 
     
elif weather == 'cold':
    print('Make sure to wear a warm coat and a scarf.')
    
else:
    print("Sorry, I don't have recommendations for this weather.")       
    


