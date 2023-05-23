import subprocess
import signal
import sys

def main():
    cmd1 = "python manage.py runserver 127.0.0.1:8000"
    cmd2 = "celery -A my_project worker -l INFO"

    process1 = subprocess.Popen(cmd1, shell=True)
    process2 = subprocess.Popen(cmd2, shell=True)

    try:
        # Wait for the processes to complete
        process1.wait()
        process2.wait()
    except KeyboardInterrupt:
        # Handle keyboard interrupt (Ctrl+C)
        print("Keyboard interrupt detected. Shutting down...")
        process1.terminate()
        process2.terminate()
        sys.exit(0)

if __name__ == '__main__':
    main()
