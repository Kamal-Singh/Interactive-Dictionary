import tkinter as tk
import dict

def search_command():
    str1=e1_data.get()
    global ans
    ans=dict.search(str1,dict.data)
    if type(ans)==list:
         lb1.delete(0,tk.END)
         for i in ans:
             lb1.insert(tk.END,i)
    else:
        lb1.delete(0,tk.END)
        lb1.insert(tk.END,ans)

def get_selected(event):
    index=lb1.curselection()[0]
    lb1.delete(0,tk.END)
    for i in dict.data[ans[index]]:
        lb1.insert(tk.END,i)

window=tk.Tk()

window.wm_title("Interactive Dictionary")

e1_data=tk.StringVar()
e1=tk.Entry(window,width=45,textvariable=e1_data)
e1.grid(row=0,column=0)

b1=tk.Button(window,text="Search",width=15,command=search_command)
b1.grid(row=0,column=1,columnspan=2)

lb1=tk.Listbox(window,width=70)
lb1.grid(row=2,column=0,columnspan=2)
lb1.bind("<<ListboxSelect>>",get_selected)

sb1=tk.Scrollbar(window)
sb1.grid(row=2,column=2)

lb1.configure(yscrollcommand=sb1.set)
sb1.configure(command=lb1.yview)

sb2=tk.Scrollbar(window, orient=tk.HORIZONTAL)
sb2.grid(row=3,column=0,columnspan=2)
lb1.configure(xscrollcommand=sb2.set)
sb2.configure(command=lb1.xview)


window.mainloop()