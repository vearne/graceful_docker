import signal
import time

is_running = True

def sig_handler(num, stack):
    global is_running
    is_running = False

def main():
    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)
    signal.siginterrupt(signal.SIGINT, False)
    signal.siginterrupt(signal.SIGTERM, False)

    while is_running:
        time.sleep(3)

    print "prepare exit"
    print "sleep 10"
    time.sleep(10)
    print "exit"
    

if __name__ == "__main__":
    main()
