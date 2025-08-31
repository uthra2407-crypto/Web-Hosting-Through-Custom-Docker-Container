import multiprocessing
import time

def cpu_stress():
    while True:
        pass

if __name__ == "__main__":
    processes = []
    for _ in range(multiprocessing.cpu_count()):
        p = multiprocessing.Process(target=cpu_stress)
        p.start()
        processes.append(p)

    time.sleep(120)  # Run stress for 2 minutes
    for p in processes:
        p.terminate()
