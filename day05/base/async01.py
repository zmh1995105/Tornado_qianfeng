import time
import threading

def longIO(callback):
    def run(cb):
        print("begin long IO")
        time.sleep(5)
        print("finish long IO")
        cb("longIO finished")
        # return "longIO finished"
    threading.Thread(target=run, args=(callback, )).start()

# callback func
def finish(data):
    print("begin callback")
    print(data)
    print("finish callback")

def reqA():
    print("begin reqA")
    longIO(finish)
    print("finish reqA")

def reqB():
    print("begin reqB")
    time.sleep(2)
    print("finish reqB")

# tornado service
def main():
    reqA()
    reqB()
    while 1:
        time.sleep(0.1)
        pass

if __name__ == '__main__':
    main()