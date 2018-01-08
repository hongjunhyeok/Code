#단체의 주소록
#전체적인 관리 class
from ContactManager import Contact
from math import ceil #올렷따리
##이름을 반환해줌
##Contact인스턴스가 넘어온다.
def sort_by_name(contact):
    return contact.get_name()

_COUNT_PER_PAGE = 5

class ContactBook():

    def __init__(self):
         self.contact_list=[
            Contact('홍길동','010 -1111-2222','hong@naver.com'),
        Contact('둘리', '010 -2222-2222', 'duli@naver.com'),
        Contact('뽀', '010 -5555-5555', 'PPO@naver.com'),
        Contact('보라돌이', '010 -1234-1234', 'BoraDori@naver.com'),
             Contact('홍길동', '010 -1111-2222', 'hong@naver.com'),
             Contact('둘리', '010 -2222-2222', 'duli@naver.com'),
             Contact('뽀Z', '010 -5555-5555', 'PPO@naver.com'),
             Contact('보라d돌이', '010 -1234-1234', 'BoraDori@naver.com'),
             Contact('뚜d비', '010 -1111-2222', 'hong@naver.com'),
             Contact('나d나', '010 -2222-2222', 'duli@naver.com'),
             Contact('뽀Y', '010 -5555-5555', 'PPO@naver.com'),
             Contact('보라s돌이', '010 -1234-1234', 'BoraDori@naver.com'),
             Contact('둘리s', '010 -1111-2222', 'hong@naver.com'),
             Contact('나s나', '010 -2222-2222', 'duli@naver.com'),
             Contact('뽀X', '010 -5555-5555', 'PPO@naver.com'),
             Contact('보라a돌이', '010 -1234-1234', 'BoraDori@naver.com'),
        ]

        ## 무엇으로 정렬할 지 함수로 넘겨주어야 한다.
         self.contact_list.sort(key=sort_by_name)

        #추가

    #추가할 사용자
    def add(self):
        print('주소록을 입력하세요')
        name = input('이름을 작성하십시오')
        phone = input('전화번호를 작성하십시오')
        address = input('주소를 작성하십시오')
        email = input('email을 작성하십시오')
        birthday=input('생일을 작성하십시오')

        add_Contact=Contact(P_name=name,P_phone=phone,P_email=email,P_address=address,P_birthday=birthday)
        self.contact_list.append(add_Contact)


    def print(self):
        ## self.***  : print를 호출 했을때 속성으로 만듦
        self.page=1
        self.total_count =len(self.contact_list)
        self.total_page= int(ceil(self.total_count/_COUNT_PER_PAGE))

    def move_previous_page(self):
        if self.page> 1 :
            self.page -=1
        self.print_page()
    def move_next_page(self):
        if self.page < self.total_page:
            self.page +=1
        self.print_page()
    def move_page(self):
        if self.page <1 :
            self.page = 1
        elif self.page > self.total_page:
            self.page=self.total_page
        self.print_page()

        while True:
            select = input('> ')
            if select == 'p' or select =='P':
                self.move_previous_page()
            elif select == 'n' or select =='N':
                self.move_next_page()
            elif select == 'q' or select =='Q':
                return
            else : # 숫자입력인자
                if select.isnumeric():
                    page=int(select)
                    self.move_page()





    def print_page(self):
        start = (self.page-1)*_COUNT_PER_PAGE
        end =start + _COUNT_PER_PAGE
        print('=================================================')
        print(' No 이름     전화번호        email')
        print('=================================================')
        for ix,Contact in enumerate(self.contact_list[start:end]):
            print('%-5d'%(start+ix+1),end="")
            Contact.print()

        print('=================================================')
        print('[%d/%d], total : %d 명 '%(self.page,self.total_page,self.total_count))

    def search(self):
        name=input('이름을 입력하세요')
        name.strip()
        # 동명이인 없으면 가능하다.
        if not name:
            print('검색할 이름이 없습니다.')
            return

        for contact in self.contact_list:
            if name == contact.get_name():
                self.print_detail(contact)
                contact.print_detail()
                break # break 반복문 탈출
        else:
            print('주소록없음')



    def print_detail(self,contact):
        print('########################################################')
        contact.print_detail()
        print('########################################################')

    ##어떤 사용자를 수정할 것인지 > 있는지 없는지 > 있으면 기존정보 하나씩 보여주고 이름은 고정시키고 다 수정
    ##전화번호: 010-1111-2222 새전화번호 : 입력
    def update(self):
        name=input('수정할 이름을 입력하세요')
        name.strip()
        for contact in self.contact_list:
            if name == contact.get_name():
               break  # 찾았을 때 break이면 그당시의 contact만으로 검사
        else: # for문이 다 돌았을때 생기는 loop
                print('수정할 이름이 없습니다 다시 실행하세요')
                return

        print('전화번호 : 01077371421')
        new_phone = input ('새전화번호 :').strip()
        if new_phone :
            contact.set_phone(new_phone)

        print('email :',contact.get_email())
        new_email = input('새 이메일 :').strip()
        if new_email :
            contact.set_email(new_email)

        print('address : ' ,contact.get_address())
        new_address = input('새 주소 :').strip()
        if new_address :
            contact.set_address(new_address)

        print('birthday : ',contact.get_birthday())
        new_birthday = input('새 생일 :').strip()
        if new_birthday :
            contact.set_birthday(new_birthday)

    ## pop에의해 참조가 사라졌지만 메모리 상에 데이터는 남아있기 때문에 쓰레기가된다.
    def delete(self):
        name=input('삭제할 이름을 입력하세요')
        index=-1
        for ix,contact in enumerate(self.contact_list):
            if name == contact.get_name():
                index=ix ##인덱스 발견
                break

                #-1 이 아니면 참이다
        if index != -1:
            self.contact_list.pop(index)
            print('%s 주소록 삭제'%name)
        else:
                print('%s 주소록에 없음'%name)


    def __iter__(self):
        self.current = 0 # 본래 currnet를 init에서 초기화했다 for에 in이 들어갈때마다 current가 0으로 초기화.
        return self

    def __next__(self):
        total = len(self.contact_list)
        if self.current<total:
            current = self.current
            self.current +=1
            return self.contact_list[current]
        else:
            raise StopIteration
