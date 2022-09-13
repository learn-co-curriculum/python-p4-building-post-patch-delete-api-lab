import json
from os import environ
import re

from app import app
from models import db, Bakery, BakedGood

class TestApp:
    '''Flask application in flask_app.py'''

    def test_bakeries_route(self):
        '''has a resource available at "/bakeries".'''
        response = app.test_client().get('/bakeries')
        assert(response.status_code == 200)

    def test_bakeries_route_returns_json(self):
        '''provides a response content type of application/json at "/bakeries"'''
        response = app.test_client().get('/bakeries')
        assert response.content_type == 'application/json'

    def test_bakeries_route_returns_list_of_bakery_objects(self):
        '''returns JSON representing models.Bakery objects.'''
        with app.app_context():
            b = Bakery(name="Mr. Bakery")
            db.session.add(b)
            db.session.commit()

            response = app.test_client().get('/bakeries')
            data = json.loads(response.data.decode())
            assert(type(data) == list)
            for record in data:
                assert(type(record) == dict)
                assert(record['id'])
                assert(record['name'])
                assert(record['created_at'])

            db.session.delete(b)
            db.session.commit()

    def test_bakery_by_id_route(self):
        '''has a resource available at "/bakeries/<int:id>".'''
        response = app.test_client().get('/bakeries/1')
        assert(response.status_code == 200)

    def test_bakery_by_id_route_returns_json(self):
        '''provides a response content type of application/json at "/bakeries/<int:id>"'''
        response = app.test_client().get('/bakeries/1')
        assert response.content_type == 'application/json'

    def test_bakery_by_id_route_returns_one_bakery_object(self):
        '''returns JSON representing one models.Bakery object.'''
        with app.app_context():
            b = Bakery(name="Mr. Bakery")
            db.session.add(b)
            db.session.commit()

            response = app.test_client().get('/bakeries/1')
            data = json.loads(response.data.decode())
            assert(type(data) == dict)
            assert(data['id'])
            assert(data['name'])
            assert(data['created_at'])

            db.session.delete(b)
            db.session.commit()

    def test_baked_goods_by_price_route(self):
        '''has a resource available at "/baked_goods/by_price".'''
        response = app.test_client().get('/baked_goods/by_price')
        assert(response.status_code == 200)
    
    def test_bakery_by_id_route_returns_json(self):
        '''provides a response content type of application/json at "/baked_goods/by_price"'''
        response = app.test_client().get('/baked_goods/by_price')
        assert response.content_type == 'application/json'

    def test_baked_goods_by_price_returns_list_of_baked_goods(self):
        '''returns JSON representing one models.Bakery object.'''
        with app.app_context():
            b = BakedGood(name="Madeleine", price=10)
            db.session.add(b)
            db.session.commit()

            response = app.test_client().get('/baked_goods/by_price')
            data = json.loads(response.data.decode())
            assert(type(data) == list)
            for record in data:
                assert(record['id'])
                assert(record['name'])
                assert(record['price'])
                assert(record['created_at'])

            db.session.delete(b)
            db.session.commit()

    def test_most_expensive_baked_good_route(self):
        '''has a resource available at "/baked_goods/most_expensive".'''
        response = app.test_client().get('/baked_goods/most_expensive')
        assert(response.status_code == 200)

    def test_most_expensive_baked_good_route_returns_json(self):
        '''provides a response content type of application/json at "/bakeries/<int:id>"'''
        response = app.test_client().get('/baked_goods/most_expensive')
        assert response.content_type == 'application/json'

    def test_most_expensive_baked_good_route_returns_one_baked_good_object(self):
        '''returns JSON representing one models.BakedGood object.'''
        with app.app_context():
            b = BakedGood(name="Madeleine", price=10)
            db.session.add(b)
            db.session.commit()

            response = app.test_client().get('/baked_goods/most_expensive')
            data = json.loads(response.data.decode())
            assert(type(data) == dict)
            assert(data['id'])
            assert(data['name'])
            assert(data['price'])
            assert(data['created_at'])

            db.session.delete(b)
            db.session.commit()
    
    def test_most_expensive_baked_good_route_returns_most_expensive_baked_good_object(self):
        '''returns JSON representing one models.BakedGood object.'''
        with app.app_context():
            b = BakedGood(name="Madeleine", price=10)
            db.session.add(b)
            db.session.commit()

            response = app.test_client().get('/baked_goods/most_expensive')
            data = json.loads(response.data.decode())
            prices = [baked_good.price for baked_good in BakedGood.query.all()]
            highest_price = max(prices)

            assert(data['price'] == highest_price)

            db.session.delete(b)
            db.session.commit()
