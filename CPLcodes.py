import streamlit as st

rad = st.radio('select',['reverse number','Fabonacci','multiplication Table',
                         'remove space','Factorial',
                         'distance',
                         'square and cube','tkinter'])

if rad == 'tkinter':
    code = """
import tkinter as tk
import ttkbootstrap as ttk

window = ttk.Window(themename='darkly')
window.title("DEMO")
window.geometry('400x150')

label = ttk.Label(master=window, text="kilo metre to metre", font='Calibiri 30')
label.pack()

def convert():
    input0 = int1.get()
    output0 = str(input0 * 1000)
    output_string.set(output0 + ' metre')

frame = ttk.Frame(master=window)
int1 = tk.IntVar()
entry = ttk.Entry(master=frame, textvariable=int1)
button = ttk.Button(master=frame, text="convert", command=convert)
entry.pack(side='left')
button.pack(side='left')
frame.pack()

output_string = tk.IntVar()
output_label = ttk.Label(
    master=window,
    text='output',
    font='Calibiri 20',
    textvariable=output_string
)
output_label.pack(pady=10)
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