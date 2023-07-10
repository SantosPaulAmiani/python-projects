list = ["James", "Mercy", "Caren","Jimmy","Lydia"]

data1 = input(str("Enter a name to search: ")).capitalize()

if data1 in list:
    print(f"{data1  } is available")
else:
    print(f"{data1} is not available")