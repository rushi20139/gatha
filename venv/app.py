import tkinter as tk
import requests, keyboard

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("API Display App")
        
        # Disable resizing and maximize button
        self.root.resizable(False, False)
        self.root.attributes('-fullscreen', True)
        self.root.config(bg="darkblue")

        # Set initial time (15 minutes in seconds)
        self.remaining_time = 15 * 60

        # Disable keyboard activity
        self.root.bind("<Key>", lambda e: "break")
        
        # Create and place widgets
        # Disable the Windows key
        self.disable_windows_key()
        self.create_widgets()

    def create_widgets(self):
        self.image = tk.PhotoImage(file="logo2.png")
        self.original_image = self.image.subsample(3,3)
        tk.Label(image=self.original_image, bg="darkblue").place(x=self.root.winfo_screenwidth() - 120, y=4)  # Adjust x and y as needed
        # self.text_widget = tk.Text(self.root, wrap="word", height=100, width=150, bg="darkblue", fg="white")
        # self.text_widget.pack(pady=200)

        # Define a custom font
        custom_font = ("Helvetica", 40, "bold italic")


        #Timer Label
        self.timer_label = tk.Label(self.root, text="", font= ("Helvetica", 40, "bold"), bg="darkblue", fg="white")
        self.timer_label.place(x=self.root.winfo_screenwidth() - 1520, y=50)


        # Text widget to display API content (read-only)
        self.text_widget = tk.Text(self.root, wrap="word", height=100, width=150, bg="darkblue", fg="white", font=custom_font)
        self.text_widget.pack(pady=200, padx=200, ipady=100, ipadx=100)
        # Insert text into the read-only text widget with consistent padding on each line
        padding_text = " " * 10  # Add extra spaces for padding
        lines = [
            "सकलाऽऽर्हत् – प्रतिष्ठान~मधिष्ठानं शिव – श्रियः ।",
            "भूर् – भुव :-स्वस् – त्रयीशान~मार्हन्त्यं प्रणिदध्महे"
        ]

        for line in lines:
            self.text_widget.config(state=tk.NORMAL)
            self.text_widget.insert(tk.END, padding_text + line + "\n")
            self.text_widget.config(state=tk.DISABLED)

 # Button to exit the application
        exit_button = tk.Button(self.root, text="Exit", command=self.exit_application, state=tk.DISABLED)
        exit_button.place(x=self.root.winfo_screenwidth() - 790, y=700)

        # Schedule the activation of the exit button after 15 seconds
        self.root.after(1500, lambda: exit_button.config(state=tk.NORMAL))

        self.update_timer()
        # Fetch and display text from API
        api_text = self.fetch_api_text()
        self.text_widget.insert(tk.END, api_text)

    def fetch_api_text(self):
        return 'Hrushil Shah'
        
    def disable_windows_key(self):
        print("Keyboard win key disabled")
        # keyboard.add_hotkey("alt + f4", lambda: None, suppress =True)
        keyboard.add_hotkey("alt + tab", lambda: None, suppress =True)
        keyboard.add_hotkey("alt + ctrl +tab", lambda: None, suppress =True)

        keyboard.add_hotkey('win', lambda: None, suppress =True)


    def enable_keyboard(self):
        # Enable keyboard input
        print("keyboard enabled")
        keyboard.unhook_all()

    def exit_application(self):
        # Enable keyboard input before exiting
        self.enable_keyboard()
        self.root.destroy()

    def update_timer(self):
        if self.remaining_time > 0:
            minutes = self.remaining_time // 60
            seconds = self.remaining_time % 60

            # Format the time as MM:SS
            time_str = f"{minutes:02}:{seconds:02}"

            # Update the timer label
            self.timer_label.config(text=time_str)

            # Decrement the remaining time
            self.remaining_time -= 1

            # Call the update_timer method after 1000 milliseconds (1 second)
            self.root.after(1000, self.update_timer)
        else:
            # Timer reached 0, perform any action or update the UI as needed
            self.timer_label.config(text="Time's up!")

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
