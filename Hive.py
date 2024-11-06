import tkinter as tk
from tkinter import messagebox

class TaskApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("HIVE")
        self.geometry("600x400")
        self.configure(bg="#2C3E50") 
        
        self.tasks = []

        container = tk.Frame(self, bg="#2C3E50")
        container.pack(fill="both", expand=True)
        
        self.frames = {}
        
        for Page in (HomePage, AddTaskPage, ViewTasksPage, SettingsPage):
            page_name = Page.__name__
            frame = Page(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("HomePage")
    
    def show_frame(self, page_name):
        """Bring a frame to the front"""
        frame = self.frames[page_name]
        if page_name == "ViewTasksPage":
            frame.refresh_task_list() 
        frame.tkraise()

    def add_task(self, title, description):
        """Save a new task and display a confirmation message"""
        if title:
            self.tasks.append({"title": title, "description": description})
            messagebox.showinfo("Success", "Task saved successfully!")
            self.show_frame("HomePage")
        else:
            messagebox.showwarning("Error", "Task title cannot be empty.")


class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#2C3E50") 
        self.controller = controller
        
       
        label = tk.Label(self, text="Welcome To Our Task Management App Hive", font=("Helvetica", 30, "bold"), fg="#ECF0F1", bg="#2C3E50")
        label.pack(side="top", anchor="e", padx=380, pady=50)  
       
        button_width = 20
        add_task_button = tk.Button(self, text="Add New Task", font=("Helvetica", 14), bg="#3498DB", fg="#ECF0F1",
                                    activebackground="#2980B9", activeforeground="#ECF0F1", width=button_width,
                                    command=lambda: controller.show_frame("AddTaskPage"))
        add_task_button.pack(pady=10, ipadx=20, ipady=10)
        
        view_tasks_button = tk.Button(self, text="View All Tasks", font=("Helvetica", 14), bg="#E74C3C", fg="#ECF0F1",
                                      activebackground="#C0392B", activeforeground="#ECF0F1", width=button_width,
                                      command=lambda: controller.show_frame("ViewTasksPage"))
        view_tasks_button.pack(pady=10, ipadx=20, ipady=10)
        
        settings_button = tk.Button(self, text="Settings", font=("Helvetica", 14), bg="#2ECC71", fg="#ECF0F1",
                                    activebackground="#27AE60", activeforeground="#ECF0F1", width=button_width,
                                    command=lambda: controller.show_frame("SettingsPage"))
        settings_button.pack(pady=10, ipadx=20, ipady=10)


class AddTaskPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#2C3E50")
        self.controller = controller
        

        label = tk.Label(self, text="Add New Task", font=("Helvetica", 24, "bold"), fg="#ECF0F1", bg="#2C3E50")
        label.pack(pady=20)
        
   
        task_label = tk.Label(self, text="Task Title:", font=("Helvetica", 20), fg="#ECF0F1", bg="#2C3E50")
        task_label.pack(pady=5)
        self.task_entry = tk.Entry(self, font=("Helvetica", 25), width=27)
        self.task_entry.pack(pady=5)
        
        desc_label = tk.Label(self, text="Task Description:", font=("Helvetica", 20), fg="#ECF0F1", bg="#2C3E50")
        desc_label.pack(pady=5)
        self.desc_entry = tk.Text(self, font=("Helvetica", 16), width=40, height=5)
        self.desc_entry.pack(pady=5)
        
        save_button = tk.Button(self, text="Save Task", font=("Helvetica", 14), bg="#3498DB", fg="#ECF0F1",
                                activebackground="#2980B9", activeforeground="#ECF0F1",
                                command=lambda: controller.add_task(self.task_entry.get(), self.desc_entry.get("1.0", "end-1c")))
        save_button.pack(pady=15, ipadx=20, ipady=5)
        
        back_button = tk.Button(self, text="Back to Home", font=("Helvetica", 12), bg="#E74C3C", fg="#ECF0F1",
                                activebackground="#C0392B", activeforeground="#ECF0F1", command=lambda: controller.show_frame("HomePage"))
        back_button.pack(pady=5)

class ViewTasksPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#2C3E50")
        self.controller = controller
        
        label = tk.Label(self, text="All Tasks", font=("Helvetica", 24, "bold"), fg="#ECF0F1", bg="#2C3E50")
        label.pack(pady=20)
        
        self.task_listbox = tk.Listbox(self, font=("Helvetica", 20), width=50, height=10, bg="#ECF0F1")
        self.task_listbox.pack(pady=10)
        
        back_button = tk.Button(self, text="Back to Home", font=("Helvetica", 12), bg="#E74C3C", fg="#ECF0F1",
                                activebackground="#C0392B", activeforeground="#ECF0F1", command=lambda: controller.show_frame("HomePage"))
        back_button.pack(pady=10)

    def refresh_task_list(self):
        """Update the listbox with current tasks"""
        self.task_listbox.delete(0, tk.END)
        for task in self.controller.tasks:
            self.task_listbox.insert(tk.END, f"{task['title']}: {task['description']}")

class SettingsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#2C3E50")
        self.controller = controller
        
        label = tk.Label(self, text="Settings", font=("Helvetica", 24, "bold"), fg="#ECF0F1", bg="#2C3E50")
        label.pack(pady=20)
        
        settings_label = tk.Label(self, text="No settings available yet", font=("Helvetica", 14), fg="#ECF0F1", bg="#2C3E50")
        settings_label.pack(pady=10)
        
        back_button = tk.Button(self, text="Back to Home", font=("Helvetica", 12), bg="#E74C3C", fg="#ECF0F1",
                                activebackground="#C0392B", activeforeground="#ECF0F1", command=lambda: controller.show_frame("HomePage"))
        back_button.pack(pady=10)

if __name__ == "__main__":
    app = TaskApp()
    app.mainloop()
