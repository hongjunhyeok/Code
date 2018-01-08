
import time

class PerformanceDecorator:
    def __init__(self,f):

        self.func=f
    def __call__(self):
        start_time=time.time()
        # print(start_time)
        self.func()
        print("-------%s seconds------"%(time.time()-start_time))
class NotificationDecorator:
    def __init__(self,f):

        self.func=f
    def __call__(self):

        # print(start_time)

        print('~~~~~~~~~~~~~~~~~~~~')
        print("오늘은 조기퇴근합니다")
        print('~~~~~~~~~~~~~~~~~~~~')
        self.func()
# class MyDecorator:
#     def __init__(self,f):
#         print("초기화중:)!!!!
#         self.func = f
#     def __call__(self):
#         print("Begin :{0}".format(self.func.__name__))
#         self.func()


#안쪽에서부터 실행됨
#덮어쓰면서 class가 생성됨
# @PerformanceDecorator
# @MyDecorator
# def print_hello():
#     print("hello")
# print_hello()