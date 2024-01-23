import pytest

def find_prime(num):
    prime_list = []
    for n in range(num):
        if n > 2:
            flag = True
            for i in range(2, n):
                if (n % i) == 0 and i != n:
                    flag = False
            if flag:
                prime_list.append(n)

    return prime_list

def sort_list(list_num):
    return sorted(list_num)


