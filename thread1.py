import threading
# from threading import *
# x=0
# l=threading.Lock()
# def increment():
#     global x
#     l.acquire()
#     for i in range(10000000):
#         x+=1
#         # print(x)
#     l.release()
       
# def main():
#     global x
#     x=0
#     t1=threading.Thread(target=increment)
#     t2=threading.Thread(target=increment)
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
  
# for i in range(10):
#     main()
#     print("iteration{0}:x={1}".format(i,x))


# from threading import *
# class Mythread(Thread):
#     def __init__(self,a):
#          super().__init__()
#          self.a=a
#     def cube(self):
#         for i in self.a:
#             print("cube",i*i*i)
#     def square(self):
#         for i in self.a:
#             print("square",i*i)
#     def run(self):
 
#         t1=Thread(target=self.cube)
#         t2=Thread(target=self.square)
#         t1.start()
#         t2.start()
# a=[1,2,3,4,5]       
# my=Mythread(a)     
# my.start()
# my.join()

####lock

from threading import *
class Mythread(Thread):
    def __init__(self,a,lock):
         super().__init__()
         self.a=a
         self.lock=lock
    def cube(self):
        self.lock.acquire()
        for i in self.a:
            print("cube",i*i*i)
        self.lock.release()
    def square(self):
        
        self.lock.acquire()
        for i in self.a:
            print("square",i*i)
        self.lock.release()
    def run(self):
 
        t1=Thread(target=self.cube)
        t2=Thread(target=self.square)
        t1.start()
        t2.start()
lock=Lock()
a=[1,2,3,4,5]       
my=Mythread(a,lock)     
my.start()
my.join()



# from threading import *
# class Mythread(Thread):
#     def _init_(self,a,lock):
#          super()._init_()
#          self.a=a
#          self.lock=lock
#     def cube(self):
       
#         for i in self.a:
#             print("cube",i*i*i)
        
#     def square(self):
 
#         for i in self.a:
#             print("square",i*i)
      
#     def run(self):
#         self.lock.acquire()
 
#         t1=Thread(target=self.cube)
#         t2=Thread(target=self.square)
#         t1.start()
#         t2.start()
#         self.lock.release()
# lock=Lock()
# a=[1,2,3,4,5]       
# my=Mythread(a,lock)     
# my.start()
# my.join()