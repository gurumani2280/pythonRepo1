class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        print()
        print(hasattr(x, "check")) #False
        print(hasattr(x, "title")) #True
        #assert hasattr(x, "check")
        print(x.title())
        assert hasattr(x, "title")