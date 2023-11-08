import streamlit as st

rad = st.radio('select',['reverse number','Fabonacci','multiplication Table',
                         'remove space','Factorial','celcius to farenheit',
                         'distance','object oriented','traverse a tuple',
                         'graph plot','sine and cosine waves','odd index',
                         'square and cube','tkinter'])

if rad == 'tkinter':
    code = """
import tkinter as tk
import ttkbootstrap as ttk

window = ttk.Window(themename="darkly")
window.title("Simple GUI")
window.geometry('400x200')  

def button_click():
    label.config(text="Button Clicked!")
button = ttk.Button(window, text="Click Me!", command=button_click)
label = ttk.Label(window, text="Hello!", font=("Calibri", 16))

button.pack(pady=20)  
label.pack()

window.mainloop()
    """

    st.code(code, language="python")
    
elif rad == 'reverse number':
    code = """
#reverse of a number
num = input('Enter number :')
print(num)
num2= ''
for i in range(1,len(num)+1):
    num2 = num2+num[-i] 

print(num2)
    """

    st.code(code, language="python")
    
elif rad == 'Fabonacci':
    code = """
#Fabonacci series
i = 0
j = 1
series = []
n = int(input('enter length of series : '))
for m in range(n):
    series.append(i)
    temp = i
    i = j
    j = j+temp
    
print(series)
    """

    st.code(code, language="python")
    
elif rad == 'multiplication Table':
    code = """
#multiplication Table
n = int(input('Enter n: '))

print('-----------')

for i in range(1,n+1):
    
    print(f'Multiplication Table of {i} is')
    
    for j in range(1,11):
        
        print(f'{i} * {j} = {i*j}')
        
    print('----------')
    """

    st.code(code, language="python")

elif rad == 'remove space':
    code = """
#remove space using continue
word = input('Enter : ')
word2 = ''

for i in range(len(word)):
    if word[i] == ' ':
        continue
    else:
        word2 = word2+word[i]

print(word2)

    """

    st.code(code, language="python")

elif rad == 'Factorial':
    code = """
#Factorial of a Number
number = int(input('Enter Number : '))
fact = 1
for i in range(1,number+1):
    fact = fact*i
    
print(f'Factorial of {number} is {fact}')
    """

    st.code(code, language="python")

elif rad == 'square and cube':
    code = """
# square and cube

num=int(input('Enter the number:'))
print('The square of number is:'+str(num**2))
print('The cube of number is:'+str(num**3))
    """

    st.code(code, language="python")
    
elif rad == 'distance':
    code = """
#Distance between two point
import math

p1 = (input('Enter (x1,y1) : '))
p2 = (input('Enter (x2,y2) : '))

p3 = p1.split(',')
p4 = p2.split(',')

x1 = int(p3[0])
y1 = int(p3[1])
x2 = int(p4[0])
y2 = int(p4[1])

dist = math.sqrt(((x2-x1)**2)+((y2-y1)**2))

print(f'Distance between ({x1},{y1}) & ({x2},{y2}) is {round(dist,4)}cm')
    """

    st.code(code, language="python")
    
elif rad == 'object oriented':
    code = """
#Program1 on oops
class student: 
    def __init__(self, name, age):
        self.name =name
        self.age =age
        
    def display_info(self):
        print(f"I am {self.name} and my age is {self.age}")
student1= student("abc",20)
student1.display_info()
    """

    st.code(code, language="python")
    
    code = """
#Program 2 \n Define a class called "Car"
class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0


    def accelerate(self):
        self.speed += 5

    def brake(self):
        if self.speed >= 5:
            self.speed -= 5
        else:
            self.speed = 0


    def display_info(self):
        return f"{self.year} {self.make} {self.model} traveling at {self.speed} mph"

car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Accord", 2021)

car1.accelerate()
car2.accelerate()
car1.accelerate()
car1.brake()

print("Car 1:", car1.display_info())
print("Car 2:", car2.display_info())

    """

    st.code(code, language="python")

elif rad == 'graph plot':
    code = """
#draw subplot
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-2,2,400)
y1=x
y2=x**2
y3=x**3
plt.figure(figsize=(10,6))

#y=x
plt.subplot(1,3,1)
plt.plot(x,y1,color='blue')
plt.title('y=x')

#y=x^2
plt.subplot(1,3,2)
plt.plot(x,y2,color='green')
plt.title('y=x^2')

#y=x^3
plt.subplot(1,3,3)
plt.plot(x,y3,color='red')
plt.title('y=x^3')

plt.tight_layout()
plt.show()
    """

    st.code(code, language="python")
    
elif rad == 'sine and cosine waves':
    code = """
#sine and cosine waves
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,2*np.pi,100)

y_sin=np.sin(x)
y_cos=np.cos(x)

plt.plot(x, y_sin, label='Sine Wave')
plt.plot(x, y_cos, label='Cosine Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sine and Cosine Waves')
plt.legend()
plt.show()
    """
    st.code(code, language="python")
    
elif rad == 'celcius to farenheit':
    code = """
#convert celcius to farenheit
temp=[23,45,67,43,79]
for i in temp:
    f=(i*9/5)+32
    print(f)
    """
    st.code(code, language="python")
    
elif rad == 'traverse a tuple':
    code = """
#traverse a tuple
mark=[(75,67,98,84),(89,69,88),(78,98,67,69)]
for i in mark:
    for j in i:
        print(j)
    """
    st.code(code, language="python")
    
elif rad == 'odd index':
    code = """
#odd index into new tuple
T=(1,3,2,4,6,5)
list=[]
for i in T:
    while i%2==1:
        list.append(T[i])
        i=i+1
newtup= tuple(list)
print(newtup)
    """
    st.code(code, language="python")
