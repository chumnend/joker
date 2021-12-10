def test_random_joke(testapp):
    res = testapp.get('/api/v1/surprise', status=200)
    assert b'joke' in res.body
    assert b'answer' in  res.body

def test_list_jokes(testapp):
    res = testapp.get('/api/v1/jokes', status=200)
    assert b'jokes' in res.body

def test_notfound(testapp):
    res = testapp.get('/badurl', status=404)
    assert res.status_code == 404
