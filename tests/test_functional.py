def test_root(testapp):
    res = testapp.get('/', status=200)
    assert b'Hello World' in res.body
