from db import db


class CarModel(db.Model):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(50), unique=True)
    year = db.Column(db.Integer, nullable=True)

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def __repr__(self):
        return '<Cars %s>' % self.brand

    @classmethod
    def find_by_name(cls, brand):
        return cls.query.filter_by(brand=brand).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()