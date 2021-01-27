"""입력
첫째 줄에는 테스트케이스의 개수 T가 주어진다. 각 테스트 케이스는 다음과 같이 주어진다.
첫째 줄에 건물의 개수 N 과 건물간의 건설순서규칙의 총 개수 K이 주어진다. (건물의 번호는 1번부터 N번까지 존재한다)
둘째 줄에는 각 건물당 건설에 걸리는 시간 D가 공백을 사이로 주어진다.
셋째 줄부터 K+2줄까지 건설순서 X Y가 주어진다. (이는 건물 X를 지은 다음에 건물 Y를 짓는 것이 가능하다는 의미이다)
"""

"""출력
건물 W를 건설완료 하는데 드는 최소 시간을 출력한다. 편의상 건물을 짓는 명령을 내리는 데는 시간이 소요되지 않는다고 가정한다.
건설순서는 모든 건물이 건설 가능하도록 주어진다.
"""

"""제한
2 ≤ N ≤ 1000
1 ≤ K ≤ 100,000
1 ≤ X, Y, W ≤ N
0 ≤ D ≤ 100,000, D는 정수
"""

"""testInput
2
4 4
10 1 100 10
1 2
1 3
2 4
3 4
4
8 8
10 20 1 5 8 7 1 43
1 2
1 3
2 4
2 5
3 6
5 7
6 7
7 8
7
"""

"""testOutput
120
39
"""
def minTime():
    N, K = input().split()
    N = int(N)
    K = int(K)
    D = list(map(int, input().split()))
    X = []
    Y = []
    buildingTime = D

    for i in range(K):
        tmp1, tmp2 = input().split()
        X.append(int(tmp1))
        Y.append(int(tmp2))
    for i in range(N):
        buildingTime.append(int(0))
    a = int(input())

    for i in range(N):
        buildingTime[i] = buildingTimeCalc(i, X, Y ,K, buildingTime)

    print("answer::",buildingTime[a])

def buildingTimeCalc(N, X, Y, K, buildingTime):
    maxTime = -1
    for i in range(K):
        if Y[i] == N+1:
            if buildingTime[X[i]] > maxTime:
                maxTime = buildingTime[X[i]]
    return buildingTime[N] + maxTime


#Main
T = int(input())

for i in range(T):
    minTime()
