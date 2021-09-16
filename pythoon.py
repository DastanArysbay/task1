print("enter symbols without space")
line = input()
func1 = [line[-i:]+line[:-i] for i in range (len(line))]
print(func1)




    



