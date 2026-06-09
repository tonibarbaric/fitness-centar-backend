from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Specijalnost(db.Model):
    __tablename__ = "specijalnosti"
    id = db.Column(db.Integer, primary_key=True)
    naziv = db.Column(db.String(50), nullable=False, unique=True)

    def to_dict(self):
        return {
            "id": self.id,
            "naziv": self.naziv
        }


class Trener(db.Model):
    __tablename__ = "treneri"
    id = db.Column(db.Integer, primary_key=True)
    ime = db.Column(db.String(50), nullable=False)
    prezime = db.Column(db.String(50), nullable=False)
    specijalnost_id = db.Column(db.Integer, db.ForeignKey('specijalnosti.id'), nullable=True)

    treninzi = db.relationship('Trening', backref='trener', lazy=True)
    specijalnost = db.relationship('Specijalnost', backref='treneri')

    def to_dict(self):
        return {
            "id": self.id,
            "ime": self.ime,
            "prezime": self.prezime,
            "specijalnost": self.specijalnost.to_dict() if self.specijalnost else None
        }

class Clan(db.Model):
    __tablename__ = "clanovi"
    id = db.Column(db.Integer, primary_key=True)
    ime = db.Column(db.String(50), nullable=False)
    prezime = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "ime": self.ime,
            "prezime": self.prezime,
            "email": self.email
        }


class Trening(db.Model):
    __tablename__ = "treninzi"
    id = db.Column(db.Integer, primary_key=True)
    naziv = db.Column(db.String(100), nullable=False)
    opis = db.Column(db.Text, nullable=True)
    dan_u_tjednu = db.Column(db.String(20), nullable=False)
    vrijeme_pocetka = db.Column(db.DateTime(), nullable=False)
    vrijeme_kraja = db.Column(db.DateTime(), nullable=False)
    kapacitet = db.Column(db.Integer, nullable=False)
    trener_id = db.Column(db.Integer, db.ForeignKey('treneri.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "naziv": self.naziv,
            "opis": self.opis,
            "dan_u_tjednu": self.dan_u_tjednu,
            "vrijeme_pocetka": self.vrijeme_pocetka.isoformat() if self.vrijeme_pocetka else None,
            "vrijeme_kraja": self.vrijeme_kraja.isoformat() if self.vrijeme_kraja else None,
            "kapacitet": self.kapacitet,
            "trener_id": self.trener_id,
            "trener": {
                "id": self.trener.id,
                "ime": self.trener.ime,
                "prezime": self.trener.prezime
            } if self.trener else None
        }

