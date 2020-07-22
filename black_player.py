from tkinter import *
import os
from pygame import mixer
import PIL
import stagger
from tkinter import ttk
from PIL import ImageTk
import io
from tkinter.messagebox import showinfo
from tkinter.filedialog import  askdirectory
from mutagen.mp3 import MP3
from time import sleep     
from pathlib import Path

def opacity100():
    root.attributes("-alpha", 1)
    
def opacity90():
    root.attributes("-alpha", .9)

def opacity80():
    root.attributes("-alpha", .8)

def opacity70():
    root.attributes("-alpha", .7)

def opacity60():
    root.attributes("-alpha", .6)

def opacity50():
    root.attributes("-alpha", .5)

def fileopen():
    global st
    path =""
    try:
        path = askdirectory(parent=root,title='Choose directory with mp3')
        if path == "":
            pass
        else:
            st = path
            playlist.delete(0,'end')
            musiclist()

    except:
        pass
    
def vol():
    if scale1.winfo_manager():
        scale1.place_forget()
    else:
        scale1.place(x=110,y=320)


def volume(val):
    global currentdir
    global st
    global vol1
    global img1
    os.chdir(currentdir)
    val1 = float(val)/100
    mixer.music.set_volume(val1)
    if(val1 == 0.0):
        volbutton['image'] = img1
    else:
        volbutton['image'] = vol1
    os.chdir(st)

def musiclist():
    global st
    os.chdir(st)
    # Fetching Songs
    songtracks = os.listdir()
    # Inserting Songs into Playlist
    for track in songtracks:
        if track.endswith(".mp3"):
            playlist.insert(END,track)
        else:
            pass
    #Buttons

def musicpic():
    global currentdir
    global st
    global photo
    global new_path
    try:
        mp3 = stagger.read_tag(new_path)
        by_data = mp3[stagger.id3.APIC][0].data
        im = io.BytesIO(by_data)
        imageFile =PIL.Image.open(im)
        imageFile = imageFile.resize((260,300 ), PIL.Image.ANTIALIAS)
        photo =  ImageTk.PhotoImage(imageFile)
        label1.image = photo
        label1['image'] = photo
    except:
        os.chdir(currentdir)
        photo=PhotoImage(file = "Music-Heart-icon.png")
        label1['image'] = photo
        os.chdir(st)

def playmusic():
    global st
    global index
    global new_path
    global song_
    status.set("--playing")
    song_ =playlist.get(ACTIVE)
    new_path=os.path.join(st , song_)
    song.set(song_)
    print(new_path)
    mixer.music.load(song_)
    # Playing Selected Song
    mixer.music.play()
    
    x = playlist.curselection()
    y=()
    if(x == y):
        x = (0,)
    index = x[0]
    playbutton.place_forget()
    pausebutton.place(x = 110 ,y=15)
    musicpic()


def pausemusic():
    status.set("--paused")
    mixer.music.pause()
    pausebutton.place_forget()
    playbutton.place(x = 110 ,y=15)
def next():
    global index
    global new_path
    playlist.activate(index+1)
    song.set(playlist.get(ACTIVE))
    song_ = playlist.get(ACTIVE)
    new_path=os.path.join(st , song_)   
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()    
    index = index+1
    musicpic()
    playbutton.place_forget()
    pausebutton.place(x = 110 ,y=15)
    

def backcomm():
    global index
    global new_path
    playlist.activate(index-1)
    song.set(playlist.get(ACTIVE))
    song_ = playlist.get(ACTIVE)
    new_path=os.path.join(st , song_)
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    index = index-1
    musicpic()
    playbutton.place_forget()
    pausebutton.place(x = 110 ,y=15)

def hide():
     if frame1.winfo_manager():
         frame1.place_forget()
         root.geometry("600x500")
         queuebutton['image'] = arrow2
     else :
        frame1.place(x=600,y=0,width=400, height = 500)
        root.geometry("1000x500")
        queuebutton['image'] = arrow1
def lighttheme():
    frame1['bg'] = "white"
    musicframe['bg'] = "white"
    buttonframe['bg'] = "white"
    label1['bg'] = "white"
    playbutton['bg'] = "white"
    backbutton['bg'] = "white"
    pausebutton['bg'] = "white"
    forwardbutton['bg'] = "white"
    playlist['bg'] = "white"
    queuebutton['bg'] ="white"
    volbutton['bg'] ="white"
    root.configure(background = "white")
def darktheme():
    frame1['bg'] = "black"
    musicframe['bg'] = "black"
    buttonframe['bg'] = "black"
    label1['bg'] = "black"
    playbutton['bg'] = "black"
    backbutton['bg'] = "black"
    pausebutton['bg'] = "black"
    forwardbutton['bg'] = "black"
    playlist['bg'] = "black"
    queuebutton['bg'] ="black"
    volbutton['bg'] ="black"
    root.configure(background = "black")

def greytheme():
    frame1['bg'] = "grey"
    musicframe['bg'] = "grey"
    buttonframe['bg'] = "grey"
    label1['bg'] = "grey"
    playbutton['bg'] = "grey"
    backbutton['bg'] = "grey"
    pausebutton['bg'] = "grey"
    forwardbutton['bg'] = "grey"
    playlist['bg'] = "grey"
    queuebutton['bg'] ="grey"
    volbutton['bg'] ="grey"
    root.configure(background = "grey")

def about():
    showinfo("Music player","by deepanshu tyagi")

if __name__ == "__main__":
    root = Tk()
    photo=PhotoImage(file = "images/Music-Heart-icon.png")
    root.title("Musicfy")
    root.geometry("600x520")
    root.iconbitmap('images/music3.ico')
    root.resizable(0,0)
    root.configure(background= "black")
    root.attributes("-alpha", 0.9)

    mixer.init()
    play = PhotoImage(file = "images/Play.png") 
    pause = PhotoImage(file = "images/Pause.png")
    back = PhotoImage(file = "images/backward.png")
    forward =PhotoImage(file = "images/Forward.png")
    queuep = PhotoImage(file = "images/interface.png")
    arrow1 =PhotoImage(file = "images/arrows(1).png")
    arrow2 =PhotoImage(file = "images/arrows.png")
    vol1 = PhotoImage(file = "images/vol.png")
    img1 = PhotoImage(file = "images/mute1.png")


    song = StringVar()
    song.set("Welcome to Musicfy")
    status = StringVar()
    index = 0
    st = str(os.path.join(Path.home(), "Music"))
    currentdir = os.path.abspath(os.getcwd())
    new_path = ""

    Menu1 = Menu(root)
    root.config(menu = Menu1)

    filemenu = Menu(root,tearoff = 0)
    filemenu.add_command(label="Open",command = fileopen)
    Menu1.add_cascade(label="File" ,menu = filemenu)

    thememenu = Menu(root,tearoff=0)
    thememenu.add_command(label="light",command = lighttheme)
    thememenu.add_command(label="dark",command = darktheme)
    thememenu.add_command(label="grey",command = greytheme)
    filemenu.add_cascade(label="Theme" ,menu = thememenu)


    helpmenu = Menu(root, tearoff = 0)
    helpmenu.add_command(label="about",command = about)
    Menu1.add_cascade(label = "Help",menu = helpmenu)

    opacitymenu = Menu(root,tearoff =0)
    opacitymenu.add_command(label = "100%",command =opacity100)
    opacitymenu.add_command(label = "90%",command =opacity90)
    opacitymenu.add_command(label = "80%",command =opacity80)
    opacitymenu.add_command(label = "70%",command =opacity70)
    opacitymenu.add_command(label = "60%",command =opacity60)
    opacitymenu.add_command(label = "50%",command =opacity50)
    filemenu.add_cascade(label = "Opacity",menu = opacitymenu)

    musicframe = LabelFrame(root,bg = "black" ,relief = GROOVE)
    musicframe.place(x=160,y=50,width= 260,height=300)

    buttonframe = LabelFrame(root,bg="black",bd =0,relief=GROOVE)
    buttonframe.place(x=160,y=400,width=600,height =80)

    frame1 = LabelFrame(root,bg ="black", relief = GROOVE) 
    frame1.place(x=600,y=0,width=400, height = 500)

    label1=Label(musicframe,bg = "black",image=photo,bd = 0,relief = GROOVE)
    label1.pack(expand = True ,fill = BOTH)
    #Label(musicframe ,font = ("times new roman",15,"bold"),bg = "black",fg = "red",bd = 0,relief = GROOVE).grid(row=1,column=2)
    label2 =Label(root,text = "Welcome to Musicfy ",textvariable=song,bg = "red",font=("times new roman",11),fg = "black",bd = 0,relief = GROOVE)

    label2.pack(side = BOTTOM,fill = BOTH)

    #listbox

    playlist = Listbox(frame1,selectbackground="gold",selectmode=SINGLE,font=("times new roman",12,"bold"),bg="black",fg="red",bd=5,relief=GROOVE)
    playlist.pack(expand =True,fill = BOTH)

    musiclist()

    playbutton = Button(buttonframe, image =play ,bg = "black" ,bd =0, relief = GROOVE,command =lambda: playmusic())
    playbutton.place(x =110 ,y= 15)

    pausebutton = Button(buttonframe, image =pause ,bg = "black" ,bd =0, relief = GROOVE,command = pausemusic)

    queuebutton = Button(buttonframe,image=queuep,bg = "black",bd=1,relief = GROOVE,command = hide)
    queuebutton.place(x=400,y=15)

    backbutton = Button(buttonframe, image =back ,bg = "black" ,bd =0, relief = GROOVE,command = backcomm)
    backbutton.place(x = 0 ,y = 15)
    forwardbutton =Button(buttonframe, image =forward ,bg = "black" ,bd =0, relief = GROOVE,command = next)
    forwardbutton.place(x= 215 ,y = 15)
    volbutton = Button(root,image = vol1,bg = "black",activebackground = "red",bd = 0,relief = GROOVE,command = vol)
    volbutton.place(x=105,y=420)
    scale1 = ttk.Scale(root,from_ = 100, to=0 ,orient = VERTICAL , command_ = volume)


    root.mainloop()
