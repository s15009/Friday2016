# 与えられた２つのパラメータの合計を２倍したものが６０を超えているかどうか
def check_sum_2times_over_60(par1, par2):
    twomultiple = (par1 + par2) * 2
    judge = True if twomultiple >= 60 else False
    return judge


# 与えられた金額に消費税率８％を含めた値が５０００を超えているかどうか
def tax_include(cost):
    tax = 1.08
    price = cost * tax
    judge = True if price > 5000 else False
    return judge
# 与えられたスコアが８０以上なら’A'、６０以上８０未満なら’B',４５以上６０未満’C'、
# ４５未満は’F'と返す
def judge_rank(score):
    if score >= 80:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 45:
        return "C"
    else:
        return "F"

# 与えられた数値の階乗を返す。　ただし再帰は使用禁止
def factorial(num):
    if num > 1:
        for x in range(1,num):
            num *= x
        return num
    else:
        return 1

# 与えられた数値の２の累乗を返す。　再帰禁止　便利な演算子ダメ
def power_of_two(num):
    two = 2
    if num == 0:
        return 1
    else:
        while (1 < num):
            two *= 2
            num -= 1
        return two


if __name__ == '__main__':
    check_sum_2times_over_60(15, 15)
    tax_include(4600)
    judge_rank(44)
    factorial(12)
    power_of_two(2)
