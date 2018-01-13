def sort_dictionary(dic):
    #'''입력받은 dic의 각 키와 값을 튜플로 만든 다음, 키 값을 기준으로 정렬해서 리스트에 넣으세요. 그 리스트를 return하면 됩니다.'''

    ## sorted 함수 ( 정렬할 내용 , key = 정렬방법 )
    ## lambda (변수) : 함수의 내용  // 함수를 따로 정의내리지 않아도 된다. 자바는 8.0부터 사용 가능
    ## items함수는 딕셔너리의 key와 value를 튜플 형태의 pair로 된 리스트를 리턴한다.
    return sorted(dic.items(),key= lambda x: x[0])

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sort_dictionary({"김철수": 78, "이하나": 97, "정진원": 88}))