import time
import threading

def longIO():
    print("begin long IO")
    time.sleep(5)
    print("finish long IO")
    yield "longIO finished"


# callback func
def finish(data):
    print("begin callback")
    print(data)
    print("finish callback")

def genCoroutine(func):
    def wrapper(*args, **kwargs):
        gen1 = func()  # reqA generator
        gen2 = next(gen1)  # longIO generator
        def run(g):
            """hang gen2"""
            res = next(g)
            try:
                gen1.send(res)  # return reqA data
            except StopIteration as e:
                pass
        threading.Thread(target=run, args=(gen2, )).start()
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