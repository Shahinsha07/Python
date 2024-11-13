# import time
# def square(l):
#     square=[]
#     for i in l:
#         time.sleep(1)
#         c=i**2
#         square.append(c)
#         print("square of",i,"is",i**2)

# # def cube(l):
# #     # cube=[]
# #     for i in l:
# #         # time.sleep(1) #1 second delay
# #     #     d=i**3
# #     #     cube.append(d)

# #         print("cube of",i,"is",i**3)
# l=[1,2,3,4,5]

# t1=time.time()
# square(l)
# cube(l)
# print(time.time()-t1)

import threading
import time

def square(l):
    for i in l:
        time.sleep(1)
        print("square of", i, "is", i**2)
        print(threading.current_thread().getName())  # Correct thread name call

def cube(l):
    for i in l:
        time.sleep(1)
        print("cube of", i, "is", i**3)
        print(threading.current_thread().getName())  # Correct thread name call

l = [1, 2, 3, 4, 5]

t1 = time.time()

# Set thread names before starting
t2 = threading.Thread(target=square, args=(l,))
t3 = threading.Thread(target=cube, args=(l,))
t3.setName("first thread")
t2.setName("second thread")

# Start the threads
t2.start()
t3.start()

print("Active threads:", threading.active_count())

# Wait for the threads to finish
t2.join()
t3.join()

print("Active threads after join:", threading.active_count())
print("Time taken:", time.time() - t1)


# import threading
# import time

# def files(a,b):
#     f1=open(a,'r')
#     data=f1.read()
#     time.sleep(3)
#     ff=open(b,'w')
#     ff.write(data)
    
# a="source.txt"
# b="file1.txt"
# c="file2.txt"

# # files(a,b)
# # files(a,c)
# t1=threading.Thread(target=files,args=(a,b))
# t2=threading.Thread(target=files,args=(a,c))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("file process completed")

# from threading import *
# import threading
# import time
# l=Lock()   #not using import method we use l=threading.Lock()
# def file(a)
#     l.acquire()
#     f=open(a,"a")
#     f.write("hello \n")
#     # time.sleep(2)

#     f=open(a,"a")
#     f.write("hai\n")
#     l.release()

# a="source1.txt"
# # file(a)
# t1=threading.Thread(target=file,args=(a,))
# t2=threading.Thread(target=file,args=(a,))
# t3=threading.Thread(target=file,args=(a,))
# t4=threading.Thread(target=file,args=(a,))
# t5=threading.Thread(target=file,args=(a,))

# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()

# t1.join()
# t2.join()
# t3.join()
# t4.join()
# t5.join()
# print("completed")


# from threading import *
# class Mythread(Thread):
#     def cube(self,a):
#         for i in a:
#             print("cube",i**3)
#     def square(self,a):
#         for i in a:
#             print("square",i*i)
#     def run(self):
#         a=[1,2,3,4,5]
#         self.cube(a)
#         self.square(a)
# my=Mythread()
# my.start()

# import threading
# x=0
# def increment():
#     global x
#     for i in range(10):
#         x+=1
#         print(x)

# def main():
#     global x
#     t1=threading.Thread(target=increment)
#     t2=threading.Thread(target=increment)


#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()

# main()
# main()

