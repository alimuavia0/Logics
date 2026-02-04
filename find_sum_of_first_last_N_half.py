lst = []
lst.append(int(input("Enter the number 1:  ")))
lst.append(int(input("Enter the number 2:  ")))
lst.append(int(input("Enter the number 3:  ")))
lst.append(int(input("Enter the number 4:  ")))
lst.append(int(input("Enter the number 5:  ")))

fst =  (lst[0] + lst[1]) / 2
last = (lst[-1] + lst[-2]) /2

if lst[0] > lst[-1] :
  
  if fst  > last :
      print(f"half of sum  first tow numbers: {fst}")
else :
  print(f"half of sum last tow numbers: {last}")
  



