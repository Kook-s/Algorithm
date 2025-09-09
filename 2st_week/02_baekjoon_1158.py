# BOJ 1158
# 1부터 N번까지 N명의 사람이 원을 이루면서 않아있다.
# 양의 정수 K <= N 이 주어진다.
# 이제 순서대로 K번째 사람을 제거한다.
# 한사람이 제거되면 남은 사람들로 이우어진 원을 따라 이 과정을 계속해 나간다.
# 이 과정은 N명의 사람이 모두 제거 될때 까지 계속 된다.
# 원에서 사람들이 제거되는 순서를 N, K 요세푸스 순열이라 한다.

def josephus_problem(n, k):
   # 이 부분을 채워보세요!
    result_arr = []

    next_index = k - 1
    people_arr = list(range(1, n + 1))

    while people_arr:
        result =  people_arr.pop(next_index)
        result_arr.append(result)

        if len(people_arr) != 0:
            next_index = (next_index + (k-1)) % len(people_arr)

    print("<", ", ".join(map(str, result_arr)), ">", sep='')


n, k = map(int, input().split())
josephus_problem(n, k)