from datetime import date

from app import app
from models import db, Bakery, BakedGood

class TestBakery:
    '''Bakery model in models.py'''

    with app.app_context():
        b = Bakery.query.filter(Bakery.name == "Mr. Bakery")
        for mb in b:
            db.session.delete(mb)
        db.session.commit()

    def test_can_instantiate(self):
        '''can be instantiated with a name.'''
        b = Bakery(name="Mr. Bakery")
        assert(b)
    
    def test_can_be_created(self):
        '''can create records that can be committed to the database.'''
        with app.app_context():
            b = Bakery(name="Mr. Bakery")
            db.session.add(b)
            db.session.commit()

            db.session.delete(b)
            db.session.commit()

    def test_can_be_retrieved(self):
        '''can be used to retrieve records from the database.'''
        with app.app_context():
            b = Bakery.query.all()

    def test_can_be_serialized(self):
        '''can create records with a to_dict() method for serialization.'''
        with app.app_context():
            b = Bakery(name="Mr. Bakery")
            db.session.add(b)
            db.session.commit()
            bs = Bakery.query.first().to_dict()
            assert(bs['id'])
            assert(bs['created_at'])
        
            db.session.delete(b)
            db.session.commit()

    def test_can_be_deleted(self):
        '''can delete its records.'''
        with app.app_context():
            b = Bakery(name="Mr. Bakery")
            db.session.add(b)
            db.session.commit()

            b = Bakery.query.filter(Bakery.name == "Mr. Bakery")
            for mb in b:
                db.session.delete(mb)
            db.session.commit()

class TestBakedGood:
    '''BakedGood model in models.py'''

    with app.app_context():
        bg = BakedGood.query.filter(BakedGood.name == "Madeleine")
        for m in bg:
            db.session.delete(m)
        db.session.commit()

    def test_can_instantiate(self):
        '''can be instantiated with a name and price.'''
        bg = BakedGood(name="Madeleine", price=4)
        assert(bg)
    
    def test_can_be_created(self):
        '''can create records that can be committed to the database.'''
        with app.app_context():
            bg = BakedGood(name="Madeleine")
            db.session.commit()

    def test_can_be_retrieved(self):
        '''can be used to retrieve records from the database.'''
        with app.app_context():
            bg = BakedGood.query.all()

    def test_can_be_serialized(self):
        '''can create records with a to_dict() method for serialization.'''
        with app.app_context():
            bg = BakedGood(name="Madeleine")
            db.session.commit()
            bgs = BakedGood.query.first().to_dict()
            assert(bgs['id'])
            assert(bgs['created_at'])

    def test_can_be_deleted(self):
        '''can delete its records.'''
        with app.app_context():
            bg = BakedGood.query.filter(BakedGood.name == "Madeleine")
            for m in bg:
                db.session.delete(m)
            db.session.commit()
