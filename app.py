from flask import Flask, jsonify, request
from extensions import db, migrate
from models import db, Clan, Trener, Trening, Specijalnost
from flask_marshmallow import Marshmallow
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
ma = Marshmallow(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/fitnesscentar"
db.init_app(app)
migrate.init_app(app, db)


@app.route('/')
def index():
    return "Početna"


@app.route('/treneri', methods=['GET'])
def treneri():
    svi_treneri = Trener.query.all()
    return jsonify(treneri_schema.dump(svi_treneri))


@app.route('/treneri/<id>', methods=['GET'])
def trener(id):
    trener = Trener.query.filter_by(id=id).first()
    return jsonify(trener.to_dict())

@app.route('/treneri', methods=['POST'])
def dodaj_trenera():
    data = request.get_json()
    novi = Trener(
        ime=data.get('ime'),
        prezime=data.get('prezime'),
        specijalnost_id=data.get('specijalnost_id')
    )
    db.session.add(novi)
    db.session.commit()
    return jsonify({"poruka": "Trener dodan"}), 201

@app.route('/treneri/<id>', methods=['PUT'])
def azuriraj_trenera(id):
    t = Trener.query.filter_by(id=id).first()
    data = request.get_json()
    t.ime = data.get('ime', t.ime)
    t.prezime = data.get('prezime', t.prezime)
    t.specijalnost_id = data.get('specijalnost_id', t.specijalnost_id)
    db.session.commit()
    return jsonify({"poruka": "Trener ažuriran"})

@app.route('/treneri/<id>', methods=['DELETE'])
def izbrisi_trenera(id):
    t = Trener.query.filter_by(id=id).first()
    db.session.delete(t)
    db.session.commit()
    return jsonify({"poruka": "Trener obrisan"})


@app.route('/clanovi', methods=['GET'])
def clanovi():
    clanovi = Clan.query.all()

    return jsonify(clanovi_schema.dump(clanovi))

@app.route('/clanovi/<id>', methods=['GET'])
def clan(id):
    clanovi = Clan.query.filter_by(id=id).first()
    return jsonify(clanovi.to_dict())

@app.route('/clanovi', methods=['POST'])
def dodaj_clana():
    data = request.get_json()
    novi = Clan(
        ime=data.get('ime'),
        prezime=data.get('prezime'),
        email=data.get('email')
    )
    db.session.add(novi)
    db.session.commit()
    return jsonify({"poruka": "Clan dodan"}), 201

@app.route('/clanovi/<id>', methods=['PUT'])
def azuriraj_clana(id):
    c = Clan.query.filter_by(id=id).first()
    data = request.get_json()
    c.ime = data.get('ime', c.ime)
    c.prezime = data.get('prezime', c.prezime)
    c.email = data.get('email', c.email)
    db.session.commit()
    return jsonify({"poruka": "Clan ažuriran"})

@app.route('/clanovi/<id>', methods=['DELETE'])
def izbrisi_clana(id):
    c = Clan.query.filter_by(id=id).first()
    db.session.delete(c)
    db.session.commit()
    return jsonify({"poruka": "Clan obrisan"})


@app.route('/treninzi', methods=['GET'])
def treninzi():
    treninzi = Trening.query.all()

    return jsonify([t.to_dict() for t in treninzi])

@app.route('/treninzi/<id>', methods=['GET'])
def trening(id):
    treninzi = Trening.query.filter_by(id=id).first()
    return jsonify(treninzi.to_dict())

@app.route('/treninzi', methods=['POST'])
def dodaj_trening():
    data = request.get_json()
    novi = Trening(
        naziv=data.get('naziv'),
        opis=data.get('opis'),
        dan_u_tjednu=data.get('dan_u_tjednu'),
        vrijeme_pocetka=data.get('vrijeme_pocetka'),
        vrijeme_kraja=data.get('vrijeme_kraja'),
        kapacitet=data.get('kapacitet'),
        trener_id=data.get('trener_id'),
    )
    db.session.add(novi)
    db.session.commit()
    return jsonify({"poruka": "Trening dodan"}), 201


@app.route('/treninzi/<id>', methods=['PUT'])
def azuriraj_trening(id):
    t = Trening.query.filter_by(id=id).first()
    data = request.get_json()
    t.naziv = data.get('naziv', t.naziv)
    t.opis = data.get('opis', t.opis)
    t.dan_u_tjednu = data.get('dan_u_tjednu', t.dan_u_tjednu)
    t.vrijeme_pocetka = data.get('vrijeme_pocetka', t.vrijeme_pocetka)
    t.vrijeme_kraja = data.get('vrijeme_kraja', t.vrijeme_kraja)
    t.kapacitet = data.get('kapacitet', t.kapacitet)
    t.trener_id = data.get('trener_id', t.trener_id)

    db.session.commit()
    return jsonify({"poruka": "Trening ažuriran"})

@app.route('/treninzi/<id>', methods=['DELETE'])
def izbrisi_trening(id):
    t = Trening.query.filter_by(id=id).first()
    db.session.delete(t)
    db.session.commit()
    return jsonify({"poruka": "Trening obrisan"})


@app.route('/specijalnosti', methods=['GET'])
def specijalnosti():
    specijalnosti = Specijalnost.query.all()

    return jsonify([s.to_dict() for s in specijalnosti])

@app.route('/specijalnosti/<id>', methods=['GET'])
def specijalnost(id):
    specijalnost = Specijalnost.query.filter_by(id=id).first()
    return jsonify(specijalnost.to_dict())


@app.route('/specijalnosti', methods=['POST'])
def dodaj_specijalnost():
    data = request.get_json()
    nova = Specijalnost(
        naziv=data.get('naziv'),

    )
    db.session.add(nova)
    db.session.commit()
    return jsonify({"poruka": "Specijalnost dodana"}), 201


@app.route('/specijalnosti/<id>', methods=['PUT'])
def azuriraj_specijalnost(id):
    s = Specijalnost.query.filter_by(id=id).first()
    data = request.get_json()
    s.naziv = data.get('naziv', s.naziv)
    db.session.commit()
    return jsonify({"poruka": "Specijalnost azurirana"})


@app.route('/specijalnosti/<id>', methods=['DELETE'])
def izbrisi_specijalnost(id):
    s = Specijalnost.query.filter_by(id=id).first()
    db.session.delete(s)
    db.session.commit()
    return jsonify({"poruka": "Specijalnost obrisana"})


class SpecijalnostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Specijalnost


class TrenerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Trener
        include_fk = True

    specijalnost = ma.Nested(SpecijalnostSchema)

class ClanSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Clan

clan_schema = ClanSchema()
clanovi_schema = ClanSchema(many=True)


trener_schema = TrenerSchema()
treneri_schema = TrenerSchema(many=True)

if __name__ == '__main__':
    app.run(debug=True)