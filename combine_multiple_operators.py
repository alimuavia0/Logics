temperature = 25
raining = False
weekend = True

# if (temperature > 20 and not raining) or weekend :
#     print("Great day for out activities")
# else :
#     print("not good day for activities")

if temperature > 20 and not raining and (weekend or not weekend):
    print("Great day for outdoor activities")
else:
    print("Not a great day for activities")
    

 

    
