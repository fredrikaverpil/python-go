import pytest

import hello_world_go


def test_hello():
    assert hello_world_go.hello("fredrik") == "hello hello fredrik"


def test_sum():
    assert hello_world_go.sum(1000, 337) == 1337