from dataclasses import dataclass
from app_main import db


@dataclass
class Cdr(db.Model):
    __tablename__ = 'cdr'

    id: int
    origin_num: int
    termi_num: int
    call_duration: float

    id = db.Column(db.Integer, primary_key=True)
    origin_num = db.Column(db.Integer)
    termi_num = db.Column(db.Integer)
    call_duration = db.Column(db.Float)
