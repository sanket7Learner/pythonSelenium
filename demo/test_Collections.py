
class MyClass:
    name="sanket"
    age = 27
    def __init__(self,Name,Age):
        self.name = Name
        self.age=Age

    def sum(self,a,b):
        print(a+b)
x = MyClass("Balasaheb",58)
#del x.age
print(x.name , x.age)
print(x.sum(5,5))

my_animal_dict = {
    "cat":"house",
    "tiger":"forest",
    "dolphin":"water"
}

print(my_animal_dict)
print(my_animal_dict["cat"])
print(my_animal_dict.get("tiger"))

my_animal_dict["cat"]="home"

my_animal_dict["Sparrow"]="Air"

my_animal_dict.pop("tiger")

for item in my_animal_dict.values():
    print(item)

