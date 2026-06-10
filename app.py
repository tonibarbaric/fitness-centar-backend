from flask import Flask, jsonify, request
from extensions import db, migrate
from models import Clan, Trener, Trening, Specijalnost
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/fitnesscentar"
db.init_app(app)
migrate.init_app(app, db)


@app.route('/')
def index():
    return "Početna"


@app.route('/statistika', methods=['GET'])
def statistika():
    return jsonify({
        "treneri": Trener.query.count(),
        "clanovi": Clan.query.count(),
        "treninzi": Trening.query.count()
    })


@app.route('/clanovi', methods=['GET'])
def clanovi():
    svi_clanovi = Clan.query.all()
    return jsonify([c.to_dict() for c in svi_clanovi])


@app.route('/clanovi/<id>', methods=['GET'])
def clan(id):
    c = Clan.query.get_or_404(id)
    return jsonify(c.to_dict())


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
    return jsonify({"poruka": "Član dodan"}), 201


@app.route('/clanovi/<id>', methods=['PUT'])
def uredi_clana(id):
    c = Clan.query.get_or_404(id)
    data = request.get_json()

    c.ime = data.get('ime')
    c.prezime = data.get('prezime')
    c.email = data.get('email')

    db.session.commit()
    return jsonify({"poruka": "Član uspješno ažuriran"})


@app.route('/clanovi/<id>', methods=['DELETE'])
def izbrisi_clana(id):
    c = Clan.query.get_or_404(id)
    db.session.delete(c)
    db.session.commit()
    return jsonify({"poruka": "Član obrisan"})


@app.route('/treneri', methods=['GET'])
def treneri():
    svi_treneri = Trener.query.all()
    return jsonify([t.to_dict() for t in svi_treneri])


@app.route('/treneri/<id>', methods=['GET'])
def trener(id):
    t = Trener.query.get_or_404(id)
    return jsonify(t.to_dict())


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
def uredi_trenera(id):
    t = Trener.query.get_or_404(id)
    data = request.get_json()

    t.ime = data.get('ime')
    t.prezime = data.get('prezime')
    t.specijalnost_id = data.get('specijalnost_id')

    db.session.commit()
    return jsonify({"poruka": "Trener uspješno ažuriran"})


@app.route('/treneri/<id>', methods=['DELETE'])
def izbrisi_trenera(id):
    t = Trener.query.get_or_404(id)
    db.session.delete(t)
    db.session.commit()
    return jsonify({"poruka": "Trener obrisan"})


@app.route('/treninzi', methods=['GET'])
def treninzi():
    svi_treninzi = Trening.query.all()
    return jsonify([t.to_dict() for t in svi_treninzi])


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
        trener_id=data.get('trener_id')
    )
    db.session.add(novi)
    db.session.commit()
    return jsonify({"poruka": "Trening dodan"}), 201

@app.route('/treninzi/<id>', methods=['PUT'])
def uredi_trening(id):
    t = Trening.query.get_or_404(id)
    data = request.get_json()
    t.naziv = data.get('naziv')
    t.opis = data.get('opis')
    t.dan_u_tjednu = data.get('dan_u_tjednu')
    t.vrijeme_pocetka = data.get('vrijeme_pocetka')
    t.vrijeme_kraja = data.get('vrijeme_kraja')
    t.kapacitet = data.get('kapacitet')
    t.trener_id = data.get('trener_id')
    db.session.commit()
    return jsonify({"poruka": "Trening uređen"})


@app.route('/treninzi/<id>', methods=['DELETE'])
def izbrisi_trening(id):
    t = Trening.query.get_or_404(id)
    db.session.delete(t)
    db.session.commit()
    return jsonify({"poruka": "Trening obrisan"})


@app.route('/specijalnosti', methods=['GET'])
def specijalnosti():
    sve = Specijalnost.query.all()
    return jsonify([s.to_dict() for s in sve])


if __name__ == "__main__":
    app.run(debug=True, port=5000)