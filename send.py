from abc import ABCMeta
from abc import abstractmethod


class Sender(metaclass=ABCMeta):
    def __init__(self,to=''):
        self.to=to

        @abstractmethod
        def send(self,msg):
            pass
        def set_to(self,to):
            self.to= to


        ## 탬플릿 : 기본양식이 정해져있고 바꿀거만 바꿔라
        ##처리절차는 정해져있으나 어떻게 처리할지는 안정해져있다.
        def send_to(self,to,msg):
            self.to=to
            self.send(msg)


class Fax(Sender):
    def __init__(self,to):
        to=0
    def send(self,msg):
        print('=================')
        print('팩스번호 :',self.to)
        print('=================')
        print('내용 : '+msg)
        print('=================')

class SMS(Sender):
    def __init__(self, to):
        pass
    def send(self, msg):
            print('=================')
            print('전화번호 :', self.to)
            print('=================')
            print('내용 : ' + msg)
class Email(Sender):
    def __init__(self, to):
        to=""

    def send(self, msg):
        print('=================')
        print('이메일:', self.to)
        print('=================')
        print('내용 : ' + msg)


def send(s):
    msg = input('내용')
    s.send(msg)
    print('전송했습니다.')



if __name__=='__main__':
    to=input('수신자 번호를 입력하세요')
    fax=Fax(to)
    send(fax)

    email=Email()
    Email.send()
    email.send_to('hong@naver.com','Hello Hong')
