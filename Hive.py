import tkinter as tk
from tkinter import messagebox
import time
import ttkbootstrap as ttk  
import datetime
from PIL import Image, ImageTk

class TaskApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("HIVE")
        self.geometry("1550x850")

        self.tasks = []
        self.theme = "light" 

        main_frame = tk.Frame(self)
        main_frame.pack(fill="both", expand=True)

        self.button_panel = tk.Frame(main_frame, width=100, padx=100, bg="#C3C7F3")
        self.button_panel.pack(side="left", fill="y", padx=(10, 0), pady=10)

        separator = tk.Frame(main_frame, width=2, bg="black")
        separator.pack(side="left", fill="y", padx=0)
        
        self.content_frame = tk.Frame(main_frame)
        self.content_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)
  
        self.frames = {}
        for Page in (HomePage, AddTaskPage, ViewTasksPage, StopwatchPage, SettingsPage):
            page_name = Page.__name__
            frame = Page(parent=self.content_frame, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")
        self.create_nav_buttons()

    def create_nav_buttons(self):
        buttons_info = [
            ("🏠 Home", "HomePage"),
            ("➕ Add Task", "AddTaskPage"),
            ("📋 View Tasks", "ViewTasksPage"),
            ("⏱️ Stopwatch", "StopwatchPage"),
            ("⚙️ Settings", "SettingsPage"),
        ]

        title_label = tk.Label(
            self.button_panel, text=" HIVE ", font=("Georgia", 35, "bold",),
            fg="orange", bg="#34495E"
        )

        title_label.pack(pady=(50, 20))      
            
        for text, page_name in buttons_info:
            button = ttk.Button(
                self.button_panel, text=text, width=20, bootstyle="dark-outline",
                command=lambda name=page_name: self.show_frame(name)
            )
            button.pack(pady=15, padx=5, ipadx=20)    

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        if page_name == "ViewTasksPage":
            frame.refresh_task_list()
        frame.tkraise()

    def switch_theme(self):
        """Switch the theme between light and dark."""
        if self.theme == "light":
            self.theme = "dark"
        else:
            self.theme = "light"
        
        self.apply_theme()

    def apply_theme(self):
        """Apply the current theme to the app."""
        if self.theme == "light":
            self.config(bg="#ECF0F1") 
            self.button_panel.config(bg="#f2f0ef")
        else:
            self.config(bg="#2C3E50")  
            self.button_panel.config(bg="#34495E")

        for frame in self.frames.values():
            frame.apply_theme(self.theme)
                    # ---------------------   Home Page    -------------------------------

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # image_path = r"C:\DesktopApp\Test\Image1.jpg"  
        # image_path = r"C:\DesktopApp\Test\Image.png" 
        # image_path = r"C:\DesktopApp\Test\Image3.jpg" 
        # image_path = r"C:\DesktopApp\Test\Image4.jpg"
        # image_path = r"C:\DesktopApp\Test\Image5.jpg"
        image_path = r"C:\DesktopApp\Test\Image6.jpg"
        
        
        
         
        image = Image.open(image_path)
        image = image.resize((1200, 770))  
        
        self.bg_image = ImageTk.PhotoImage(image)  
        
        canvas = tk.Canvas(self, width=1200, height=770)  
        canvas.pack(fill="both", expand=True)
        
        canvas.create_image(0, 0, image=self.bg_image, anchor="nw")  
        
        canvas.create_text(600, 120, text="Welcome To Hive", font=("Georgia", 40, "bold"), fill="#6F4E37")
        canvas.create_text(600, 200, text="Your Efficient Task Manager", font=("Georgia", 40, "bold"), fill="#6F4E37")

        
        # label = tk.Label(self, text="Welcome To Hive", font=("Georgia", 40, "bold"), fg="#A36361")
        # label.pack(pady=(150, 40),padx=200)
        # sub_label = tk.Label(self, text="Your Efficient Task Manager", font=("Georgia", 40), fg="#BDC3C7", bg="#34495E")
        # sub_label.pack(pady=10)


def custom_messagebox(title, message, color):
    custom_box = tk.Toplevel()
    custom_box.title(title)
    custom_box.configure(bg=color)

    width, height = 500, 200  
    screen_width = custom_box.winfo_screenwidth()
    screen_height = custom_box.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    custom_box.geometry(f"{width}x{height}+{x}+{y}")

    label = tk.Label(custom_box, text=message, font=("Georgia", 15), bg=color, fg="white", wraplength=450)
    label.pack(pady=40)

    ok_button = tk.Button(custom_box, text="OK", font=("Georgia", 20), command=custom_box.destroy, bg="white", fg="black")
    ok_button.pack(pady=10)

    custom_box.grab_set()
    custom_box.mainloop()


# ------------------------------ADD TASK PAGE----------------------


class AddTaskPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.canvas = tk.Canvas(self, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True, pady=2)

        self.create_gradient("#C850C0", "#4158D0")  
        
        self.canvas.create_text(570, 80, text="Add New Task", font=("Georgia", 40, "bold"), fill="#6F4E37")

        task_label = self.canvas.create_text(225, 150, text="Task Title", font=("Georgia", 20, "bold"), fill="#FFFFFF", anchor="w")
        
        self.task_entry = tk.Entry(self.canvas, font=("Georgia", 18), bg="#f2f0ef", fg="#f2f0ef", relief="groove", bd=2)
        self.canvas.create_window(550, 200, window=self.task_entry, width=650, height=40)

        desc_label = self.canvas.create_text(225, 270, text="Task Description", font=("Georgia", 20, "bold"), fill="#FFFFFF", anchor="w")

        self.desc_entry = tk.Text(self.canvas, font=("Georgia", 18), bg="#FFFFFF", fg="#1C2833", relief="groove", bd=2, height=4)
        self.canvas.create_window(550, 350, window=self.desc_entry, width=650, height=100)
        
        task_label = self.canvas.create_text(225, 450, text="Execution Time", font=("Georgia", 20, "bold"), fill="#FFFFFF", anchor="w")
        
        self.Ex_Time = tk.Entry(self.canvas, font=("Georgia", 18), bg="#FFFFFF", fg="#1C2833", relief="groove", bd=2)
        self.canvas.create_window(550, 500, window=self.Ex_Time, width=650, height=40)
        
        priority_label = self.canvas.create_text(225, 570, text="Task Priority", font=("Georgia", 20, "bold"), fill="#FFFFFF", anchor="w")

        self.priority_var = tk.StringVar()
        self.priority_menu = ttk.Combobox(self.canvas, textvariable=self.priority_var, font=("Georgia", 15))
        self.priority_menu['values'] = ("Select Priority", "High", "Medium", "Low")
        self.canvas.create_window(550, 610, window=self.priority_menu, width=650, height=35)
        self.priority_menu.current(0)

        save_button = tk.Button(
            self.canvas, text="Save Task", font=("Georgia", 18, "bold"),
            bg="#2980B9", fg="#FFFFFF", activebackground="#3498DB",
            activeforeground="#FFFFFF", relief="flat",
            command=self.save_task, padx=8, pady=8, cursor="hand2"
        )
        self.canvas.create_window(600, 700, window=save_button, width=200, height=50)

        save_button.bind("<Enter>", lambda e: save_button.config(bg="#3498DB"))
        save_button.bind("<Leave>", lambda e: save_button.config(bg="#2980B9"))

    def create_gradient(self, *colors):
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        gradient_steps = 100
        num_colors = len(colors)

        for i in range(gradient_steps):
            t = i / gradient_steps  
            color = colors[0]  
            for j in range(1, num_colors):
                color = self.mix_colors(color, colors[j], t)  
            self.canvas.create_rectangle(0, height * i / gradient_steps, width,
                                         height * (i + 1) / gradient_steps, outline="", fill=color)

    def mix_colors(self, color1, color2, t):
        c1 = tuple(int(color1.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4))
        c2 = tuple(int(color2.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4))
        mixed = tuple(int(c1[i] * (1 - t) + c2[i] * t) for i in range(3))
        return "#%02x%02x%02x" % mixed

    def save_task(self):
        title = self.task_entry.get().strip()
        Execution_Time = self.Ex_Time.get().strip()
        description = self.desc_entry.get("1.0", "end-1c").strip()
        priority = self.priority_var.get().strip()

        if not title or not description:
            custom_messagebox("Error", "Both Task Title and Description are required!!!", "red")
        elif priority == "Select Priority":
            custom_messagebox("Error", "Please select a priority level for the task!!!", "orange")
        else:
            current_date = datetime.datetime.now().strftime("%d/%m/%Y")
            current_datetime = datetime.datetime.now()
            # :%S
            current_time = current_datetime.strftime("%H:%M")
            serial_number = len(self.controller.tasks) + 1
            task_data = {
                "serial": serial_number,
                "date": current_date,
                "title": title,
                "description": description,
                "priority": priority,
                "time": current_time,
                "ExecutionTime":Execution_Time
            }
            self.controller.tasks.append(task_data)
            custom_messagebox("Success", f"Task No {serial_number} added successfully!!!", "green")

            self.task_entry.delete(0, tk.END)
            self.desc_entry.delete("1.0", tk.END)
            self.priority_var.set("Select Priority")



            # --------------------Task View Page---------------------------


class ViewTasksPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#D5DBDB")  
        self.controller = controller

        label = tk.Label(
            self, 
            text="📌 YOUR TASKS", 
            font=("Georgia", 18, "bold"), 
            fg="#2C3E50", 
            bg="#D5DBDB"
        )
        label.pack(pady=(10, 10))

        self.create_task_table("🔥 High Priority Tasks", "#C0392B", 0)  
        self.create_task_table("⚡ Medium Priority Tasks", "#D68910", 1)  
        self.create_task_table("✅ Low Priority Tasks", "#1E8449", 2) 

        self.refresh_task_list()

    def create_task_table(self, title, color, row):
        frame = tk.Frame(self, bg="#D5DBDB", height=200)  
        frame.pack(fill="both", expand=False, padx=10, pady=5)

        label = tk.Label(
            frame, 
            text=title, 
            font=("Georgia", 14, "bold"), 
            fg="white", 
            bg=color, 
            padx=10, 
            pady=5
        )
        label.pack(fill="x")

        table_scroll_y = tk.Scrollbar(frame, orient="vertical")

        table = ttk.Treeview(
            frame,
            columns=("Serial", "DateTime", "ExecutionTime", "Title", "Description"),
            show="headings",
            yscrollcommand=table_scroll_y.set,
            selectmode="browse",
            height=6  
        )

        table_scroll_y.config(command=table.yview)
        table_scroll_y.pack(side="right", fill="y")

        # ALL Columns
        table.heading("Serial", text="Serial No", anchor="center")
        table.heading("DateTime", text="Date & Time", anchor="center")  
        table.heading("ExecutionTime", text="Task Deadline", anchor="center")
        table.heading("Title", text="Task Title", anchor="w")
        table.heading("Description", text="Task Details", anchor="w")

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Helvetica", 15, "bold"), foreground="#1A5276")
        style.configure("Treeview", font=("Helvetica", 15), foreground="#2C3E50", rowheight=21)

        table.column("Serial", width=80, anchor="center")
        table.column("DateTime", width=180, anchor="center")  
        table.column("ExecutionTime", width=50, anchor="center")
        table.column("Title", width=100, anchor="w")
        table.column("Description", width=220, anchor="w")

        table.pack(fill="both", expand=True, padx=5, pady=5, ipadx=5, ipady=5)

        if row == 0:
            self.high_priority_table = table
        elif row == 1:
            self.medium_priority_table = table
        else:
            self.low_priority_table = table

        table.bind("<Double-1>", self.confirm_and_delete_task)

    def confirm_and_delete_task(self, event):
        selected_item = event.widget.selection()
        if selected_item:
            task_values = event.widget.item(selected_item, "values")
            confirm = messagebox.askyesno("Delete Task", f"Are you sure you want to delete this task?\n\n{task_values}")
            if confirm:
                self.delete_task(task_values[0])  

    def delete_task(self, serial):
        serial = int(serial)
        self.controller.tasks = [task for task in self.controller.tasks if task["serial"] != serial]

        for index, task in enumerate(self.controller.tasks, start=1):
            task["serial"] = index

        self.refresh_task_list()

    def refresh_task_list(self):
        self.high_priority_table.delete(*self.high_priority_table.get_children())
        self.medium_priority_table.delete(*self.medium_priority_table.get_children())
        self.low_priority_table.delete(*self.low_priority_table.get_children())

        high_priority_serial = 1
        medium_priority_serial = 1
        low_priority_serial = 1

        for task in self.controller.tasks:
            table = None
            serial = None

            if task["priority"] == "High":
                table = self.high_priority_table
                serial = high_priority_serial
                high_priority_serial += 1
            elif task["priority"] == "Medium":
                table = self.medium_priority_table
                serial = medium_priority_serial
                medium_priority_serial += 1
            elif task["priority"] == "Low":
                table = self.low_priority_table
                serial = low_priority_serial
                low_priority_serial += 1

            if table:
                
                date_time = f"{task['date']} {task['time']}"  

                task_data = (
                    serial,  
                    date_time,
                    task["ExecutionTime"],
                    task["title"],
                    task["description"]
                )

                task_item = table.insert(
                    "",
                    "end",
                    values=task_data
                )

                table.item(task_item, values=(
                    serial,  
                    f"{task['date']} ({task['time']})",
                    f"                           {task['ExecutionTime']}",
                    f" {task['title']}",
                    f"     {task['description']}",
                ))

                    # For No Tasks message
        for table in [self.high_priority_table, self.medium_priority_table, self.low_priority_table]:
            if not table.get_children():
                
                for _ in range(2):  
                    table.insert("", "end", values=("", "", "", "", ""))  

                no_task_message = table.insert(
                    "", 
                    "end", 
                    values=("", "", "", "", " " * 10 + "⚠ No Tasks Added Yet! ⚠")  
                )

                table.tag_configure("no_tasks", font=("Helvetica", 16, "bold"), foreground="red")

                table.item(no_task_message, tags=("no_tasks",))

                
                table.column("#3", width=400, anchor="w")  
                table.column("#0", width=400, anchor="w")  
                table.item(no_task_message, values=(  "", ""," " * 15 + "⚠ No Tasks Added Yet! ⚠"))
 


            #-------------------SettingsPage------------------------

class SettingsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        image_path = r"C:\DesktopApp\Test\Image5.jpg"  
        
        image = Image.open(image_path)
        image = image.resize((1200, 770))  
        
        self.bg_image = ImageTk.PhotoImage(image)
        
        self.canvas = tk.Canvas(self, width=1200, height=770)
        self.canvas.pack(fill="both", expand=True)
        
        self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")
        
        self.canvas.create_text(600, 120, text="Settings", font=("Georgia", 40, "bold"), fill="#6F4E37")

        self.theme_button = ttk.Button(
            self, text="Switch Theme", width=15, 
            bootstyle="warning", command=self.toggle_theme
        )
        self.theme_button_window = self.canvas.create_window(250, 400, window=self.theme_button)

    def toggle_theme(self):
        """Toggle the theme between light and dark."""
        self.controller.switch_theme()

    def apply_theme(self, theme):
        """Apply the given theme to this page."""
        if theme == "light":
            self.config(bg="#ECF0F1")
            self.theme_button.config(text="Switch to Dark Theme", bootstyle="light-outline")
        else:
            self.config(bg="#34495E")
            self.theme_button.config(text="Switch to Light Theme", bootstyle="dark-outline")

        if theme == "light":
            self.canvas.config(bg="#ECF0F1")
        else:
            self.canvas.config(bg="#34495E")

class StopwatchPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.time_elapsed = 0
        self.running = False

        self.bg_image = Image.open("C:/DesktopApp/Test/Image1.jpg")  
        self.bg_image = self.bg_image.resize((1150, 850), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.canvas = tk.Canvas(self, width=1150, height=850)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")
        
        # **Digital Clock**
        self.clock_label1 = self.canvas.create_text(550, 150, text="Digital Clock", font=("Georgia", 45, "bold"), fill="white")
        self.clock_label = self.canvas.create_text(550, 250, text="", font=("Helvetica", 45, "bold"), fill="yellow")
        self.update_clock()

        # **Stopwatch**
        self.timer_label1 = self.canvas.create_text(550, 390, text="Stopwatch", font=("Georgia", 50, "bold"), fill="white")
        self.timer_label = self.canvas.create_text(550, 500, text="0:00:00.00", font=("Helvetica", 50, "bold"), fill="yellow")
        
        # **Buttons 
        start_button = ttk.Button(self, text="START", width=20, bootstyle="success", command=self.start_timer)
        self.start_button_window = self.canvas.create_window(380, 620, window=start_button)

        stop_button = ttk.Button(self, text="STOP", width=20, bootstyle="danger", command=self.stop_timer)
        self.stop_button_window = self.canvas.create_window(560, 620, window=stop_button)

        reset_button = ttk.Button(self, text="RESET", width=20, bootstyle="warning", command=self.reset_timer)
        self.reset_button_window = self.canvas.create_window(740, 620, window=reset_button)
       
        start_button.config(padding=(10, 15))  
        stop_button.config(padding=(10, 15))   
        reset_button.config(padding=(10, 15)) 
        
    def update_clock(self):
        hour = time.strftime("%I")
        minute = time.strftime("%M")
        second = time.strftime("%S")
        am_pm = time.strftime("%p")
        self.canvas.itemconfig(self.clock_label, text=f"{hour}:{minute}:{second} {am_pm}")
        self.after(1000, self.update_clock)

    def start_timer(self):
        if not self.running:
            self.running = True
            self.update_timer()

    def stop_timer(self):
        self.running = False

    def reset_timer(self):
        self.running = False
        self.time_elapsed = 0
        self.canvas.itemconfig(self.timer_label, text="0:00:00.00")

    def update_timer(self):
        if self.running:
            self.time_elapsed += 10
            milliseconds = self.time_elapsed % 1000 // 10
            total_seconds = self.time_elapsed // 1000
            minutes, seconds = divmod(total_seconds, 60)
            hours, minutes = divmod(minutes, 60)
            self.canvas.itemconfig(self.timer_label, text=f"{hours}:{minutes:02d}:{seconds:02d}.{milliseconds:02d}")
            self.after(10, self.update_timer)
    
    
if __name__ == "__main__":
    app = TaskApp()
    app.mainloop()
