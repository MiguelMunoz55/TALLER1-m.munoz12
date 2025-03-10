from app.config.db import db

class Guarderia(db.Model):
    __tablename__ = "guarderias"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(45), nullable=True)
    direccion = db.Column(db.String(45), nullable=True)
    telefono = db.Column(db.String(45), nullable=True)

    # Relación con cuidadores y perros
    cuidadores = db.relationship('Cuidador', backref='guarderia', lazy=True)
    perros = db.relationship('Perro', backref='guarderia', lazy=True)
