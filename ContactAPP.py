from Deco import PerformanceDecorator,NotificationDecorator
from ContactBook import ContactBook
contact_book = ContactBook()



for contact in contact_book:## for 에서 리스트를 달라 그리고 __next__로 넘겨달라## 컨택리스트의 아이템을 받아서 컨택에 넘겨줘야해
    print(contact)



def print_menu():
    print('출력(P) | 추가(A) | 검색(S) | 수정(U) | 삭제(D) | 종료(X)')

def select_menu():
    select = input('메뉴를 선택하세요 -->')
    return select.upper()

## 인스턴스 생성 비어있는 리스트로 초기화

##전역함수
##프로그램이 종료될때 종료
book_Instance = ContactBook()



@PerformanceDecorator

@NotificationDecorator
def main():
    while True:
        print_menu()
        command = select_menu()


        if(command == 'P'):
            book_Instance.print()
        elif(command == 'A'):

            book_Instance.add()

        elif(command == 'S'):

            book_Instance.search()
        elif(command == 'U'):
            book_Instance.update()

        elif(command == 'D'):
            book_Instance.delete()

        elif(command == 'X'):
            return

if __name__ == '__main__':
    main()
