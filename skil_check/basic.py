
def print_self_information():
    print("ITスペシャリスト")
    print("２年")
    print("s15009")

def print_how_many_years_to_80():
    age = 19
    set = 80
    answer = set - age
    print(answer)

def print_odd_or_even(target):
    if(target % 2 == 0):
        print("偶数")
    else:
        print("奇数")

def print_hoge():
    from random import randint
    while(True):
        num = randint(0,50)
        if(num == 25):
            print("hoge")
            break
        else:
            print(num)

def print_even_from_100_to_1000():
    for x in range(100,1000):
        if(x % 2 == 0):
            print(x)
        else:
            pass

if __name__ == '__main__':

    print_self_information()
    print_how_many_years_to_80()
    print_odd_or_even(13)
    print_odd_or_even(10)
    print_hoge()
    print_even_from_100_to_1000()
