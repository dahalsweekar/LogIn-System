from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Sign Up")
        self.root.resizable(0, 0)
        self.root.geometry('990x660+50+50')
        self.bg_image = ImageTk.PhotoImage(file='./gui/bg.png')

        self.bg_Label = Label(self.root, image=self.bg_image)
        self.bg_Label.pack()

        self.heading = Label(self.root, text="USER LOGIN", font=('Microsoft Yahei UI Light', 23, 'bold'),
                             bg='white',
                             fg='SlateBlue4')
        self.heading.place(x=605, y=120)

        # Username
        self.usernameEntry = Entry(self.root, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'),
                                   bd=0,
                                   fg='SlateBlue4')
        self.usernameEntry.place(x=580, y=200)
        self.usernameEntry.insert(0, 'Username')
        self.usernameEntry.bind('<FocusIn>', self.user_enter)
        Frame(root, width=250, height=2, bg="SlateBlue4").place(x=580, y=222)

        # Password
        self.passwordEntry = Entry(self.root, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'),
                                   bd=0,
                                   fg='SlateBlue4')
        self.passwordEntry.place(x=580, y=260)
        self.passwordEntry.insert(0, 'Password')
        self.passwordEntry.bind('<FocusIn>', self.pass_enter)
        Frame(root, width=250, height=2, bg="SlateBlue4").place(x=580, y=282)

        self.openeye = PhotoImage(file='./gui/openeye.png')
        self.eyeButton = Button(self.root, image=self.openeye, bd=0, bg='white', activebackground='white',
                                cursor='hand2', command=self.hide)
        self.eyeButton.place(x=800, y=255)

        # Forget
        self.forgotButton = Button(self.root, text='Forgot Password?', bd=0, bg='white', activeforeground='SlateBlue4',
                                   cursor='hand2',
                                   font=('Microsoft Yahei UI Light', 9, 'bold'),
                                   fg='SlateBlue4',
                                   command=self.hide)
        self.forgotButton.place(x=700, y=295)

        self.loginButton = Button(self.root, text='Login', font=('Open Sans', 16, 'bold'),
                                  fg='white',
                                  bg='SlateBlue4',
                                  activebackground='white',
                                  activeforeground='SlateBlue4',
                                  cursor='hand2',
                                  bd=0,
                                  width=18,
                                  command=self.login_user)
        self.loginButton.place(x=579, y=350)

        self.orLabel = Label(self.root, text='__________OR__________', font=('Open Sans', 16), fg='SlateBlue4',
                             width=25)
        self.orLabel.place(x=579, y=400)

        self.facebook_logo = PhotoImage(file='./gui/facebook.png')
        self.fbLabel = Label(self.root, image=self.facebook_logo, bg='white')
        self.fbLabel.place(x=640, y=440)

        self.google_logo = PhotoImage(file='./gui/google.png')
        self.googleLabel = Label(self.root, image=self.google_logo, bg='white')
        self.googleLabel.place(x=690, y=440)

        self.twitter_logo = PhotoImage(file='./gui/twitter.png')
        self.twitterLabel = Label(self.root, image=self.twitter_logo, bg='white')
        self.twitterLabel.place(x=740, y=440)

        self.signupLabel = Label(self.root, text="Dont have an account?", font=('Open Sans', 9, 'bold'),
                                 fg='SlateBlue4',
                                 bg='white')
        self.signupLabel.place(x=590, y=500)

        self.newAccButton = Button(self.root, text='Create', font=('Open Sans', 9, 'bold'),
                                   fg='SlateBlue4',
                                   bg='white',
                                   activebackground='white',
                                   activeforeground='SlateBlue4',
                                   cursor='hand2',
                                   bd=0,
                                   command=self.signup_page)
        self.newAccButton.place(x=750, y=495)

    def user_enter(self, event):
        if self.usernameEntry.get() == 'Username':
            self.usernameEntry.delete(0, END)

    def pass_enter(self, event):
        if self.passwordEntry.get() == 'Password':
            self.passwordEntry.delete(0, END)

    def hide(self):
        self.openeye.config(file='./gui/closeye.png')
        self.passwordEntry.config(show='*')
        self.eyeButton.config(command=self.show)

    def show(self):
        self.openeye.config(file='./gui/openeye.png')
        self.passwordEntry.config(show='')
        self.eyeButton.config(command=self.hide)

    def signup_page(self):
        login.destroy()
        import signup

    def login_user(self):
        if self.usernameEntry.get() == '' or self.passwordEntry.get() == '':
            messagebox.showerror('Error', 'All fields are required')
        else:
            try:
                db = pymysql.connect(
                    host='localhost',
                    user='root',
                    passwd='Mysqlspace@51'
                )
                my_cursor = db.cursor()
            except:
                messagebox.showerror('Error', 'Connection is not established. Try again.')
                return

            query = 'use userdata'
            my_cursor.execute(query)
            query = 'select * from data where username=%s and password=%s'
            values = (self.usernameEntry.get(), self.passwordEntry.get())
            my_cursor.execute(query, values)
            row = my_cursor.fetchone()
            if row is None:
                messagebox.showerror('Error', 'Invalid username and password')
            else:
                messagebox.showinfo('Welcome', 'Login Successful')


login = Tk()
ob = Login(login)
login.mainloop()
