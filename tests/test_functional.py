def test_root(testapp):
    res = testapp.get('/', status=200)
    assert b'Hello World' in res.body

def test_hello_with_param(testapp):
    res = testapp.get('/?name=Nicholas', status=200)
    assert b'Hello, Nicholas' in res.body