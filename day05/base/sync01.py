import time

def longIO():
    print("begin long IO")
    time.sleep(5)
    print("finish long IO")

def reqA():
    print("begin reqA")
    longIO()
    print("finish reqA")

def reqB():
    print("begin reqB")
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