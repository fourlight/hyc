# 百分数类
class Percentage:
    def __init__(self, numerator):
        self.numerator = numerator
        self.one_unit = None

    # 单位“1”加百分数
    def __radd__(self, other):
        self.one_unit = other
        result = other + self.one_unit * self.numerator / 100
        self.one_unit = None
        return int(result)

    # 单位“1”减百分数
    def __rsub__(self, other):
        self.one_unit = other
        result = other - self.one_unit * (self.numerator / 100)
        self.one_unit = None
        return int(result)

    # 单位“1”乘百分数
    def __rmul__(self, other):
        self.one_unit = other
        result = other * (self.numerator / 100)
        self.one_unit = None
        return int(result)

    # 单位“1”除以百分数
    def __rtruediv__(self, other):
        self.one_unit = other
        result = other / (self.numerator / 100)
        self.one_unit = None
        return int(result)

    # 百分数读作
    def __repr__(self):
        return f'{self.numerator}%'
