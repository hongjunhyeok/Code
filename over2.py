
from ContactManager import Contact


hong= Contact('홍','010','hong@naver.com')
hong2= Contact('홍','010','hong@naver.com')
hong3=hong
hong4= Contact('홍4','010','hong@naver.com')
go= Contact('고','011','gdgd@naver.com')

## 물리적 동등성
if hong == go:
    print('hong과 go는 동일한 인스턴스입니다.')
else:
    print('hong과 go는 다른 인스턴스입니다.')

if hong == hong2:
    print('hong과 hong2는 동일한 인스턴스입니다.')
else:
    print('hong과 hong2는 다른 인스턴스입니다.')

if hong == hong3:
    print('hong과 hong3는 동일한 인스턴스입니다.')
else:
    print('hong과 hong3는 다른 인스턴스입니다.')


#왜틀렸는지 설명할 수 있을까?
if hong=='hong':
    print('hong과 "hong"는 동일한 인스턴스입니다.')
else:
    print('hong과 "hong"는 다른 인스턴스입니다.')
