from unittest.mock import Mock
from praktikum.burger import Burger

class TestBurger:

    def test_set_buns(self):
        mock = Mock()
        mock.get_name.return_value = "Флюоресцентная булка"
        mock.get_price.return_value = 988
        burger = Burger()
        burger.set_buns(mock)
        assert burger.bun.get_name() == mock.get_name() and burger.bun.get_price() == mock.get_price()

    def test_add_ingredient(self):
        mock = Mock()
        mock.get_price.return_value = 100
        mock.get_name.return_value = "test_name"
        mock.get_type.return_value = "SAUCE"
        burger = Burger()
        burger.add_ingredient(mock)
        assert burger.ingredients[0].get_price() == mock.get_price()
        assert burger.ingredients[0].get_name() == mock.get_name()
        assert burger.ingredients[0].get_type() == mock.get_type()
        assert len(burger.ingredients) != 0

    def test_remove_ingredient(self):
        mock = Mock()
        mock.get_price.return_value = 100
        mock.get_name.return_value = "test_name"
        mock.get_type.return_value = "SAUCE"
        burger = Burger()
        burger.add_ingredient(mock)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self):
        one_ingredient = Mock()
        two_ingredient = Mock()
        burger = Burger()
        burger.add_ingredient(one_ingredient)
        burger.add_ingredient(two_ingredient)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == one_ingredient and burger.ingredients[0] == two_ingredient

    def test_get_price(self):
        mock_bun = Mock()
        mock_ingredient = Mock()
        mock_bun.get_price.return_value = 100
        mock_ingredient.get_price.return_value = 50
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == mock_bun.get_price() * 2 + mock_ingredient.get_price()

    def test_get_receipt(self):
        mock_ingredient = Mock()
        mock_bun = Mock()
        mock_ingredient.get_price.return_value = 50
        mock_ingredient.get_name.return_value = "test_name"
        mock_ingredient.get_type.return_value = "sauce"
        mock_bun.get_price.return_value = 100
        mock_bun.get_name.return_value = "булка"
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.set_buns(mock_bun)
        burger.get_price()
        receipt = (f'(==== {mock_bun.get_name()} ====)\n'
                   f'= {mock_ingredient.get_type()} {mock_ingredient.get_name()} =\n'
                   f'(==== {mock_bun.get_name()} ====)\n\n'
                   f'Price: 250')
        assert burger.get_receipt() == receipt