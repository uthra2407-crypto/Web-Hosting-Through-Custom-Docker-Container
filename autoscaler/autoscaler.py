# import os
# import time
# import psutil
# import subprocess
# from datetime import datetime

# # Configuration
# MAX_CONTAINERS = 4
# MIN_CONTAINERS = 1
# CPU_THRESHOLD_HIGH = 60.0  # in %
# CPU_THRESHOLD_LOW = 20.0
# SCALE_COOLDOWN = 30  # in seconds
# DOCKER_SERVICE_NAME = "backend"
# LOG_FILE = "scaling_log.txt"

# def count_backend_containers():
#     try:
#         result = subprocess.check_output(
#             f"docker ps --filter 'name={DOCKER_SERVICE_NAME}' --format '{{{{.ID}}}}'",
#             shell=True
#         )
#         return len(result.decode().strip().split('\n')) if result.strip() else 0
#     except subprocess.CalledProcessError:
#         return 0

# def scale_up():
#     current = count_backend_containers()
#     if current < MAX_CONTAINERS:
#         new_count = current + 1
#         subprocess.call(f"docker-compose up -d --scale {DOCKER_SERVICE_NAME}={new_count}", shell=True)
#         log_event(f"[+] Scaled up: {new_count} {DOCKER_SERVICE_NAME} containers")

# def scale_down():
#     current = count_backend_containers()
#     if current > MIN_CONTAINERS:
#         new_count = current - 1
#         subprocess.call(f"docker-compose up -d --scale {DOCKER_SERVICE_NAME}={new_count}", shell=True)
#         log_event(f"[-] Scaled down: {new_count} {DOCKER_SERVICE_NAME} containers")

# def log_event(message):
#     with open(LOG_FILE, "a") as f:
#         f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")
#     print(message)

# # Main loop
# if __name__ == "__main__":
#     print("🔁 Starting auto-scaler...")
#     log_event("Auto-scaler started.")
    
#     while True:
#         cpu = psutil.cpu_percent(interval=3)
#         print(f"⚙️  CPU Usage: {cpu}%")

#         if cpu > CPU_THRESHOLD_HIGH:
#             scale_up()
#         elif cpu < CPU_THRESHOLD_LOW:
#             scale_down()

#         time.sleep(SCALE_COOLDOWN)
############### import psutil
# import time
# from datetime import datetime

# log_file = "../monitoring/scaling_log.txt"
# cpu_check_interval = 10  # in seconds

# def log_event(message):
#     timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     log_line = f"[INFO] {timestamp} - {message}\n"
#     with open(log_file, "a") as f:
#         f.write(log_line)
#     print(log_line.strip())

# def monitor():
#     log_event("Autoscaler initialized")
#     log_event("Monitoring started")
    
#     instance_running = True

#     while True:
#         cpu = psutil.cpu_percent(interval=1)

#         log_event(f"CPU usage: {cpu}%")
        
#         if cpu > 80:
#             log_event("CPU usage: {}% — scaling up".format(cpu))
#             log_event("New instance created")
#             instance_running = True
        
#         elif cpu < 30 and instance_running:
#             log_event("CPU usage: {}% — scaling down".format(cpu))
#             log_event("Instance terminated")
#             instance_running = False
        
#         time.sleep(cpu_check_interval)
# from datetime import datetime

# def log_event(message):
#     with open("scaling_log.txt", "a") as f:
#         f.write(f"[INFO] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")


# if __name__ == "__main__":
#     monitor()

import os
import time
import psutil
import subprocess
from datetime import datetime

# === Configuration ===
MAX_CONTAINERS = 4
MIN_CONTAINERS = 1
CPU_THRESHOLD_HIGH = 60.0
CPU_THRESHOLD_LOW = 25.0
SCALE_COOLDOWN = 30  # seconds
DOCKER_SERVICE_NAME = "backend"
LOG_FILE = os.path.join(os.path.dirname(__file__), "scaling_log.txt")


def log_event(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_line = f"[INFO] {timestamp} - {message}"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_line + "\n")
    print(log_line)

def count_backend_containers():
    try:
        result = subprocess.check_output(
            f"docker ps --filter name={DOCKER_SERVICE_NAME} --format '{{{{.ID}}}}'",
            shell=True
        )
        return len(result.decode().strip().split('\n')) if result.strip() else 0
    except subprocess.CalledProcessError:
        return 0

def scale_up():
    current = count_backend_containers()
    if current < MAX_CONTAINERS:
        new_count = current + 1
        subprocess.call(f"docker-compose up -d --scale {DOCKER_SERVICE_NAME}={new_count}", shell=True)
        log_event(f"[+] Scaled UP: Running {new_count} '{DOCKER_SERVICE_NAME}' containers.")
    else:
        log_event("🚫 Max containers reached. Cannot scale up.")

def scale_down():
    current = count_backend_containers()
    if current > MIN_CONTAINERS:
        new_count = current - 1
        subprocess.call(f"docker-compose up -d --scale {DOCKER_SERVICE_NAME}={new_count}", shell=True)
        log_event(f"[-] Scaled DOWN: Running {new_count} '{DOCKER_SERVICE_NAME}' containers.")
    else:
        log_event("🚫 Min containers reached. Cannot scale down.")

# === Main Monitor Loop ===
if __name__ == "__main__":
    log_event("🚀 Auto-Scaler Started")
    
    while True:
        cpu = psutil.cpu_percent(interval=3)
        log_event(f"CPU usage: {cpu}%")

        if cpu > CPU_THRESHOLD_HIGH:
            log_event("🔥 High CPU detected - Triggering scale UP")
            scale_up()

        elif cpu < CPU_THRESHOLD_LOW:
            log_event("❄️  Low CPU detected - Triggering scale DOWN")
            scale_down()

        time.sleep(SCALE_COOLDOWN)

