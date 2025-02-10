import pytest
from praktikum.database import Database
from praktikum.ingredient_types import *

class TestDatabase:

    @pytest.mark.parametrize('bun_name, price, index',
                             [('black bun', 100, 0),
                              ("white bun", 200, 1),
                              ("red bun", 300, 2)
                              ])
    def test_init_database(self, bun_name, price, index):
        db = Database()
        assert db.available_buns()[index].get_name() == bun_name and db.available_buns()[index].get_price() == price

    @pytest.mark.parametrize('type, name, price, index',
                             [(INGREDIENT_TYPE_SAUCE, "hot sauce", 100, 0),
                              (INGREDIENT_TYPE_SAUCE, "sour cream", 200, 1),
                              (INGREDIENT_TYPE_SAUCE, "chili sauce", 300, 2),
                              (INGREDIENT_TYPE_FILLING, "cutlet", 100, 3),
                              (INGREDIENT_TYPE_FILLING, "dinosaur", 200, 4),
                              (INGREDIENT_TYPE_FILLING, "sausage", 300, 5)
                              ])
    def test_init_database(self, type, name, price, index):
        db = Database()
        assert db.available_ingredients()[index].get_type() == type
        assert db.available_ingredients()[index].get_name() == name
        assert db.available_ingredients()[index].get_price() == price

