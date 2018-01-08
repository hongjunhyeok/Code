##각 개인에 대한 주소록
##기본 단위
import Deco
class Contact:
    ## 초기화 하는 메소드
    ## 필수로 하는 정보와 옵션으로 하는 정보를 나눔
    def __init__(self,P_name,P_phone,P_email="",P_address="",P_birthday=""):
        self.__name = P_name
        self.__phone = P_phone
        self.__email = P_email
        self.__address = P_address
        self.__birthday = P_birthday
    def print(self):
        print('%-5s %-15s %-20s' % (self.__name, self.__phone, self.__email))
    def print_detail(self):
        print('이름 : ', self.__name)
        print('번호 : ', self.__phone)
        print("이메일 : ", self.__email)
        print('주소 : ', self.__address)
        print('생일: ', self.__birthday)


    ## 유지보수에 좋다 코드가 길어지는대신
    ## set ==  설정 ,get == read
    def set_email(self,email):
        self.__email = email
    def set_address(self,address) :
        self.__address = address

    def set_birthday(self,birthday):
        self.__birthday=birthday
    def set_phone(self,phone):
        self.__phone = phone



    def get_name(self):

        return self.__name
    def get_email(self):
        return self.__email
    def get_address(self) :
        return self.__address
    def get_birthday(self):
        return self.__birthday
    def get_phone(self):
        return self.__phone

    def __str__(self) -> str:

        #문자열로 리턴하는 리턴값을 재정의하고자 함
        # 보통  (변수 : 값) (변수 : 값) 으로 1대1 대응하면서 리턴이 된다
        return 'name : %s,email : %s,phone : %s, address=%s,birthday=%s' %(self.__name, self.__email,
                                                                           self.__phone, self.__address, self.__birthday)
        #return super().__str__()

#str1 > self로 넘어감 str2 > 매개변수로 넘어감
#if str1 == str2:
#isinstance type 검사 o가 Contact의 인스턴스인가?
    def __eq__(self, o):
        if not isinstance(o,Contact):
            return False

        if self.__email == o.__email:
            return True
        else:
            return False


        # return super().__eq__(o)

    def __ne__(self, o: object) -> bool:
        if not isinstance(o,Contact):
            return True

        if self.__email == o.__email:
            return False
        else:
            return True




