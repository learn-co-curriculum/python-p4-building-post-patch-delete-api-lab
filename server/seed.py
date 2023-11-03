#!/usr/bin/env python3

from app import app
from models import db, Bakery, BakedGood

with app.app_context():

    BakedGood.query.delete()
    Bakery.query.delete()
    
    bakeries = []
    bakeries.append(Bakery(name='Delightful donuts'));
    bakeries.append(Bakery(name='Incredible crullers'));
    db.session.add_all(bakeries)

    baked_goods = []
    baked_goods.append(BakedGood(name='Chocolate dipped donut', price=2.75, bakery=bakeries[0]));
    baked_goods.append(BakedGood(name='Apple-spice filled donut', price=3.50, bakery=bakeries[0]));
    baked_goods.append(BakedGood(name='Glazed honey cruller', price=3.25, bakery=bakeries[1]));
    baked_goods.append(BakedGood(name='Chocolate cruller', price=3.40, bakery=bakeries[1]));

    db.session.add_all(baked_goods)
    db.session.commit()