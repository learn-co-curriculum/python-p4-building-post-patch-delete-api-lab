#!/usr/bin/env python3

from random import randint, choice as rc

from faker import Faker

from app import app
from models import db, Bakery, BakedGood


fake = Faker()

with app.app_context():

    BakedGood.query.delete()
    Bakery.query.delete()
    
    bakeries = []
    for i in range(20):
        b = Bakery(
            name=fake.company()
        )
        bakeries.append(b)
    
    db.session.add_all(bakeries)

    baked_goods = []
    names = []
    for i in range(200):

        name = fake.first_name()
        while name in names:
            name = fake.first_name()
        names.append(name)

        bg = BakedGood(
            name=name,
            price=randint(1,10),
            bakery=rc(bakeries)
        )

        baked_goods.append(bg)

    db.session.add_all(baked_goods)
    db.session.commit()
    
    most_expensive_baked_good = rc(baked_goods)
    most_expensive_baked_good.price = 100
    db.session.add(most_expensive_baked_good)
    db.session.commit()
