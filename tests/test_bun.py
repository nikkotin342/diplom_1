from praktikum.bun import Bun

class TestBun:

    def test_get_name(self):
        bun = Bun('Флюоресцентная булка', 988)
        assert bun.get_name() == 'Флюоресцентная булка'

    def test_get_price(self):
        bun = Bun('Флюоресцентная булка', 988)
        assert bun.get_price() == 988