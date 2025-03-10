from app.config.db import db

class Cuidador(db.Model):
    __tablename__ = "cuidadores"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(45), nullable=False)
    telefono = db.Column(db.String(45), nullable=False)

    # Clave foránea para relacionar con guardería
    id_guarderia = db.Column(db.Integer, db.ForeignKey('guarderias.id'), nullable=False)

    # Relación con perros
    perros = db.relationship('Perro', backref='cuidador', lazy=True)


