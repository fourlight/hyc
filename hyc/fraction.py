from hyc.num import *


# 分数类
class Fraction:
    def __init__(self, denominator: int, numerator: int, num: int = 0):
        self.fraction = [denominator, numerator + num * denominator]

    # 分数化整数（保留到个位）
    def __int__(self):
        if self.fraction[1] > self.fraction[0]:
            num = self.fraction[1] // self.fraction[0]
        else:
            num = 0
        return num

    # 读作
    def __repr__(self):
        self.red_fr()
        if float(self) < 1 or float(self) % 1 == 0:
            string = f'{self.fraction[0]}分之{self.fraction[1]}'
        elif float(self) > 1:
            string = f'{int(self)}又{self.fraction[0]}分之{self.fraction[1] % self.fraction[0]}'
        return string

    # 分数化小数
    def __float__(self):
        decimal = self.fraction[1] / self.fraction[0]
        return decimal

    # 约分
    def red_fr(self):
        if self.simp_fr():
            return self
        else:
            _, common_div = hcf(self.fraction)
            for i in range(2):
                self.fraction[i] = self.fraction[i] // common_div
            return self

    # 最简分数
    def simp_fr(self):
        if coprime(self.fraction):
            return True
        else:
            return False

    # 倒数
    def opposide(self):
        fraction_opposide = Fraction(self.fraction[1], self.fraction[0])
        return fraction_opposide

    # 比较运算
    # x<y
    def __lt__(self, other):
        if float(self) < float(other):
            return True
        else:
            return False

    # x<=y
    def __le__(self, other):
        if float(self) <= float(other):
            return True
        else:
            return False

    # x==y
    def __eq__(self, other):
        if float(self) == float(other):
            return True
        else:
            return False

    # x!=y
    def __ne__(self, other):
        if float(self) == float(other):
            return False
        else:
            return True

    # x>y
    def __gt__(self, other):
        if float(self) > float(other):
            return True
        else:
            return False

    # x>y
    def __ge__(self, other):
        if float(self) >= float(other):
            return True
        else:
            return False

    # 分数运算（当分数为左操作数时）
    # 分数加整数（小数）
    def __add__(self, other):
        if type(other) == int or type(other) == float:
            other = covert(other)
        result = 0
        fraction_list = den_di([self, other])
        for i in fraction_list:
            result += i.fraction[1]
        fraction_sum = Fraction(fraction_list[0].fraction[0], result)
        return fraction_sum.red_fr()

    # 分数减整数（小数）
    def __sub__(self, other):
        if type(other) == int or type(other) == float:
            other = covert(other)
        minuend, subtracted = den_di([self, other])
        minuend.fraction[1] -= subtracted.fraction[1]
        return minuend.red_fr()

    # 分数乘整数（小数）
    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            other = covert(other)
        deno = 1
        mole = 1
        for i in [self.fraction, other.fraction]:
            deno *= i[0]
            mole *= i[1]
        result = Fraction(deno, mole)
        return result.red_fr()

    # 分数除整数（小数）
    def __truediv__(self, other):
        if type(other) == int or type(other) == float:
            other = covert(other)
        result = self * other.opposide()
        return result.red_fr()

    # 分数的整数次方
    def __pow__(self, power: int, modulo=None):
        result = 1
        for i in range(power):
            result *= self
        return int(result)

    # 分数整除整数（小数）
    def __floordiv__(self, other):
        result = float(self) // float(other)
        return int(result)

    # 分数运算（当分数为右操作数时）（不包括平方）
    # 整数（小数）加分数
    def __radd__(self, other):
        result = covert(other) + self
        return int(result)

    # 整数（小数）减分数
    def __rsub__(self, other):
        result = covert(other) - self
        return int(result)

    # 整数（小数）乘分数
    def __rmul__(self, other):
        result = covert(other) * self
        return int(result)

    # 整数（小数）除分数
    def __rtruediv__(self, other):
        result = covert(other) / self
        return int(result)

    # 整数（小数）整除分数
    def __rfloordiv__(self, other):
        result = float(other) // float(self)
        return int(result)


# 通分
def den_di(fraction_list: list[Fraction]):
    all_deno = []
    for i in fraction_list:
        all_deno.append(i.fraction[0])
    common_deno = lcm(all_deno)
    new_fraction_list = []
    for i in fraction_list:
        common_mul = int(common_deno / i.fraction[0])
        i = Fraction(i.fraction[0] * common_mul, i.fraction[1] * common_mul)
        new_fraction_list.append(i)
    return new_fraction_list


# 整数（小数）化分数
def covert(covert_num: float):
    covert_num = float(covert_num)
    num, decimal = str(covert_num).split('.')
    if covert_num < 1:
        frac = Fraction(10 ** len(decimal), int(decimal))
    else:
        frac = Fraction(10 ** len(decimal), int(decimal) + int(num) * 10 ** len(decimal))
    return frac.red_fr()
