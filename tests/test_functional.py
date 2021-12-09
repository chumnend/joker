def test_joke(testapp):
    res = testapp.get('/v1/joke', status=200)
    assert b'joke' in res.body
    assert b'answer' in  res.body

def test_notfound(testapp):
    res = testapp.get('/badurl', status=404)
    assert res.status_code == 404
