from tkinter import *

root = Tk()
root.title("Restaurant App")
root.geometry("400x400")



def create_menu( title,options):

    def show():
        label.config( text = clicked.get())

    

    clicked = StringVar()

    clicked.set(title)

    drop = OptionMenu(root,clicked,*options)
    drop.pack()


    # label = Label(root,text="choose")
    # label.pack()

create_menu("Category",["Pizza" ,"Burger" ,"Soft Drink","Extra Cheese","Extra Ketchup"]  )
create_menu("Size",["Small" ,"medium" ,"Large","classic","Big"]  )

# order type
take_away = StringVar().get()
dine = StringVar().get()
take_away_bt = Radiobutton(root, text="Take Away", variable=take_away, value="male")
dine_bt = Radiobutton(root, text="Dine", variable=dine, value="female")

root.mainloop()