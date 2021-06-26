import pytest
import yaml

from python_code.calc import Calculator

with open("./datas/calc.yaml") as f:
    calc = yaml.safe_load(f)['calc']
    adddatas = calc['add']
    add_datas = adddatas['datas']
    print(add_datas)
    addmyid = adddatas['myid']
    print(addmyid)
    subdatas = calc['sub']
    sub_datas = subdatas['datas']
    print(sub_datas)
    submyid = subdatas['myid']
    print(submyid)
    muldatas = calc['mul']
    mul_datas = muldatas['datas']
    print(mul_datas)
    mulmyid = muldatas['myid']
    print(mulmyid)
    divdatas = calc['div']
    div_datas = divdatas['datas']
    print(div_datas)
    divmyid = divdatas['myid']
    print(divmyid)


def test_datas():
    print(add_datas)
    print(sub_datas)
    print(mul_datas)
    print(div_datas)


@pytest.fixture(scope="function")
def get_calc():
    print("开始计算")
    calc = Calculator()
    yield calc;
    print("计算结束")


class TestCalc:

    @pytest.mark.parametrize("a,b,expect", add_datas, ids=addmyid)
    def test_add(self, get_calc, a, b, expect):
        result = get_calc.add(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", sub_datas, ids=submyid)
    def test_sub(self, get_calc, a, b, expect):
        result = get_calc.sub(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", mul_datas, ids=mulmyid)
    def test_mul(self, get_calc, a, b, expect):
        result = get_calc.mul(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", div_datas, ids=divmyid)
    def test_div(self, get_calc, a, b, expect):
        result = get_calc.div(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect
