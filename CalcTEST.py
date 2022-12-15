import Calculate
import pytest
#тест калькулятора
class TestCalc:
    #задаем числа и знак действия
    @pytest.fixture()
    def plus(self):
        return 5,'+',5

    @pytest.fixture()
    def minus(self):
        return 10,'-',10

    @pytest.fixture()
    def umnozh(self):
        return 4,'*',5

    @pytest.fixture()
    def delen(self):
        return 10,'/',10

    @pytest.fixture()
    def error(self):
        return '+', '-', '+'
    
    #тест плюса
    def testplus(self,plus):
        assert Calculate.calc(*plus) == 10

    #тест минуса
    def testminus(self,minus):
        assert Calculate.calc(*minus) == 0

    #тест умножения
    def testumnozhenine(self,umnozh):
        assert Calculate.calc(*umnozh) == 20

    #тест деления
    def testdelenie(self,delen):
        assert Calculate.calc(*delen) == 1

    def testerror(self, error):
        with pytest.raises(TypeError):
            Calculate.calc(error)