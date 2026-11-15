from day_5 import country, countries;


# print((country[7:13]).title())
# print(country[:13])
# print(country.find("US")) #-1 (Not Found)
# print(country.index("A"))
# print(country.find("America"))


# print(type(str(countries[:1])))
# print(type(countries))

Lenguage = ["Py", "Java", "C++"]
Lenguage.append("C")
# Lenguage[3] = ("JS")
Lenguage[0] = ("JS")

# Lenguage.insert(2,"Flutter")
# Lenguage[1:1] = ["C#", "Kottlen"]
# Lenguage[1:2] = []

# Lenguage[1:2] = "Larveal"
Lenguage[1:2] = ["Larveal"]

# print(Lenguage)

cities = ["Lahore", "Multan", "Quetta"]

# for city in cities:
#  print(city, end=" - ")

cities[1] = "Bahawalpur"

# if "Bahawalpur" in cities:
#  print("We are in 'IUB'");
 
# print(cities)

# newLen = Lenguage.pop()
# print(newLen);

# newLen = Lenguage.remove("JS")
# a = Lenguage.copy()
# print(a)

# newLen = Lenguage.pop(2)

# print(Lenguage)

# for i in range(0, 10, 2):
#     print(i, end=" | ")


cities = ("Lahore", "Multan", "Quetta")
north = ("Swat", "Hunza", "Swat")
# print(cities[-1])
# print(cities + north)


student = ("Ali", ("Lahore", "Punjab"), [70, 85])

print(student[1])
print(student[1][0])
print(student[2][1]) 

#******** Tupple Unpacking
student = (101, "Ali", 88)

roll_no, name, marks = student

# print(roll_no)
# print(name)
# print(marks)

