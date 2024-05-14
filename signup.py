from tkinter import *
from PIL import ImageTk
import pymysql
from tkinter import messagebox


class SignUp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sign Up")
        self.root.resizable(0, 0)
        self.root.geometry('990x660+50+50')
        self.bg_image = ImageTk.PhotoImage(file='./gui/bg.png')

        self.bg_Label = Label(self.root, image=self.bg_image)
        self.bg_Label.grid()

        self.frame = Frame(self.root, bg='white')
        self.frame.place(x=554, y=100)

        self.heading = Label(self.frame, text="CREATE AN ACCOUNT", font=('Microsoft Yahei UI Light', 20, 'bold'),
                             bg='white',
                             fg='SlateBlue4')
        self.heading.grid(row=0, column=0)

        # Email
        self.emailLabel = Label(self.frame, text="Email", font=('Microsoft Yahei UI Light', 12, 'bold'), bg='white',
                                fg='SlateBlue4')
        self.emailLabel.grid(row=1, column=0, sticky='w', padx=15, pady=10)
        self.emailEntry = Entry(self.frame, text="Email", font=('Microsoft Yahei UI Light', 12, 'bold'), bg='white',
                                fg='SlateBlue4')
        self.emailEntry.grid(row=2, column=0, sticky='w', padx=15)

        # Email
        self.emailLabel = Label(self.frame, text="Email", font=('Microsoft Yahei UI Light', 12, 'bold'), bg='white',
                                fg='SlateBlue4')
        self.emailLabel.grid(row=1, column=0, sticky='w', padx=15, pady=10)
        self.emailEntry = Entry(self.frame, text="Email", font=('Microsoft Yahei UI Light', 12, 'bold'), bg='white',
                                fg='SlateBlue4')
        self.emailEntry.grid(row=2, column=0, sticky='w', padx=15)

        # Username
        self.usernameLabel = Label(self.frame, text="Username", font=('Microsoft Yahei UI Light', 12, 'bold'),
                                   bg='white',
                                   fg='SlateBlue4')
        self.usernameLabel.grid(row=3, column=0, sticky='w', padx=15, pady=10)
        self.usernameEntry = Entry(self.frame, text="Username", font=('Microsoft Yahei UI Light', 12, 'bold'),
                                   bg='white',
                                   fg='SlateBlue4')
        self.usernameEntry.grid(row=4, column=0, sticky='w', padx=15)

        # Password
        self.passwordLabel = Label(self.frame, text="Password", font=('Microsoft Yahei UI Light', 12, 'bold'),
                                   bg='white',
                                   fg='SlateBlue4')
        self.passwordLabel.grid(row=5, column=0, sticky='w', padx=15, pady=10)
        self.passwordEntry = Entry(self.frame, text="Password", font=('Microsoft Yahei UI Light', 12, 'bold'),
                                   bg='white',
                                   fg='SlateBlue4')
        self.passwordEntry.grid(row=6, column=0, sticky='w', padx=15)

        # Confirm Password
        self.conpasswordLabel = Label(self.frame, text="Confirm Password",
                                      font=('Microsoft Yahei UI Light', 12, 'bold'),
                                      bg='white',
                                      fg='SlateBlue4')
        self.conpasswordLabel.grid(row=7, column=0, sticky='w', padx=15, pady=10)
        self.conpasswordEntry = Entry(self.frame, text="Confirm Password",
                                      font=('Microsoft Yahei UI Light', 12, 'bold'),
                                      bg='white',
                                      fg='SlateBlue4')
        self.conpasswordEntry.grid(row=8, column=0, sticky='w', padx=15)

        # Terms and Conditions
        self.check = IntVar()
        self.terms = Checkbutton(self.frame, text="I agree to the Terms & Conditions",
                                 font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white', fg='SlateBlue4',
                                 activebackground='white', cursor='hand2', variable=self.check)
        self.terms.grid(row=9, column=0, pady=10, padx=20)

        # Signup Button
        self.signupButton = Button(self.frame, text="SignUp", font=('Microsoft Yahei UI Light', 15, 'bold'), bd=0,
                                   bg='SlateBlue4', fg='white', activebackground='white', cursor='hand2',
                                   command=self.connect_db)
        self.signupButton.grid(row=10, column=0, pady=25)

        # Already have an account?
        self.aleadyAcc = Label(self.frame, text="Don't have an account?", font=('Open Sans', '9', 'bold'),
                               bg='white', fg='SlateBlue4')
        self.aleadyAcc.grid(row=11, column=0, sticky='w', padx=25)

        # Login Button
        self.loginButton = Button(self.frame, text='Log in', font=('Open Sans', 9, 'bold underline'),
                                  bg='white',
                                  fg='blue',
                                  bd=0,
                                  cursor='hand2',
                                  activebackground='white',
                                  activeforeground='blue', command=self.login_page)
        self.loginButton.place(x=190, y=395)

    def login_page(self):
        signup.destroy()
        import login

    def connect_db(self):
        if self.emailEntry.get() == '' or self.usernameEntry.get() == '' or self.passwordEntry.get() == '' or self.conpasswordEntry.get() == '':
            messagebox.showerror('Error', 'Please fill all the fields')
        elif self.passwordEntry.get() != self.conpasswordEntry.get():
            messagebox.showerror('Error', 'Password Mismatch')
        elif self.check.get() == 0:
            messagebox.showerror('Error', 'Please agree to the Terms & Conditions')
        else:
            try:
                db = pymysql.connect(
                    host='localhost',
                    user='root',
                    passwd='Mysqlspace@51'
                )
                my_cursor = db.cursor()
            except:
                messagebox.showerror('Error', 'Connection to Database failed. Please try again.')
                return

            try:
                query = 'CREATE DATABASE userdata'
                my_cursor.execute(query)
                query = 'USE userdata'
                my_cursor.execute(query)
                query = 'CREATE TABLE data(id int auto_increment primary key not null, email varchar(50), username varchar(100), password varchar(50))'
                my_cursor.execute(query)
            except:
                my_cursor.execute('use userdata')

            query = 'select * from data where username=%s'
            my_cursor.execute(query, (self.usernameEntry.get()))
            row = my_cursor.fetchone()
            if row is not None:
                messagebox.showerror('Error', 'User already exist')
            else:
                query = 'insert into data(email, username, password) values (%s,%s,%s)'
                values = (self.emailEntry.get(), self.usernameEntry.get(), self.passwordEntry.get())
                my_cursor.execute(query, values)
                db.commit()
                db.close()
                messagebox.showinfo('Success', 'Registration complete')
                self.clear()

    def clear(self):
        self.emailEntry.delete(0, END)
        self.usernameEntry.delete(0, END)
        self.passwordEntry.delete(0, END)
        self.conpasswordEntry.delete(0, END)
        self.check.set(0)
        signup.destroy()
        import login


signup = Tk()
ob = SignUp(signup)
signup.mainloop()
