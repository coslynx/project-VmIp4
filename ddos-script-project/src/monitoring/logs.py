import datetime

class Logs:
    def __init__(self):
        self.log_file = "ddos_logs.txt"

    def log_attack_details(self, target, attack_type, duration, intensity):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{current_time} - Target: {target}, Attack Type: {attack_type}, Duration: {duration}, Intensity: {intensity}\n"

        with open(self.log_file, "a") as file:
            file.write(log_entry)

    def log_attack_results(self, target, success):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = "Successful" if success else "Unsuccessful"
        log_entry = f"{current_time} - Target: {target}, Result: {result}\n"

        with open(self.log_file, "a") as file:
            file.write(log_entry)