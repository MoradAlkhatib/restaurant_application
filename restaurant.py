from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("Restaurant App")
root.geometry('{}x{}'.format(420, 280))

# pizza label and place it using grid
pizza_label = Label(root,text="How Much Pizza You need:",height=2,width=25)
pizza_label.grid(row=0,column=0)

# pizza input and place it using grid and make the focus on this input because its the first one.
pizza_input= Entry(root,width= 20 )
pizza_space= Label(root, text="d",width=17)
pizza_space.grid(row=0,column=2)
pizza_input.focus_set()
pizza_input.grid(row=0,column=1)

# pizza dropdown list for sizes and place it by using grid .
pizza_size_choose = StringVar()
pizza_size_choose.set("Pizza   Size")
pizza_size = OptionMenu(root,pizza_size_choose,*["Small" ,"medium" ,"Large"])    
pizza_size.grid(row=0,column=2)

# burger label and place it using grid.
burger_label = Label(root,text="How Much Burger You need:",height=2,width=25)
burger_label.grid(row=2,column=0)

# burger input and place it using grid.
burger_input= Entry(root, width= 20)
burger_input.grid(row=2,column=1)

# burger dropdown list for sizes and place it by using grid .
burger_size_choose = StringVar()
burger_size_choose.set("Burger Size")
burger_size = OptionMenu(root,burger_size_choose,*["classic","Big"])    
burger_size.grid(row=2,column=2)

# soft drink label and place it using grid.
soft_drink_label = Label(root,text="How Much Soft drink You need",height=2,width=25)
soft_drink_label.grid(row=4,column=0)

# soft drink input and place it using grid.
soft_drink_input= Entry(root, width= 20)
soft_drink_input.grid(row=4,column=1)

# label for Extra Things.
extra_label = Label(root,text="Extra Things:",height=2)
extra_label.grid(row=6,column=0)

#  CheckBox for Extra Cheese.
cheese_val = IntVar()
cheese_checker = Checkbutton(master=root,text="Extra Cheese",variable=cheese_val,height=2)
cheese_checker.grid(row=6,column=1)

#  CheckBox for Extra Ketchup.
ketchup_val = IntVar()
ketchup_checker = Checkbutton(master=root,text="Extra Ketchup",variable=ketchup_val,height=2)
ketchup_checker.grid(row=6,column=2)

# order type its radio buttons to check how the order will deliver to the user.
num_radio_bt = IntVar()
label_radio = Label(root,text="Order type:", height=2)
take_away = Radiobutton(root, text="Take Away",value = 1, variable = num_radio_bt )
dine  = Radiobutton(root, text="Dine In", value = 2 , variable = num_radio_bt )

# set positions for radio buttons.
label_radio.grid(row=8,column=0)
take_away.grid(row=8,column=1)
dine.grid(row=8,column=2)



# Create a messagebox showinfo and price.

def onClick():   
    the_price = 0
    text = 'You order for... \n'
    number_of_pizza = pizza_input.get()
    size_of_pizza = pizza_size_choose.get()
    if number_of_pizza:
        if size_of_pizza in ["Small" ,"medium" ,"Large"]:
            text+=f"{number_of_pizza} {size_of_pizza} Pizza.\n"
            
            if size_of_pizza == "Small":
                x = 5
            elif size_of_pizza == "medium":
                x = 7
            else :
                x = 10 

            the_price = int(number_of_pizza) * x

        else :
            text = "You forgot to choose Pizza size."

    number_of_burger = burger_input.get()
    size_of_burger = burger_size_choose.get()

    if number_of_burger:
        if size_of_burger == "Classic" or size_of_burger=="Big":
            text+=f"{number_of_burger} {size_of_burger} Burger.\n"
            
            if size_of_burger == "Classic":
                x = 5
            else :
                 x = 7
            the_price += int(number_of_burger) * x
          
            
        else :
            text = "You forgot to choose Burger size."

    number_of_soft_drink = soft_drink_input.get()

    if number_of_soft_drink:
        text+=f"{number_of_soft_drink} Soft Drink."
        the_price += int(number_of_soft_drink)

    cheese = cheese_val.get()

    if cheese:
        text+=f"With Extra Cheese\n"
        the_price += 1

    ketchup = ketchup_val.get()

    if ketchup:
        text+=f"With Extra Ketchup\n"
        the_price += 1

    deliver = num_radio_bt.get()

    if deliver == 1:
        text+= "The order will take a way\n"
    else :
        text+="The order is dine\n"

    pizza_input.delete(0,'end')
    burger_input.delete(0,'end')
    soft_drink_input.delete(0,'end')
    
    

    if the_price > 0:
        text += f"The Total Price Is {the_price}"
    
    tkinter.messagebox.showinfo("Your Order Is",  text)
    

label_space = Label(root,text="")
label_space.grid(row=10,rowspan=8,columnspan=10)

# Create a Button to get the order and set the position using grid.
message = Button(root, text="Order Now", command=onClick, height=2, width=10,fg = 'black',
                 bg = 'yellow',font = (("Times New Roman"),12))
message.grid(row=18,column=1)

root.mainloop()



