from tkinter import *
from datetime import date
import time
root=Tk()
def send():
    send="you:"+a.get()
    text.insert('end',"\n"+send)
    if(a.get().lower()=='hi'):
        text.insert('end','\n'+"Robot:hello")
    elif(a.get().lower()=='hey'):
        text.insert('end','\n'+"Robot:How may i help you")
    elif(a.get().lower()=='hello'):
        text.insert('end','\n'+"Robot:hi")    
    elif(a.get().lower()=='how are you'):
        text.insert('end','\n'+"Robot:I am fine.How are you")
    elif(a.get().lower()=='I am fine'):
        text.insert('end','\n'+"Robot:Nice to hear that")
    elif(a.get().lower()=='how is your day'):
        text.insert('end','\n'+"Robot:hello")
    elif(a.get().lower()=='hi'):
        text.insert('end','\n'+"Robot:good")
    elif(a.get().lower()=='how can you help me'):
        text.insert('end','\n'+"Robot:what help you need")
    elif(a.get().lower()=='what is your name'):
        text.insert('end','\n'+"Robot:my name is varsha")
    elif(a.get().lower()=='are you a human'):
        text.insert('end','\n'+"Robot:no i am a robot")
    elif(a.get().lower()=='what is todays date'):
        text.insert('end','\n'+"Robot:"+str(date.today()))  
    elif(a.get().lower()=='what is the time now'):
        text.insert('end','\n'+"Robot:"+str(time.strftime("%I:%M:%S%p")))        
    else:
        text.insert('end','\n'+"Robot:i didnt get you")        
root.title("Varsha's chatbot")
text=Text(bg="green")
text.grid(row=0,column=0,columnspan=2)
a=Entry(root,width=80)
send=Button(root,bg='yellow',text='Send',width=20,command=send)
send.grid(row=1,column=1)
a.grid(row=1,column=0)
root.mainloop()
        
