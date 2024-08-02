import threading
#excutes mutiple tasks seperately 
#one thread per task
#run simultanelously and share data with each other

#thread must have action/function 



def function1():
    for i in range(10):
        print("THREE ")


def function2():
    for i in range(10):
        print("TWO ")

def function3():
    for i in range(10):
        print("ONE ")


#without thread their done linearly
t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2)
t3 = threading.Thread(target=function3)
    
t1.start()
t2.start()
t3.start()
#however threads can be used once so to reuse re define thread
#However, due to the nature of the Global Interpreter Lock (GIL) and the way the print function works, the output might not always clearly demonstrate concurrent execution.



#if you want to pause one till complete
t1 = threading.Thread(target=function1)
t1.start()
t1.join()
print("it works")
