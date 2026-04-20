import os
import shutil

def get_disk_usage():
    total, used, free = shutil.disk_usage("/")
    print("Disk Total:", total // (2**30), "GB")
    print("Disk Used:", used // (2**30), "GB")
    print("Disk Free:", free // (2**30), "GB")

def get_cpu_usage():
    load = os.getloadavg()
    print("CPU Load (1, 5, 15 mins):", load)

def main():
    print(" System Health Check Running...\n")

    print(" CPU Info:")
    get_cpu_usage()
    
    print("\n Disk Info:")
    get_disk_usage()

    print("\n System Check Completed!")

if __name__ == "__main__":
    main()