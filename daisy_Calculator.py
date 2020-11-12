#!/usr/bin/env/python3
'''
This current program is a calculator with a user interface using
tkinter. So far the GUI is set, and the buttons allow for user input.
All the operators work to an extent.

Things to add:
functionality to the rest of the operating buttons.
ability to have more then 2 coefficients.
'''

import tkinter as tk
from tkinter import *

__author__ = "Marce Estrada"
__version__ = "1.0"
__date__ = "2020.11.11"

# setting global variables
global user_in
global numbers
global answer
global operator

user_in = []
numbers = []
answer = 0
operator = ' '

# create the window
root = tk.Tk()

root.configure(background="#ffd8d4", padx= 15, pady=15)
root.title("Daisy Calculator")
root.iconphoto(False, tk.PhotoImage(file='img/daisy_icon.png'))
root.geometry("270x400")
root.resizable(0, 0)

# setting the frames to group the gui elements
frame1 = tk.Frame(root, padx=10, pady=10, bg="white")
frame1.grid(row = 1,columnspan=5)
frame2 = tk.Frame(root,padx=0, pady=10, bg="#ffd8d4")
frame2.grid(rowspan=5,row = 2,columnspan= 3, column= 2)
frame3 = tk.Frame(root,padx=10, pady=10, bg="#ffd8d4")
frame3.grid(rowspan=5,row = 2, column = 1)
frame4 = tk.Frame(root,padx=15, pady=0, bg="#ffd8d4")
frame4.grid(rowspan = 6,row = 7, columnspan = 3)
frame5 = tk.Frame(root,padx=0, pady=0, bg="#ffd8d4")
frame5.grid( rowspan=7, row = 6, columnspan = 6, column = 3)

# setting the images to be used in the program
img1 = PhotoImage(file="img/num-01.png")
img2 = PhotoImage(file="img/num-02.png")
img3 = PhotoImage(file="img/num-03.png")
img4 = PhotoImage(file="img/num-04.png")
img5 = PhotoImage(file="img/num-05.png")
img6 = PhotoImage(file="img/num-06.png")
img7 = PhotoImage(file="img/num-07.png")
img8 = PhotoImage(file="img/num-08.png")
img9 = PhotoImage(file="img/num-09.png")
img10 = PhotoImage(file="img/num-10.png")
img11 = PhotoImage(file="img/num-11.png")
img12 = PhotoImage(file="img/num-12.png")
img13 = PhotoImage(file="img/num-13.png")
img14 = PhotoImage(file="img/num-14.png")
img15 = PhotoImage(file="img/num-15.png")
img16 = PhotoImage(file="img/num-16.png")
imgB = PhotoImage(file="img/daisy.png")




# create the label to show the user input
label = tk.Label(frame1, text = "", width=20, height=3, background= "black", foreground="white")
label.grid(columnspan=10)

logo = tk.Label(frame5, text="d", width=90, height = 90, bg="#ffd8d4", image=imgB)
logo.grid(column = 1)

def make_buttons():
    '''
    Creates all the buttons for the calculator

    :return: no value
    :rtype: none
    '''
    button1 = tk.Button(frame2, command=lambda: click_button(1))
    button2 = tk.Button(frame2, command=lambda: click_button(2))
    button3 = tk.Button(frame2, command=lambda: click_button(3))
    button4 = tk.Button(frame2, command=lambda: click_button(4))
    button5 = tk.Button(frame2, command=lambda: click_button(5))
    button6 = tk.Button(frame2, command=lambda: click_button(6))
    button7 = tk.Button(frame2, command=lambda: click_button(7))
    button8 = tk.Button(frame2, command=lambda: click_button(8))
    button9 = tk.Button(frame2, command=lambda: click_button(9))
    button0 = tk.Button(frame2, command=lambda: click_button(0))

    plus = tk.Button(frame3, command=lambda: click_button('+'))
    minus = tk.Button(frame3, command=lambda: click_button('-'))
    multi = tk.Button(frame3, command=lambda: click_button('*'))
    divides = tk.Button(frame3, command=lambda: click_button('/'))

    equals = tk.Button(frame4, command=lambda: click_button('='))
    clear = tk.Button(frame4, command=lambda: click_button('C'))

    buttons = {button1:img1, button2:img2, button3:img3, button4:img4, button5:img5, button6:img6,
              button7:img7, button8:img8, button9:img9, button0:img10,
              plus:img11, minus:img12, multi:img13, divides:img14, equals:img15, clear:img16}
    conf_button(buttons)


def conf_button(buttons):
    '''
    This functions takes a dictionary of buttons with a value assigned to them.
    It then goes through the dictionary using a for loop and configures
    each button with it's appropriate attributes. This is to have cleaner and less
    code.

    :param buttons: button, value
    :type buttons: dictionary

    :return: no value
    :rtype: none
    '''
    i = 0
    j = 0
    k = 0
    for button,n in buttons.items():
     button.configure(width=50, height=50, fg="#fc74aa", bg="white", activeforeground="white", activebackground="light blue", bd=0,relief="flat", image=n)
     if (i<10):
         
         if (i%3 == 0):
            j = i%3
            k+=1
            j=0
         j = j + 1
     if (i >= 10 and i <14):
         k+=1
         j=1
     if (i >= 14):
         k=0
         j+=1
     i+=1
     button.grid(row=k, column=j)
     

def click_button(n):
    '''
    This function determines what happens when a button is clicked
    if the buttons 0-9 are clicked, it registers it to a list.
    If any of the operators are clicked then it
    takes the list of digits that was made and concatanates them into a string.
    That way once the user clicks on the '=' then each of the concatanated
    string is cast into an int and the operator that was saved will be used for the final
    operation.

    :param n: value
    :type n: int or char

    :return: no value
    :rtype: none
    '''
    i = str(n)
    if (n == '-'):
        set_operations(n)
        return
    if (n == '+'):
        set_operations(n)
        return
    if (n == '*'):
        set_operations(n)
        return
    if (n == '/'):
        set_operations(n)
        return
    if (n == 'C'):
        label.configure(text='')
        user_in.clear()
        numbers.clear()
        return
    if (n == '='):
        coef =""
        for i in user_in:
            coef = coef + i
        user_in.clear()
        numbers.append(coef)
        j=0
        for i in numbers:
            if (i == '-'):
                answer = int(numbers[j-1]) - int(numbers[j+1])
                numbers[j+1] = str(answer)
            if (i == '+'):
                answer = int(numbers[j-1]) + int(numbers[j+1])
                numbers[j+1] = str(answer)
            if (i == '*'):
                answer = int(numbers[j-1]) * int(numbers[j+1])
                numbers[j+1] = str(answer)
            if (i == '/'):
                answer = int(numbers[j-1]) / int(numbers[j+1])
                numbers[j+1] = str(answer)
            j+=1
        numbers.clear()
        user_in.append(str(answer))
        label.configure(text=answer)
        return    
    user_in.append(i)
    
    label.configure(text=user_in)

def set_operations(n):
    '''
    This function sets the operations

    :param n: value
    :type n: int or char

    :return: no value
    :rtype: none
    '''
    if (len(user_in)==0 and len(numbers)==0):
        label.configure(text="Enter numbers please!")
        return
    if (len(user_in)==0):
        label.configure(text="Enter numbers please!")
        return    
    coef=""
    for i in user_in:
        coef = coef + i
    numbers.append(coef)
    numbers.append(n)
    label.configure(text=n)
    user_in.clear()
    return
   
     

def main():
    '''
    Main starts the program by setting the GUI by calling make_buttons, and is running through
    a loop until the user closes the window. 

    :param buttons: button, value
    :type buttons: dictionary

    :return: no value
    :rtype: none
    '''
    make_buttons()
 
    root.mainloop()


if __name__ == "__main__": # if this is the module where the program started from, then run the main function
   main()
