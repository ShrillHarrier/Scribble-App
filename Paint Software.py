from tkinter import * 

def clearscreen():
    border = borderon.get()
    
    if border == True:
        cv.delete(ALL)
        cv.create_rectangle(0, 0, 800, 35, fill = 'black', outline='')
        cv.create_rectangle(750, 0, 800, 430, fill = 'black', outline='')
        cv.create_rectangle(0, 395, 800, 430, fill = 'black', outline='')
        cv.create_rectangle(0, 0, 50, 430, fill = 'black', outline='')

    elif border == False:
        cv.delete(ALL)

def addshape():
    red=r.get()
    green=g.get()
    blue=b.get()
    rgb = (f'#{red:02x}{green:02x}{blue:02x}')

    cv.unbind('<Button-1>')
    textbutton.configure(bg='#F0F0ED')

    shapebutton.configure(bg='green')
    
    currentshape = shape.get()

    def first(event):
        x=event.x
        y=event.y
        cv.unbind('<Button-1>')
        def second(event):
            x2=event.x
            y2=event.y
            if currentshape == 'Rectangle':
               cv.create_rectangle(x, y, x2, y2, fill = rgb, outline='')
            elif currentshape == 'Circle':
                cv.create_oval(x, y, x2, y2, fill = rgb, outline='')
            elif currentshape == 'Line':
                cv.create_line(x, y, x2, y2, fill = rgb)
            cv.unbind('<Button-1>')
            shapebutton.configure(bg='#F0F0ED')
        cv.bind('<Button-1>',second)
                
    cv.bind('<Button-1>',first)

def addfont():
    red=r.get()
    green=g.get()
    blue=b.get()
    rgb = (f'#{red:02x}{green:02x}{blue:02x}')

    title=titleon.get()

    cv.unbind('<Button-1>')
    shapebutton.configure(bg='#F0F0ED')

    textbutton.configure(bg='green')

    f=font.get()
    fs=fontsize.get()
    t=textinput.get()

    if title == True:
        cv.create_text(400,50+(fs/4.5),fill=rgb,font=(f,fs),text=t)
        textbutton.configure(bg='#F0F0ED')
        titleon.set(False)
        
    elif title == False:
        def first(event):
            x=event.x
            y=event.y
        
            cv.create_text(x,y,fill=rgb,font=(f,fs),text=t)
            cv.unbind('<Button-1>')
            textbutton.configure(bg='#F0F0ED')

        cv.bind('<Button-1>',first)

def border():
    bgcolour=background.get()
    border = borderon.get()
    if border == True:
        cv.create_rectangle(0, 0, 800, 35, fill = 'black', outline='')
        cv.create_rectangle(750, 0, 800, 430, fill = 'black', outline='')
        cv.create_rectangle(0, 395, 800, 430, fill = 'black', outline='')
        cv.create_rectangle(0, 0, 50, 430, fill = 'black', outline='')
    elif border == False:
        cv.create_rectangle(0, 0, 800, 35, fill = bgcolour, outline='')
        cv.create_rectangle(750, 0, 800, 430, fill = bgcolour, outline='')
        cv.create_rectangle(0, 395, 800, 430, fill = bgcolour, outline='')
        cv.create_rectangle(0, 0, 50, 430, fill = bgcolour, outline='')

def bgcolour(self):
    bgcolour=background.get()
    cv.configure(bg=bgcolour)
    
def draw(event):
    red=r.get()
    green=g.get()
    blue=b.get()
    rgb = (f'#{red:02x}{green:02x}{blue:02x}')
    bgcolour=background.get()

    cvsmall.configure(bg=rgb)
    colourhex.configure(text=rgb)

    localbrush = brushsize.get()
    localeraser = erasersize.get()
    
    x=event.x
    y=event.y

    if event.widget == cv:
        if utensil.get() == 'brush':
            cv.create_oval(x, y, x + localbrush, y + localbrush, fill = rgb, outline='')
        
        elif utensil.get() == 'eraser':
            cv.create_oval(x, y, x + localeraser, y + localeraser, fill = bgcolour, outline='')
    
#MAIN
#Generate holding structures for GUI
#############
root = Tk()
mainframe = Frame(root)

#Create the widgets and associated Vars
#############
utensillabel = Label(mainframe, text='Untensil Colour', font=('Arial',15))
sample = Label(mainframe, text='Untensil Colour Sample', font=('Arial',10))
bglabel = Label(mainframe, text='Background Colour', font=('Arial',15))

colourhex = Label(mainframe, text='#000000', font=('Arial',8))

textlabel = Label(mainframe, text='Add Text', font=('Arial',15))
fontlabel = Label(mainframe, text='Font:', font=('Arial',8))
fontsizelabel = Label(mainframe, text='Font Size:', font=('Arial',8))
entertextlabel = Label(mainframe, text='Enter Text:', font=('Arial',8))

shapelabel = Label(mainframe, text='Add Shape', font=('Arial',15))
shapesublabel = Label(mainframe, text='Shape:', font=('Arial',8))
                
red = Label(mainframe, text='Red:', font=('Arial', 10))
r = IntVar()
r.set(0)
rcolour = Scale(mainframe, from_=0, to=255, variable=r, width=15, length=150, orient=HORIZONTAL,)
rcolour.bind("<B1-Motion>", draw)

green = Label(mainframe, text='Green:', font=('Arial', 10))
g = IntVar()
g.set(0)
gcolour = Scale(mainframe, from_=0, to=255, variable=g, width=15, length=150, orient=HORIZONTAL,)
gcolour.bind("<B1-Motion>", draw)

blue = Label(mainframe, text='Blue:', font=('Arial', 10))
b = IntVar()
b.set(0)
bcolour = Scale(mainframe, from_=0, to=255, variable=b, width=15, length=150, orient=HORIZONTAL,)
bcolour.bind("<B1-Motion>", draw)

background = StringVar()
colours = ['White', 'Grey', 'Black', 'Red', 'Green', 'Blue', 'Yellow', 'Orange', 'Purple']
background.set('White')
backgrounds = OptionMenu(mainframe, background, *colours, command=bgcolour)

font = StringVar()
fonts = ['Arial', 'Times New Roman', 'Impact', 'Terminal', 'Gigi']
font.set('Arial')
fontchoice = OptionMenu(mainframe, font, *fonts)

fontsize = IntVar()
fontsize.set(20)
sizeselect = Spinbox(mainframe, textvariable=fontsize, width=10, from_=5, to=50)

textinput = StringVar()
textget = Entry(mainframe, font=(font.get(), fontsize.get()), width=10, textvariable = textinput)

textbutton = Button(mainframe, text='Add', command=addfont)

titleon = BooleanVar()
titleon.set(False)
titlecheck = Checkbutton(mainframe, text='Title', variable=titleon, onvalue=True, offvalue=False)
                    
shape = StringVar()
shapes = ['Rectangle', 'Circle', 'Line']
shape.set('Rectangle')
shapeselect = OptionMenu(mainframe, shape, *shapes)

shapebutton = Button(mainframe, text='Add', command=addshape)

clear = Button(mainframe, text='Clear', command=clearscreen)

options = LabelFrame(mainframe, text='Effect')
borderon = BooleanVar()
borderon.set(False)
bordercheck = Checkbutton(options, text='Border', variable=borderon, onvalue=True, offvalue=False, command=border)

utensil = StringVar()
utensil.set('brush')
brush = Radiobutton(mainframe, text="Brush", variable=utensil, value="brush")
eraser = Radiobutton(mainframe, text="Eraser", variable=utensil, value="eraser")

brushlabel=Label(mainframe, text='Brush Size', font=('Arial',8))
eraserlabel=Label(mainframe, text='Eraser Size', font=('Arial',8))

brushsize=IntVar()
brushsize.set(10)
brushscale = Scale(mainframe, from_=50, to=1, variable=brushsize, orient=VERTICAL, length=100, show=True)
brushscale.bind("<B1-Motion>", draw)

erasersize=IntVar()
erasersize.set(10)
eraserscale = Scale(mainframe, from_=50, to=1, variable=erasersize, orient=VERTICAL, length=100, show=True)
eraserscale.bind("<B1-Motion>", draw)

cv = Canvas(mainframe, width=800, height=430, bg=background.get())
cvsmall = Canvas(mainframe, width=80, height=65, bg="#000000")

#Grid the widgets
#############
root.minsize(width=1040, height=660)
root.maxsize(width=1040, height=660)
mainframe.grid(rowspan=11, columnspan=11)

utensillabel.grid(row=1, column=1, columnspan=3)

sample.grid(row=3, column=5, columnspan=2)
bglabel.grid(row=1, column=5, columnspan=2)
colourhex.grid(row=5, column=5, columnspan=2)

textlabel.grid(row=1,column=7,columnspan=3)

shapelabel.grid(row=1,column=10)
shapesublabel.grid(row=2,column=10,sticky=W)

fontlabel.grid(row=2,column=7)
fontsizelabel.grid(row=3,column=7)
entertextlabel.grid(row=4,column=7)

red.grid(row=2,column=1, columnspan=2, sticky=W)
green.grid(row=3,column=1, columnspan=2, sticky=W)
blue.grid(row=4,column=1, columnspan=2, sticky=W)

rcolour.grid(row=2,column=2,columnspan=3)
gcolour.grid(row=3,column=2,columnspan=3)
bcolour.grid(row=4,column=2,columnspan=3,sticky=N)

backgrounds.grid(row=2,column=5,columnspan=2)

cv.grid(row=6, column=3, rowspan=5, columnspan=8, padx=40)
cv.bind("<Button1-Motion>", draw)

cvsmall.grid(row=4,column=5,columnspan=2)

fontchoice.grid(row=2,column=7,columnspan=3)
sizeselect.grid(row=3,column=7,columnspan=3)
textget.grid(row=4,column=7,columnspan=2,sticky=E)
textbutton.grid(row=5,column=8,sticky=W)
titlecheck.grid(row=5,column=7)

shapeselect.grid(row=2,column=10)
shapebutton.grid(row=3,column=10)

clear.grid(row=9,column=2,sticky=W)

options.grid(row=6,column=2,padx=5)
bordercheck.grid(row=1,column=2)

brushlabel.grid(row=6,column=11,sticky=S)

brush.grid(row=5,column=11)
brushscale.grid(row=7,column=11)

eraserlabel.grid(row=9,column=11,sticky=S)

eraser.grid(row=8,column=11)
eraserscale.grid(row=10,column=11)

root.mainloop() 
