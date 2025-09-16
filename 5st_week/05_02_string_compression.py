input = "abcabcabcabcdededededede"

# 모든 경우에서 가장 압축을 많이 시킨 문자열의 길이를 반환해야 한다.
# 문자열의 길이를 n 이라고 한다면
# 1부터 n개까지 길이로 쪼갤 수 있다는 걸 의미한다.

# 1 ~ n//2


def string_compression(string):
    # 문자열의 길이를 구한다.
    n = len(string)
    # 결과값 초기화
    result = n

    for split_size in range(1, n // 2 + 1): # 문자열의 n/2 의 이상 넘어가도 반복되는게 없기 때문에 n/2의 범위 까지만, range는 0~n-1 이기 때문에 +1
        splited = [
            string[i:i + split_size] for i in range(0, n, split_size)
            # 0~n 까지 반복하는데 슬라이싱하기 때문에 1,2,3 순차적으로 늘어나야 된다.
            # split_size = 1,2,3,4.... (0, n, 1), (0, n, 2), (0, n, 3)...[0:1],[0:2],[0:3], a,b, ab,cd, adbc,....
        ]

        compressed = "" #압축한 문자열
        count = 1 # 압축된 횟수

        for i in range(0, len(splited) - 1 ): # 압축된 배열의 길이를 꺼내 비교
            cur, next =  splited[i], splited[i + 1] # 앞뒤 압축 문자를 비교해

            if cur == next: # 같다면 횟수를 증가 시킨다.
                count += 1
            else:
                if count == 1: # 앞뒤 문자가 다른데 횟수가 1이라면 압축된 것이 아니기 때문에 압축 문자에 추가
                    compressed += cur
                else: #앞뒤 문자가 같지 않는게 횟수가 1이 아니라면 이전에 압축된 문자가 있단는 것
                    compressed += f"{count}{cur}" # 압축 문자에 추가
                count = 1 # 다시 초기화

        if count == 1: # 마지막 압축문자는 cur가 될수없다 그래서 추가되지 못하고 끝나는데 반복을 다 했을 경우 마지막 문자를 추가한다.
            compressed += splited[-1]
        else: # 압축 문자가 마지막까지 이어진다면 추가되지 못하고 끝나는데 그럴 경우 추가 해준다.
            compressed += f"{count}{splited[-1]}"

        result = min(len(compressed), result)

    return result

print(string_compression(input))  # 14 가 출력되어야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", string_compression("JAAA"))
print("정답 = 9 / 현재 풀이 값 = ", string_compression("AZAAAZDWAAA"))
print("정답 = 12 / 현재 풀이 값 = ", string_compression('BBAABAAADABBBD'))