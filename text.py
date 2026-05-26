import tkinter as tk



class myapps:
    def __init__(self,root:tk.Tk):
        self.root=root
        self.root.title("text")
        self.root.geometry("640x480")
        self.root.configure(background="black")
        self.canvas=tk.Canvas(background="white",width=300,height=80)
        self.canvas.pack(padx=10,pady=10)
        self.value="hello world|"
        self.text=self.canvas.create_text(150,10,text=self.value,fill="black",width=200)
        
        self.root.bind("<KeyPress>",self.ekeys)
        self.root.focus_get()
    def ekeys(self,event):
        
        a=event.keysym
        if a=="BackSpace":
            if len(self.value)>1:
                self.value=self.value[:-1]
        else:
            self.value=self.value+a
        self.canvas.delete(self.text) 
        self.text=self.canvas.create_text(150,10,text=self.value,fill="black",width=200)




root=tk.Tk()
apps=myapps(root)
root.mainloop()