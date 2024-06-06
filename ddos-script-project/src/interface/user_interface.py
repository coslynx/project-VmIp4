import tkinter as tk

class UserInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("DDoS Script Interface")
        self.root.geometry("400x300")

        self.target_label = tk.Label(self.root, text="Target IP address or domain:")
        self.target_label.pack()

        self.target_entry = tk.Entry(self.root)
        self.target_entry.pack()

        self.attack_type_label = tk.Label(self.root, text="Choose DDoS attack type:")
        self.attack_type_label.pack()

        self.attack_type_var = tk.StringVar()
        self.attack_type_var.set("UDP Flood") # Default attack type
        self.attack_type_options = ["UDP Flood", "SYN Flood"]
        self.attack_type_dropdown = tk.OptionMenu(self.root, self.attack_type_var, *self.attack_type_options)
        self.attack_type_dropdown.pack()

        self.duration_label = tk.Label(self.root, text="Enter attack duration (in seconds):")
        self.duration_label.pack()

        self.duration_entry = tk.Entry(self.root)
        self.duration_entry.pack()

        self.intensity_label = tk.Label(self.root, text="Enter attack intensity:")
        self.intensity_label.pack()

        self.intensity_entry = tk.Entry(self.root)
        self.intensity_entry.pack()

        self.start_button = tk.Button(self.root, text="Start Attack", command=self.start_attack)
        self.start_button.pack()

    def start_attack(self):
        target = self.target_entry.get()
        attack_type = self.attack_type_var.get()
        duration = int(self.duration_entry.get())
        intensity = int(self.intensity_entry.get())

        # Logic to start the DDoS attack with the specified parameters
        # This is where the integration with other modules and APIs would occur

        print(f"Starting {attack_type} attack on {target} for {duration} seconds with intensity {intensity}.")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    ui = UserInterface()
    ui.run()