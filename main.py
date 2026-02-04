import psutil
import time
import winsound
import os
from datetime import datetime
from colorama import init, Fore

init(autoreset=True)

class ShellResourceMonitor:
    def __init__(self, cpu_limit=80, mem_limit=75, disk_limit=85, log_file="alert.log"):
        self.cpu_limit = cpu_limit
        self.mem_limit = mem_limit
        self.disk_limit = disk_limit
        self.log_file = log_file
        self.cpu_history = []

    def clear_shell(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def log_alert(self, message):
        with open(self.log_file, "a") as f:
            f.write(f"{datetime.now()} - {message}\n")

    def play_sound(self):
        winsound.Beep(1000, 500)

    def get_usage(self):
        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent
        return cpu, mem, disk

    def avg_cpu(self, cpu):
        self.cpu_history.append(cpu)
        if len(self.cpu_history) > 5:
            self.cpu_history.pop(0)
        return sum(self.cpu_history) / len(self.cpu_history)

    def print_bar(self, label, percent):
        bar_length = 30
        filled = int(bar_length * percent / 100)
        bar = '█' * filled + '-' * (bar_length - filled)

        if percent >= 80:
            color = Fore.RED
        elif percent >= 60:
            color = Fore.YELLOW
        else:
            color = Fore.GREEN

        print(f"{label:10}: |{color}{bar}{Fore.RESET}| {percent:.1f}%")

    def monitor(self):
        try:
            while True:
                self.clear_shell()

                cpu, mem, disk = self.get_usage()
                avg_cpu = self.avg_cpu(cpu)

                alert = False

                print(Fore.CYAN + "===== Shell Resource Monitoring & Alert System =====\n")

                self.print_bar("CPU(avg)", avg_cpu)
                self.print_bar("Memory", mem)
                self.print_bar("Disk", disk)

                print("\nStatus:")

                if avg_cpu > self.cpu_limit:
                    print(Fore.RED + "⚠ High CPU pressure detected")
                    self.log_alert(f"High CPU usage: {avg_cpu:.1f}%")
                    alert = True

                if mem > self.mem_limit:
                    print(Fore.RED + "⚠ High Memory pressure detected")
                    self.log_alert(f"High Memory usage: {mem:.1f}%")
                    alert = True

                if disk > self.disk_limit:
                    print(Fore.RED + "⚠ Disk space critical")
                    self.log_alert(f"High Disk usage: {disk:.1f}%")
                    alert = True

                if alert:
                    self.play_sound()
                else:
                    print(Fore.GREEN + "✓ System running normally")

                print("\nPress Ctrl+C to exit")
                time.sleep(2)

        except KeyboardInterrupt:
            print("\nMonitoring stopped.")
            self.log_alert("Monitoring stopped by user")

if __name__ == "__main__":
    monitor = ShellResourceMonitor(cpu_limit=80, mem_limit=75, disk_limit=85)
    monitor.monitor()
    
