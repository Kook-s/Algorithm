input = 20


def find_prime_list_under_number(number):
    # 이 부분을 채워보세요!
    prime_list = []

    for n in range(2, number + 1):
        for i in prime_list:
            if i * i <= n and  n % i == 0:
                break
        else:
            prime_list.append(n)

    return prime_list


result = find_prime_list_under_number(input)
print(result)