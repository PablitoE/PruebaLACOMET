from examples.using_my_module import main


def test_main():
    assert main() == (3, 2, 6)
