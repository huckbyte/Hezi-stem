import re
from tkinter import *
from body import All_functions,bot_name
from PIL import ImageTk ,Image
from itertools  import count

#from alexa import wishMe

bg_gray  = '#ABB2B9'
bg_color  = '#17202A'
# text_color = '#EAECEE'
text_color = 'green'
Font = 'Helvetica 14'
Font_bold = 'Helvetica 13 bold'

image_list = []
gif_duration = ''
images_counting = -1


global msg2,msg3,time_label

class ChatApplication:
    
    def __init__(self):
        self.window = Tk()
        #main window initial
        self._setup_main_window()
        
    def run(self):
        self.extra_image('Earth.gif')
        self.window.after(1000,self.play_slider)
        self.window.mainloop()
        
      #layout  
    def _setup_main_window(self):
        self.window.title("chat")
        self.window.resizable(width=False,height=False)
        self.window.configure(width=800,height=800,bg=bg_color)
        
        #gif image
        # self.slider_lb = Label(self.window)
        # # self.slider_lb.place(x=200,y=200)
        # self.slider_lb.place(relheight=0.745,relwidth=1,rely=0.08)
        
       # head_label = Label()
        head_label = Label(self.window,bg = bg_color,fg= text_color,
                          text='welcom',font=Font_bold,pady=10)
        head_label.place(relwidth=1)
        
        #divider
        line = Label(self.window,width = 450, bg="green")
        line.place(relwidth =1, rely =0.07,relheight=0.012)
        
        #text area
        #text_widge is a text vvariable
        self.text_widge = Text(self.window,width=20,height=2,bg=bg_color,fg=text_color,font=Font,padx=5,pady=5)

        
        
        self.text_widge.place(relheight=0.630,relwidth=0.61,rely=0.1,relx=0.0)
        # self.text_widge.place(rely= 0.3,relx=0.5)
        self.text_widge.configure(cursor="arrow",state=DISABLED)
        
        #scrool
        scrollbar = Scrollbar(self.text_widge)
        scrollbar.place(relheight=1,relx=0.974)
        scrollbar.configure(command=self.text_widge.yview)
        
        
        #bottom label
        bottom_label = Label(self.window,bg='white',height=80)
        bottom_label.place(relwidth=1,rely=0.825)
   
        #message box
        
        self.msg_entry = Entry(self.window,bg='#2C3E50',fg=text_color,font=Font)
        self.msg_entry.place(relheight=0.10,relwidth=0.61,rely=0.725,relx=0.0)
        self.msg_entry.focus()
        self.msg_entry.bind('<Return>',self.enter)
        
        #send bottom
        self.send_img = PhotoImage(file="start.png")
        send_button= Button(bottom_label,image=self.send_img,
                            command=lambda: self.enter(None))
        # send_button= Button(bottom_label,font=Font_bold,width=20,bg=bg_gray,image=send_img,
                            # command=lambda: self.enter(None))
        send_button.place(relx=0.77,rely=0.008,relheight=0.06,relwidth=0.32)
        
        #gif rorating
        
        self.slider_lb = Label(self.window,width=300,height=300)
        self.slider_lb.place(rely= 0.1,relx=0.61)
        # self.slider_lb.place(relheight=0.745,relwidth=1,rely=0.08)
        
        #get text input
    def enter(self,event):
        msg = self.msg_entry.get()
        self.insert_messange(msg,"<♦paps♣>")
        
    def insert_messange(self,msg,sender):
        if not msg:
            return
        #delete existing text
        self.msg_entry.delete(0,END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widge.configure(state=NORMAL)
        self.text_widge.insert(END,msg1)
        self.text_widge.configure(state=DISABLED)
        
        
        #get responce from import
        
        msg2 = f"{bot_name}: {All_functions.get_responces(msg)}\n\n"
        self.text_widge.configure(state=NORMAL)
        self.text_widge.insert(END,msg2)
        self.text_widge.configure(state=DISABLED)
       # self.text_widge.delete(msg2)
       
       
        
        #to see last msg
        self.text_widge.see(END)
        
        
    def extra_image(self,path):
        global gif_duration
        image = Image.open(path)# type: ignore

        for i in count(1):
            try:
                image_list.append(ImageTk.PhotoImage(image.copy()))
                image.seek(i)
                
            except Exception as error:
                # print(error)
                break
                
        gif_duration = int(image.info['duration'])
    def play_slider(self):
        global images_counting
        
        try:
            images_counting +=1
            
            self.slider_lb.config(image=image_list[images_counting])
            self.window.after(gif_duration,self.play_slider)# type: ignore
            
        except Exception as error:
            # print(error)
            images_counting = -1
            self.window.after(gif_duration,self.play_slider)     # type: ignore
   
            
        
if __name__ == "__main__":
        
    app = ChatApplication()
    app.run()