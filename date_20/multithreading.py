import time
import threading
def cal_sqaure(numbers):
    print("Calculate square numbers")
    for n in numbers:
        time.sleep(0.2)
        print('square',n*n)
def cal_cube(numbers):
    print("Calculate cube numbers")
    for n in numbers:
        time.sleep(0.2)
        print('cube',n*n*n)

arr=[2,3,4,5]
t=time.time()
t1=threading.Thread(target=cal_sqaure,args=(arr,))
t2=threading.Thread(target=cal_cube,args=(arr,))
t1.start()
t2.start()

t1.join()
t2.join()
print("done",time.time()-t)
