from tkinter import *
import os
from pygame import mixer


def playmusic():
    global index
    status.set("--playing")
    song.set(playlist.get(ACTIVE))
    mixer.music.load(playlist.get(ACTIVE))
    # Playing Selected Song
    mixer.music.play()
    x = playlist.curselection()
    y=()
    if(x == y):
        x = (0,)
    index = x[0]
def pausemusic():
    status.set("--paused")
    mixer.music.pause()
def next():
    global index
    playlist.activate(index+1)
    song.set(playlist.get(ACTIVE))
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()    
    index = index+1
    

def backcomm():
    global index
    playlist.activate(index-1)
    song.set(playlist.get(ACTIVE))
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    index = index-1

root = Tk()
root.title("Musicfy")
root.geometry("600x400")
root.iconbitmap('images\music3.ico')
root.resizable(0,0)

mixer.init()
play = PhotoImage(file = "images\Play.png") 
pause = PhotoImage(file = "images\Pause.png")
back = PhotoImage(file = "images\Backward.png")
forward =PhotoImage(file = "images\Forward.png")
image1 = PhotoImage(file = "images\Capture.png")

song = StringVar()
status = StringVar()
index = 0

Menu1 = Menu(root)
root.config(menu = Menu1)

filemenu = Menu(root,tearoff = 0)
filemenu.add_command(label="Open")

Menu1.add_cascade(label="File" ,menu = filemenu)

helpmenu = Menu(root, tearoff = 0)
helpmenu.add_command(label="about")

Menu1.add_cascade(label = "help",menu = helpmenu)

musicframe = LabelFrame(root, text = "Music", font =("times new roman",15,"bold"),bg = "White",fg = "gold" ,bd =5,relief = GROOVE)
musicframe.place(x=0,y=0,width=600,height =100)

buttonframe = LabelFrame(root,text="Control",font=("times new roman",15,"bold"),bg="white",fg="gold",bd=1,relief=GROOVE)
buttonframe.place(x=0,y=100,width=600,height=100)

frame1 = LabelFrame(root,text="Music list",font = ("times new roman",15,"bold"),bg ="white",fg = "gold",bd = 5 , relief = GROOVE)
frame1.place(x=0,y=200,width=600, height = 200)

Label(musicframe,textvariable = song ,font = ("times new roman",15,"bold"),bg = "white",fg = "red",bd = 0,relief = GROOVE).grid(row=0,column=2)
Label(musicframe,textvariable = status ,font = ("times new roman",15,"bold"),bg = "white",fg = "red",bd = 0,relief = GROOVE).grid(row=1,column=2)



label = Label(buttonframe, image = image1 )
label.pack(expand = True , fill = BOTH)

#listbox

playlist = Listbox(frame1,selectbackground="gold",selectmode=SINGLE,font=("times new roman",12,"bold"),bg="white",fg="navyblue",bd=5,relief=GROOVE)
playlist.pack(fill = BOTH)
os.chdir("Enter Your music folder address") #here is your music address
    # Fetching Songs
songtracks = os.listdir()
    # Inserting Songs into Playlist
for track in songtracks:
        playlist.insert(END,track)
#Buttons

playbutton = Button(buttonframe, image =play ,bg = "silver" , relief = GROOVE,command = playmusic)
playbutton.place(x = 200,y= 15)

pausebutton = Button(buttonframe, image =pause ,bg = "silver" , relief = GROOVE,command = pausemusic)
pausebutton.place(x = 300 ,y=15)

backbutton = Button(buttonframe, image =back ,bg = "silver" , relief = GROOVE,command = backcomm)
backbutton.place(x = 100 ,y = 15)
forwardbutton = Button(buttonframe, image =forward ,bg = "silver" , relief = GROOVE,command = next)
forwardbutton.place(x= 400 ,y = 15)



root.mainloop()
