# 找一个数所有的因数
def factor(num: int):
    factors = []
    for i in range(1, num):
        if num % i == 0:
            factors.append(i)
    factors.append(num)
    return factors

<<<<<<< HEAD
=======

>>>>>>> fe1a949 (hyc库4.0.0α3版本)
# 判断一个数是否为完全数
def per_num(num: int):
    sum = 0
    factors = factor(num)
<<<<<<< HEAD
    for i in range(len(factors)-1):
=======
    for i in range(len(factors) - 1):
>>>>>>> fe1a949 (hyc库4.0.0α3版本)
        sum += factors[i]
    if sum == num:
        return True
    else:
        return False

<<<<<<< HEAD
# 判断一个数是否为质数
def pri_num(num: int):
=======

# 判断一个数是否为质数
def prime(num: int):
>>>>>>> fe1a949 (hyc库4.0.0α3版本)
    if len(factor(num)) == 2:
        return True
    else:
        return False

<<<<<<< HEAD
# 判断一个数是否为偶数
def even_num(num: int):
    if num %2 == 0:
=======

# 判断一个数是否为偶数
def even_num(num: int):
    if num % 2 == 0:
>>>>>>> fe1a949 (hyc库4.0.0α3版本)
        return True
    else:
        return False

<<<<<<< HEAD
=======

>>>>>>> fe1a949 (hyc库4.0.0α3版本)
# （最大）公因数
def hcf(num_list: list[int]):
    common_f = []
    for i in factor(num_list[0]):
        common = True
        for j in num_list:
<<<<<<< HEAD
            if not i in factor(j):
                common = False
        if common:
                common_f.append(i)
    return common_f, max(common_f)

=======
            if i not in factor(j):
                common = False
        if common:
            common_f.append(i)
    return common_f, max(common_f)


>>>>>>> fe1a949 (hyc库4.0.0α3版本)
# 注意：本函数会返回两个值：两个数的公因数和最大公因数；请在该函数的参数内传入一个包含两个或以上数字的列表！

# （最小）公倍数
def lcm(num_list: list[int]):
    i = 1
    common = False
    while not common:
        common = True
<<<<<<< HEAD
        now_num = num_list[0]*i
=======
        now_num = num_list[0] * i
>>>>>>> fe1a949 (hyc库4.0.0α3版本)
        for j in num_list:
            if not now_num % j == 0:
                common = False
        i += 1
    return now_num

# 注意：请在该函数的参数内传入一个包含两个或以上数字的列表！

<<<<<<< HEAD
=======

>>>>>>> fe1a949 (hyc库4.0.0α3版本)
# 分解质因数
def pri_fac(num: int):
    pri_factors = []
    now_num = num
<<<<<<< HEAD
    while not pri_num(now_num):
        pri_factor = factor(now_num)[1]
        now_num = int(now_num/pri_factor)
=======
    while not prime(now_num):
        pri_factor = factor(now_num)[1]
        now_num = int(now_num / pri_factor)
>>>>>>> fe1a949 (hyc库4.0.0α3版本)
        pri_factors.append(pri_factor)
    if pri_factors:
        text = '{} = '.format(num)
        for i in pri_factors:
            text += '{}*'.format(i)
        text += str(now_num)
    else:
        text = '{} = {}'.format(num, num)
    return text

<<<<<<< HEAD
=======

>>>>>>> fe1a949 (hyc库4.0.0α3版本)
# 互质数
def coprime(num_list: list[int]):
    if len(hcf(num_list)) == 1:
        return True
    else:
<<<<<<< HEAD
        return False
=======
        return False


# 平均数
def mean(num_list: list[int]):
    result = sum(num_list) / len(num_list)
    return result
>>>>>>> fe1a949 (hyc库4.0.0α3版本)
