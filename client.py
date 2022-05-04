from tkinter import *
from tkinter import messagebox
from module import imgMerge

# menual text window
def openMenualFile():
    global menual_window
    menual_window = Toplevel(window)
    menual_window.geometry("490x480+480+300")
    menual_window.title("Menual")
    menual_window.resizable(False,False)
    menual_window.iconphoto(False, PhotoImage(file="./public/icon/vong.png"))

    description_frame = Frame(menual_window, relief="solid", width=1000, height=1000)
    description_frame.pack()

    # menual file read and pack label in sub window 
    menual_file = open("./menual.txt","r")
    lines = menual_file.readlines()
    linestep = 0
    for i in range(len(lines)):
        Label(description_frame, text=lines[i]).place(x=0,y=linestep)
        linestep += 20
    menual_file.close()
# input image count
def mergeImageHandller():
    # only input int type
    try:
        txt = int(input_txt.get())
        if 1 <= txt <= 999:
            imgMerge(txt)
            input_count.delete(0,5)
            messagebox.showinfo(message="Done.")
        elif txt <= 0:
            input_count.delete(0,100)
            messagebox.showerror(message="Must not be less than 0.")
        else:
            input_count.delete(0,100)
            messagebox.showerror(message="No more than 999.")

    except:
        input_count.delete(0,100)
        messagebox.showerror(message="Only input number!")
# main
if __name__ == "__main__":
    window = Tk()
    window.title("NFT Creater")
    # window show center
    screen_w = window.winfo_screenwidth()
    screen_h = window.winfo_screenheight()
    x_cordiante = int((screen_w/2)-(150))
    y_cordinate = int((screen_h/2)-(60))
    window.geometry("300x180+{}+{}".format(x_cordiante,y_cordinate))

    window.resizable(False, False)
    window.iconphoto(False, PhotoImage(file='./public/icon/vong.png'))

    label = Label(window, text="You must reading menual!").pack(side="top")
    menual_btn = Button(window, width=15,text="Menual",command=openMenualFile).pack()

    # input the number of images you want to create
    input_txt = StringVar()
    input_count = Entry(window, width=15, textvariable=input_txt)
    input_count.pack()

    make_button = Button(window, overrelief="solid", width=15, command=mergeImageHandller, repeatdelay=1000, repeatinterval=100, text="make!").pack()
    version_label = Label(window, text="v0.0.1").pack()
    window.mainloop()