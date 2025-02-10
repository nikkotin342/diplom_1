import pytest
from praktikum.ingredient import Ingredient
from praktikum import ingredient_types


class TestIngredient:

    @pytest.mark.parametrize('ingredient_type, name, price',
                            [(ingredient_types.INGREDIENT_TYPE_SAUCE, 'test_name_one', 100),
                             (ingredient_types.INGREDIENT_TYPE_FILLING, 'test_name_two', 200)
                             ])
    def test_get_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize('ingredient_type, name, price',
                            [(ingredient_types.INGREDIENT_TYPE_SAUCE, 'test_name_one', 100),
                             (ingredient_types.INGREDIENT_TYPE_FILLING, 'test_name_two', 200)
                             ])
    def test_get_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize('ingredient_type, name, price',
                            [(ingredient_types.INGREDIENT_TYPE_SAUCE, 'test_name_one', 100),
                             (ingredient_types.INGREDIENT_TYPE_FILLING, 'test_name_two', 200)
                             ])
    def test_get_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type