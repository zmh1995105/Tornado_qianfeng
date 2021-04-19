import time
import threading

gen = None

def longIO():
    def run():
        print("begin long IO")
        time.sleep(5)
        try:
            global gen
            gen.send("longIO finished")
        except StopIteration as e:
            pass
        print("finish long IO")
        # return "longIO finished"
    threading.Thread(target=run).start()

# callback func
def finish(data):
    print("begin callback")
    print(data)
    print("finish callback")

def genCoroutine(func):
    def wrapper(*args, **kwargs):
        global gen
        gen = func(*args, **kwargs)
        next(gen)
    return wrapper

@genCoroutine
def reqA():
    print("begin reqA")
    res = yield longIO()
    print("get longIO data: ", res)
    print("finish reqA")

def reqB():

    print("begin reqB")
    time.sleep(2)
    print("finish reqB")

# tornado service
def main():
    # global gen
    # gen = reqA()
    # next(gen)
    reqA()
    reqB()
    while 1:
        time.sleep(0.1)
        pass

if __name__ == '__main__':
    main()