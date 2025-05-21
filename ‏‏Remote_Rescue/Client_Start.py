import tkinter as tk
from tkinter import PhotoImage
from Client import Client

#def Confirm_Details():
#    try:
#        host = ip.get()
#        port = int(port_Entry.get())
#        root.destroy()
#        dic['host'] = host
#        dic['port'] = port
#    except ValueError:
#        lab = tk.Label(root, text= 'Please enter a number for your port.', font= ('Helvetica', 18))
#        lab.pack(pady=20)
#        port_Entry.delete()
#        Confirm_Details()

#root = tk.Tk()
#oot.title('Remote Rescue')
#root.geometry('1024x900')
#root.resizable(False, False)


#ip_label = tk.Label(root, text= 'Enter desired IP Adress.', font= ('Helvetica', 18))
#ip_label.pack(pady= 20)

#ip = tk.Entry(root, width= 20, font= ('Helvetica', 18))
#ip.pack()

#port_label =  tk.Label(root, text= 'Enter Your desired port number.', font= ('Helvetica', 18))
#port_label.pack(pady= 20)               


#port_Entry = tk.Entry(root, width= 20, font= ('Helvetica', 18))
#port_Entry.pack()

#dic = {
#    'host': '' , 
#    'port': 0
#}

#Button = tk.Button(root, text='Confirm', command=Confirm_Details)
#Button.pack(pady= 40)

#root.mainloop()

#print(dic)
#host = dic['host']
#port = dic['port']  


parent = tk.Tk()
parent.title('Remote Rescue')
parent.geometry('1024x900')
parent.resizable(False, False)

# Create the main window
# Load the image 
screen_image = PhotoImage(file="Home_Screen.png")

# Create a label to display the image
image_label = tk.Label(parent, image=screen_image)
image_label.pack()
parent.after(5000, parent.destroy)
# Start the Tkinter event loop
parent.mainloop()
Client()