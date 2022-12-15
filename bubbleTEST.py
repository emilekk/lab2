# тест сортировки пузырьком
import pytest
import Calculate

class TestBubble:

    #сортировка в порядке возрастания
    @pytest.fixture()
    def toMax(self):
        return 1

    #сортировка в порядке убывания
    @pytest.fixture()
    def toMin(self):
        return 2

    # запуск с ошибкой
    @pytest.fixture()
    def toError(self):
       return 3

    #тест сортировки в порядке возрастания
    def testMax(self, toMax):
        assert Calculate.bubble(toMax) == [1,2,3,4,5,6,7,8]

    #тест сортировки в порядке убывания
    def testMin(self, toMin):
        assert Calculate.bubble(toMin) == [8,7,6,5,4,3,2,1]

    #тест сортировки с ошибкой
    def testMin(self, toError):
        assert Calculate.bubble(toError) == -1