from collections import deque

c = 11
b = 2


def catch_me(cony_loc, brown_loc):
    # 구현해보세요!
    time = 0
    queue = deque()
    queue.append((brown_loc,0)) # 브라운의 위치와 시간

    visited = [{} for _ in range(200001)]

    while cony_loc <= 200000:
        cony_loc += time # 브라운은 시간데로 위치변경

        if time in visited[cony_loc]: #해당 위치에 시간이 있다면 게임 종료
            return time

        for i  in range(0, len(queue)):
            current_position, current_item = queue.popleft()

            new_time = current_item + 1

            new_position = current_position - 1
            if 0 <= new_position <= 200000:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position + 1
            if 0 <= new_position <= 200000:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position * 2
            if 0 <= new_position <= 200000:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

        time += 1

    return


print(catch_me(c, b))  # 5가 나와야 합니다!


print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))
# 1. 코니는 처음 위치 C에서 1초 후 1만큼 움직임
# 2. 이후 가속이 붙어 매 초 마다 이전 이동 거리 + 1 만큼 움직인다.
# 3. 즉 시간에 따라 코니의 위치는 C, C + 1, C + 3, C + 6
# 4. 브라운은 현재 위치 B에서 다음 순간 B -1 , B + 1, 2 *B 중 하나로 움직일 수 있다.
# 5. 코니와 브라운의 위치 p는 조건 0 <= x <= 200,000을 만족한다.
# 6. 브라운은 범위를 벗어나는 위치로 이동할 수 없고, 코니가 범위를 벗어나면 게임이 끝난다.

# 브라운이 코니를 잡는다. 잡는 최소 시간을 구하라
# 위치가 같으면 게임 종료
#

# T0   1    2    3    4
# 11 , 12 , 14 , 17 , 21



