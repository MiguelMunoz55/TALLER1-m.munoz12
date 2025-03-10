from app.config.db import db

class Perro(db.Model):
    __tablename__ = "perros"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(45), nullable=False)
    raza = db.Column(db.String(45), nullable=False)
    edad = db.Column(db.Integer, nullable=False)

    # Claves foráneas
    id_guarderia = db.Column(db.Integer, db.ForeignKey('guarderias.id'), nullable=False)
    id_cuidador = db.Column(db.Integer, db.ForeignKey('cuidadores.id'), nullable=False)

