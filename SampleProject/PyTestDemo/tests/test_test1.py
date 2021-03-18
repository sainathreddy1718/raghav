def test_test1():
    x = 10
    y = 20
    assert x == y

def test_test2():

    name = "selenium"
    title = "selenium is for web autoamiton"
    assert name in title

def test_test3():
    name = "jenkins"
    title = "jenkins is ci server"
    assert name in title, "Title doesnot match"