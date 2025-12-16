
import pytest
@pytest.mark.smoke

def  test_login_page_valid_user():
    print("Login with valid user")
    print("Fnciton : aaaaaaa")

@pytest.mark.regression
def test_login_page_wrong_password():
    print("Login with Wrong Password")
    print("Function : bbbbbbb")

   #assert 1 == 2  'one is not equal to two'
    