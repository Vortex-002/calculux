from tkinter import *



root = Tk()
root.title('CALCULUX')

e = Entry(root, width=30, borderwidth=5)
e.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

    
def click(number):
	#e.delete(0, END)
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(number))

def AC():
	e.delete(0, END)

def add():
	first_number = e.get()
	global f_num
	global math
	math = "addition"
	f_num = int(first_number)
	e.delete(0, END)

def equal():
	second_number = e.get()
	e.delete(0, END)
	
	if math == "addition":
		e.insert(0, f_num + int(second_number))

	if math == "subtraction":
		e.insert(0, f_num - int(second_number))

	if math == "multiplication":
		e.insert(0, f_num * int(second_number))

	if math == "division":
		e.insert(0, f_num / int(second_number))

	

def minus():
	first_number = e.get()
	global f_num
	global math
	math = "subtraction"
	f_num = int(first_number)
	e.delete(0, END)

def product():
	first_number = e.get()
	global f_num
	global math
	math = "multiplication"
	f_num = int(first_number)
	e.delete(0, END)

def divide():
	first_number = e.get()
	global f_num
	global math
	math = "division"
	f_num = int(first_number)
	e.delete(0, END)












#assingning the buttons
btn_0 = Button(root, text='0', padx=20, pady=20, command= lambda: click(0))
btn_1 = Button(root, text='1', padx=20, pady=20, command= lambda: click(1))
btn_2 = Button(root, text='2', padx=20, pady=20, command= lambda: click(2))
btn_3 = Button(root, text='3', padx=20, pady=20, command= lambda: click(3))
btn_4 = Button(root, text='4', padx=20, pady=20, command= lambda: click(4))
btn_5 = Button(root, text='5', padx=20, pady=20, command= lambda: click(5))
btn_6 = Button(root, text='6', padx=20, pady=20, command= lambda: click(6))
btn_7 = Button(root, text='7', padx=20, pady=20, command= lambda: click(7))
btn_8 = Button(root, text='8', padx=20, pady=20, command= lambda: click(8))
btn_9 = Button(root, text='9', padx=20, pady=20, command= lambda: click(9))
btn_del = Button(root, text='DEL', padx=16, pady=20)
btn_AC = Button(root, text='AC', padx=16, pady=20, command= AC)
btn_product = Button(root, text='X', padx=20, pady=20, command=product)
btn_divide = Button(root, text="/", padx=20, pady=20, command=divide)
btn_add = Button(root, text='+', padx=20, pady=20, command=add)
btn_minus = Button(root, text='-', padx=20, pady=20, command=minus)
btn_ans = Button(root, text='ANS', padx=16, pady=20)
btn_equal = Button(root, text='=', padx=17, pady=20, command= equal)
btn_decimal = Button(root, text='.', padx=20, pady=20)
btn_exp = Button(root, text='EXP', padx=16, pady=20)


#putting the buttons on screen

btn_0.grid(row=4, column=0)
btn_decimal.grid(row=4, column=1)
btn_exp.grid(row=4, column=2)
btn_ans.grid(row=4, column=3)
btn_equal.grid(row=4, column=4)

btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)
btn_add.grid(row=3, column=3)
btn_minus.grid(row=3, column=4)

btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)
btn_product.grid(row=2, column=3)
btn_divide.grid(row=2, column=4)

btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)
btn_del.grid(row=1, column=3)
btn_AC.grid(row=1, column=4)


root.mainloop()
