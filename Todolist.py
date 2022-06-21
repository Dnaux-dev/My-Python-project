""""
  Python To-do list is a software that holds information about an upcoming tasks or events
  The To-do app contains the following features; listbox,scrollbars, frame, buttons,Entry box, message box.
"""
# import all functions from tkinter
import tkinter
# import the messagebox class from tkinter
import tkinter.messagebox
import pickle
# create a window
ws = tkinter.Tk()
ws.title("To-Do App by Daniel")


def add_task():
    task =entry_task.get()
    if task !="":
        lb_tasks.insert(tkinter.END,task)
        entry_task.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!",message="Enter a task")

def delete_task():
    try:
        task_index = lb_tasks.curselection()[0]
        lb_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(
            title="Warning!", message="Select a task.")


def load_tasks():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        lb_tasks.delete(0, tkinter.END)
        for task in tasks:
            lb_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(
            title="Warning!", message="Cannot find datafile")


def save_tasks():
    tasks = lb_tasks.get(0, lb_tasks.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))


# create GUI
frame_tasks = tkinter.Frame(ws)
frame_tasks.pack()

lb_tasks = tkinter.Listbox(frame_tasks, height=10, width=50)
lb_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

lb_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=lb_tasks.yview)

entry_task = tkinter.Entry(ws, width=50)
entry_task.pack()

button_add_task = tkinter.Button(
    ws, text="Add task", width=48, command=add_task)
button_add_task.pack()

button_delete_task = tkinter.Button(
    ws, text="Delete task", width=48, command=delete_task)
button_delete_task.pack()

button_load_tasks = tkinter.Button(
    ws, text="Load tasks", width=48, command=load_tasks)
button_load_tasks.pack()

button_save_tasks = tkinter.Button(
    ws, text="Save tasks", width=48, command=save_tasks)
button_save_tasks.pack()


# Start the GUI
ws.mainloop()
