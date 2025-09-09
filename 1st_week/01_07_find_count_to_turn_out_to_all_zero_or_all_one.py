input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # 이 부분을 채워보세요!
    count_to_all_zero = 0
    count_to_all_one = 0

    for i in range(len(string) - 1):
        print(i)
        if string[i] != string[i + 1]:
            if string[i +1] == "1":
                count_to_all_zero += 1
            if string[i +1] == "0":
                count_to_all_one += 1

    return min(count_to_all_zero, count_to_all_one)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)