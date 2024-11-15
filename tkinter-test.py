import tkinter as tk
root = tk.Tk()

root.geometry("310x500")
root.title("Server Instance - EIM")

message = tk.StringVar()

def send_button_action():
    chat_log.insert(tk.END, enter_message.get() + "\n")
    enter_message.delete(0, len(enter_message.get()))

chat_log = tk.Text(root, height = 20, width = 36, font=("Times New Roman", 12, "bold"), relief="sunken")
enter_message = tk.Entry(root, width = 18, font=("Arial", 12), textvariable = message, relief="sunken")
send_button = tk.Button(root, text = "Enter", command = send_button_action)

chat_log.pack()
enter_message.pack()
send_button.pack()
root.mainloop()