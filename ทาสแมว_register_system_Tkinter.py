
from tkinter import *

def register_user():
    name_info = name.get()
    email_info = email.get()
    username_info = username.get()
    password_info = password.get()
    

    file=open(username_info+".txt", "w")
    file.write(name_info+"\n")
    file.write(email_info+"\n")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()
    
    name_entry.delete(0, END)
    email_entry.delete(0, END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)


    Label(screen1, text = "ลงทะเบียน สำเร็จ! \n 'ตอนนี้คุณคือหนึ่งในสมาชิกทาสแมว อคาเดมี' ", fg ="green" ,font = ("calibri", 10)).pack()
    

def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("400x300")
    
    global name
    global email
    global username
    global password
    global name_entry
    global email_entry
    global username_entry
    global password_entry
    name = StringVar()
    email = StringVar()
    username = StringVar()
    password = StringVar()

    Label(screen1, text = "กรุณากรอกรายละเอียดด้านล่าง").pack()
    Label(screen1, text = "").pack()
    #name regis
    Label(screen1, text = "ชื่อ-นามสกุล * ").pack()
    name_entry = Entry(screen1, textvariable = name)
    name_entry.pack()
    #email regis
    Label(screen1, text = "Email * ").pack()
    email_entry = Entry(screen1, textvariable = email)
    email_entry.pack()
    #username regis
    Label(screen1, text = "ชื่อผู้ใช้ * ").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    #password regis
    Label(screen1, text = "รหัสผ่าน * ").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    #register button
    Label(screen1, text = "").pack()
    Button(screen1, text ="สมัครสมาชิก", width = 10, height = 1, command = register_user).pack()

def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("400x300")

    global username
    global password
    username = StringVar()
    password = StringVar()

    #username login
    Label(screen2, text = "ชื่อผู้ใช้ * ").pack()
    username_entry = Entry(screen2, textvariable = username)
    username_entry.pack()
    #password login
    Label(screen2, text = "รหัสผ่าน * ").pack()
    password_entry = Entry(screen2, textvariable = password)
    password_entry.pack()

    Label(screen2, text = "").pack()
    Button(screen2, text ="เข้าสู่ระบบ", width = 10, height = 1, command = register_user).pack()

    print("Login EROOOOOOR!")
    
    Label(screen2, text = "อ้อ บังเอิญว่าทางทาสแมวอคาเดมีกำลังปรับปรุงระบบอยู่ ตอนนี้จึงยังล็อกอินไม่ได้ \n ขออภัยในความไม่สะดวกค่ะ (Terribly sorry from Hamie ;-;)", fg ="red" ,font = ("calibri", 8)).pack()
    

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("400x300")
    screen.title("ทาสแมว อคาเดมี")
    Label(text ="ทาสแมว อคาเดมี" , bg ="grey", width ="300", height = "2", font = ("calibri", 24)).pack()
    Label(text = "").pack()
    Button(text = "สมัครสมาชิก",height ="2" , width = "30", command = register).pack()
    Label(text = "").pack()
    Button(text = "ล็อกอิน", height ="2" , width = "30", command = login).pack()


    screen.mainloop()

main_screen()
    
    
