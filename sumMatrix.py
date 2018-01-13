## answer에 [ [ ] , [ ] ] 꼴로 만들어야 하니까 answer에 작업
## 이중for문으로 2차원배열

def sumMatrix(A, B):

    answer = [[] for j in range(len(A))]
    for i in range(len(A)):
        for x in range(len(A[i])):
            answer[i].append(A[i][x] + B[i][x])

    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumMatrix([[1, 2], [2, 3]], [[3, 4], [5, 6]]))