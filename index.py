import csv
import pandas as pd
import requests
import time
## OOP 
## OOP is how you tell the computer about your created objects
## OOP contain 2 concept
    ## attributes - characteristics of the object
    ## methods - actions that the object can perform

class Dog:
    def __init__(self,name,species,age): ## attributes of the class
        self.name = name
        self.species = species
        self.age = age
    def bark(self): ## method of the class
       print("Woof!")
    def hbd(self):
        self.age += 1
    def __str__(self):
        return "I'm a dog"
dog1 = Dog("Milo","Poodle",3)
print("dog1:",dog1)
print(f"{dog1.name} is a {dog1.species} and {dog1.age} years old")
dog1.bark()
dog1.hbd()
print(f"{dog1.name} is now {dog1.age}")

## super class คือการสร้างคลาสที่ต่อยอดมากจาก class เดิมได้
class person:
   def __init__(self,name,age):
         self.name = name
         self.age = age

pure = person("Pure", 20)
print(f"{pure.name} is {pure.age} years old")

class Employee(person):
    def __init__(self,name,age,company):
        super().__init__(name,age) ## super() คือการเรียกใช้ method ของ class พ่อแม่
        self.company = company
    def greeting(self):
        print(f"Hello, I'm {self.name} and I work at {self.company}")

employee1 = Employee("Alice", 30, "Google")
employee1.greeting()

## try except block
## น่าจะเหมือน try catch 

try: 
    result = 1/0
except:
    print("Error: Division by zero is not allowed.")
try:
## read file
    file = open("hotel.csv", "r")

    data = csv.reader(file)
    for row in data:
        print("row data:",row)
    file.close()
except FileNotFoundError:
    print("Error: File not found.")
finally:
    print("read file successfully")

##context manager
##  python จะเปิดปิดไฟล์ให้เราเองด้วย keyword "with"
read_data = []
prices = []
with open("hotel.csv","r") as file:
    data = csv.reader(file)
    for row in data:
        read_data.append(row)
    for row in read_data[1:]:
        prices.append(float(row[-1]))     ##index -1 คือการเข้าถึงข้อมูลตัวสุดท้ายของ list
    print(f"average price is: {sum(prices)/len(prices)}")

print("read data:",read_data)
print("prices:",prices)


##pandas modern python
df = pd.read_csv("hotel.csv")

print("head csv:",df.head())
print(f"average price is: {df.price_per_night.mean()}")

##write file + context manager

# with open("school.csv","w") as file:
#     writer = csv.writer(file)
#     header = ["id","name","city"]
#     body = [1, "CU", "Bangkok"],[2, "LSE", "London"],[3, "Reading", "Reading"]


# with open("school.csv","w") as file:
#     writer = csv.writer(file)
#     writer.writerow(header)
#     writer.writerows(body)


##with pandas

# df.to_csv("hotel_copy.csv")

##select column
# df_penguin["species","island","body_mass_g"].head ## select column by name

## pandas query method
# df_penguin.query("body_mass_g > 5000") ## select row by condition

##filter without query()
# df_penguin[df_penguin["body_mass_g"] > 5000] ## select row by condition without query()

##request api
##how to get data via api the easy way

# url = "https://swapi.info/api/people/1"

# response = requests.get(url)

# response_json = response.json()
# print(response_json)

for i in range(10):
    url = f"https://swapi.info/api/people/{i+1}"
    response = requests.get(url)
    if response.status_code == 200:
        response_json = response.json()
        name.append(response_json["name"])
        print(response_json)
        time.sleep(1) ## delay 1 second between each request to avoid rate limit
    else:
        print(f"Error: {response.status_code}")
    time.sleep(1) ## delay 1 second between each request to avoid rate limit

    starwars = pd.DataFrame(name,columns=["name"]).to_csv("star_wars_characters.csv")

    print("starwars:",starwars)