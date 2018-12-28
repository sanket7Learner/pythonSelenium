import pytest

@pytest.mark.skip(reason="no need")
def test_printHello_1():
    a=5
    assert a == 6
    print("Hello World")

@pytest.mark.Execute
def test_printHello_2():
    a=5
    assert a == 6
    print("Hello World_2")

@pytest.mark.Execute
def test_printHello_3():
    a=5
    assert a == 5
    print("Hello World_3")
#
# @pytest.mark.parametrize('test_input,expected', [
#     ("3+5", 8),
#     ("2+4", 6),
#     ("6*9", 54),
# ])
# def test_eval(test_input, expected):
#     assert eval(test_input) == expected
#
# def calculate(a,b):
#     return(a+b)
#
# @pytest.mark.parametrize("input1,input2,output",[(1,2,6)])
# def test_calculation_pass(input1,input2,output):
#     result = calculate(input1,input2)
#     assert result == output

# def test_calculation_fail():
#     result = calculate(5,5)
#     assert result == 11
#cd
#
# def printName(name="Sanket"):
#     print("Hello "+name)
#
# printName("Lata")
# printName()
#
# def test_returnValue():
#     print("Secoand File")
#
#
# class MyClass:
#     name="sanket"
#     age = 27
#     def __init__(self,Name,Age):
#         self.name = Name
#         self.age=Age
#
#     def sum(self,a,b):
#         print(a+b)
# x = MyClass("Balasaheb",58)
# del x.age
# print(x.name , x.age)
# print(x.sum(5,5))
#
# my_List = ["Sanket","Lata","Balasaheb","Shiralkar"]
# print(my_List)
# print(my_List[0])
# my_List[0] = "Ghanshyam"
# print(my_List[0])
#
# my_List.append("Atul")
# my_List.insert(0,"Sanskar")
#
# for item in my_List:
#     print(item)
#
# print("------------------------------------------------------")
#
# my_tuple = ("sanket","Nitin","rahul","Chand","Amol",[1,2,3])
# print(my_tuple[-1])
#
# print(my_tuple[5][1])
#
# print("sanket" in my_tuple)
#
# print(len(my_tuple))
#
# for item in my_tuple:
#     print(item)
#
# my_Set = {"TCS","Capgemini","Wipro","Infosys"}
#
# for item in my_Set:
#     print(item)
#
# print("TCS" in my_Set)
# my_Set.add("SQS")
# my_Set.update(["Microsoft","Google","Facebook"])
#
# my_Set.pop()
#
# for item in my_Set:
#     print(item)
