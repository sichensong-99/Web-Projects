import datetime
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()



class Hotel(db.Model):
    __tablename__ = 'py_hotel'

    id = db.Column(db.Integer, primary_key=True)
    hotel = db.Column(db.String(100))
    lead_time = db.Column(db.Integer)
    arrival_date = db.Column(db.Integer)
    stays_in_weekend_nights = db.Column(db.Integer)
    stays_in_week_nights = db.Column(db.Integer)
    meal = db.Column(db.String(100))
    country = db.Column(db.String(100))
    market_segment = db.Column(db.String(100))
    reserved_room_type = db.Column(db.String(100))
    booking_changes = db.Column(db.Integer)
    customer_type = db.Column(db.String(100))
    reservation_status = db.Column(db.String(100))
    
    def to_x_y(self):
        return {'x': self.arrival_date, 'y': self.stays_in_week_nights}
    def to_x_y2(self):
        return {'x': self.arrival_date, 'y': self.stays_in_weekend_nights}

    @classmethod
    def from_dict(cls, in_dict):
        cls = Hotel()
        cls.id = in_dict['id']
        cls.hotel = in_dict['hotel']
        cls.lead_time = in_dict['lead_time']
        cls.arrival_date = in_dict['arrival_date']
        cls.stays_in_weekend_nights = in_dict['stays_in_weekend_nights']
        cls.stays_in_week_nights = in_dict['stays_in_week_nights']
        cls.meal = in_dict['meal']
        cls.country = in_dict['country']
        cls.market_segment = in_dict['market_segment']
        cls.reserved_room_type = in_dict['reserved_room_type']
        cls.booking_changes = in_dict['booking_changes']
        cls.customer_type = in_dict['customer_type']
        cls.reservation_status = in_dict['reservation_status']
        return cls