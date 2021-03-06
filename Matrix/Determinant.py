import copy
import Matrix as M
# 리스트를 복사할때 내장된 list(), copy()를 이용하면 어인일인지 원본도 훼손된다.
# 따라서 반드시 copy모듈을 이용해 깊은 복사를 해주어야 한다.

def Determinant(n, mat):
    mat_copy = copy.deepcopy(mat)
    value = []
    mat_tmp = []
    if n>=3:
        for i in range(n):
            mat_tmp.clear()
            mat_tmp = copy.deepcopy(mat_copy)
            tmp = int(mat_tmp[0][i])
            # 행 삭제
            del mat_tmp[0]
            # 열 삭제 
            for j in range(0, n-1):
                del mat_tmp[j][i]
            if i%2 == 0: # 짝순열
                value.append((tmp*Determinant(n-1, mat_tmp)))
            else:        # 홀순열
                value.append(((-1)*tmp*Determinant(n-1, mat_tmp)))
    else:
        return int(int(mat_copy[0][0])*int(mat_copy[1][1])-int(mat_copy[0][1])*int(mat_copy[1][0]))
    D = sum(value, 0)
    return D

try:
    num = int(input())
    MAT = M.Matrix(num)
    print(MAT)
    D = Determinant(num, MAT)
finally:
    print(D)
