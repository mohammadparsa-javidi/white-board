from tkinter import *
from tkinter.colorchooser import askcolor
win = Tk()
win.title("White board")
win.geometry("1050x570+150+50")
win.resizable(False,False)
current_x = 0 
current_y = 0
color = "black"
# function for locate x and y
def locate_xy(work):
    global current_x,current_y
    
    current_x = work.x
    current_y = work.y
# function for draw line    
def add_line(work):
    global current_x,current_y
    canvase.create_line((current_x,current_y,work.x,work.y),width=get_current_value(),fill=color,
                        capstyle=ROUND,smooth=True)
    
    current_x,current_y = work.x,work.y
# function for change color    
def show_color(new_color):
    global color
    color = new_color

# function for eraser
def delete_canvase():
     canvase.delete("all")
     display_pallet()
     

# seticon for app
image_icon = PhotoImage(file="logo.png")
win.iconphoto(False,image_icon)
# set color box for colors
box_color = PhotoImage(file="section.png")
label_colors = Label(win,image=box_color)
label_colors.place(x=10,y=20)

# place for set color
colors = Canvas(win,bg="#ffffff",width=37,height=300)
colors.place(x=30,y=60)
# function for display color 
def display_pallet():
    id = colors.create_rectangle((10,10,30,30),fill="black")
    colors.tag_bind(id,"<Button-1>",lambda x:show_color("black"))
    
    id = colors.create_rectangle((10,40,30,60),fill="red")
    colors.tag_bind(id,"<Button-1>",lambda x:show_color("red"))
    
    id = colors.create_rectangle((10,70,30,90),fill="blue")
    colors.tag_bind(id,"<Button-1>",lambda x:show_color("blue"))
    
    id = colors.create_rectangle((10,100,30,120),fill="gray")
    colors.tag_bind(id,"<Button-1>",lambda x:show_color("gray"))
    
    id = colors.create_rectangle((10,130,30,150),fill="orange")
    colors.tag_bind(id,"<Button-1>",lambda x:show_color("orange"))
    
    id = colors.create_rectangle((10,160,30,180),fill="yellow")
    colors.tag_bind(id,"<Button-1>",lambda x:show_color("yellow"))
    
    id = colors.create_rectangle((10,190,30,210),fill="green")
    colors.tag_bind(id,"<Button-1>",lambda x:show_color("green"))
    
    id = colors.create_rectangle((10,220,30,240),fill="brown4")
    colors.tag_bind(id,"<Button-1>",lambda x:show_color("brown4"))
    
    id = colors.create_rectangle((10,250,30,270),fill="purple")
    colors.tag_bind(id,"<Button-1>",lambda x:show_color("purple"))
    
display_pallet()
# create eraser 
eraser = PhotoImage(file="eraser.png")
btn_eraser = Button(win,image=eraser,command=delete_canvase,cursor="hand2")
btn_eraser.place(x=30,y=400)

# canvase for paint
canvase = Canvas(win,width=930,bg="white",height=500)
canvase.place(x=100,y=10)

canvase.bind("<Button-1>",locate_xy)
canvase.bind("<B1-Motion>",add_line)
# Create slider for width of drawing
current_value = DoubleVar()

def get_current_value():
    return "{: .2f}".format(current_value.get())

def slider_changed(event):
    value_label.config(text=get_current_value())
    
slider = Scale(win,from_=0,to=100,orient="horizontal",command=slider_changed,variable=current_value)
slider.place(x=30,y=530)


value_label = Label(win,text=get_current_value())
value_label.place(x=27,y=550)
win.mainloop()