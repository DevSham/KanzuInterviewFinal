from API import app
import json
# Test method to test get all categories


def test_all():
    with app.test_client() as T:
        response = T.get('Article/api/v1/entry')
        info = json.loads(response.data)
        diary = info['Article_entries'][0]['CategoryName']
        assert type(info) == dict
        assert diary == 'Sports'
# Test method to add a category API


def test_entry():
    with app.test_client() as T:
        response = T.post('/Article/api/v1/entry',
                          json={
                              'CategoryName': 'Business'
                          })
        info = response.get_json()
        my_post1 = info['My_Categories'][2]['CategoryName']
        my_post2 = info['My_Categories'][2]['id']
        assert type(info) == dict
        assert my_post1 == 'Business'
        assert my_post2 == 3
# # Test method to test the get specific entry API


def test_specific_entry():
    with app.test_client() as T:
        response = T.get('/Article/api/v1/entry/1')
        info = json.loads(response.data)
        my_cat1 = info['My_Category'][0]['id']
        my_cat2 = info['My_Category'][0]['CategoryName']
        assert type(info) == dict
        assert my_cat1 == 1
        assert my_cat2 == "Sports"
#  Test method to test the put method.


def test_update_entry():
    with app.test_client() as T:
        response = T.put('/Article/api/v1/entry/1',
                         json={
                             'CategoryName': 'Love'
                         })
        info = json.loads(response.data)
        mod1 = info['Category'][0]['CategoryName']
        assert mod1 == 'Love'


def test_delete_category():
    with app.test_client() as T:
        response = T.delete('/Article/api/v1/entry/2')
        info = json.loads(response.data)
        del1 = info['Categories'][0]['id']
        del2 = info['Categories'][0]['CategoryName']
        assert del1 != 2
        assert del2 != 'Health'
