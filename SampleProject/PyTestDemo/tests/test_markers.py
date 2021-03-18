import pytest

@pytest.mark.smoke
def test_login():
    print("login to the application")


@pytest.mark.regression
def test_add_products():
    print("add products")


@pytest.mark.smoke
def test_logout():
    print("logout the application")