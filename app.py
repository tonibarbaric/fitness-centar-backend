from flask import Flask, jsonify, request
from extensions import db, migrate
from models import db, Clan, Trener, Trening, Specijalnost
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



@app.route('/treneri', methods=['GET'])
def treneri():
    stranica = request.args.get('page', 1, type=int)
    po_stranici = request.args.get('per_page', 5, type=int)
    paginirani = Trener.query.paginate(page=stranica, per_page=po_stranici, error_out=False)

    return jsonify({
        "podaci": [t.to_dict() for t in paginirani.items],
        "ukupno_stranica": paginirani.pages,
        "trenutna_stranica": paginirani.page
    })


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
def azuriraj_trenera(id):
    t = Trener.query.get_or_404(id)
    data = request.get_json()

    t.ime = data.get('ime', t.ime)
    t.prezime = data.get('prezime', t.prezime)
    t.specijalnost_id = data.get('specijalnost_id', t.specijalnost_id)

    db.session.commit()
    return jsonify({"poruka": "Trener ažuriran"})


@app.route('/treneri/<id>', methods=['DELETE'])
def izbrisi_trenera(id):
    t = Trener.query.get_or_404(id)
    db.session.delete(t)
    db.session.commit()
    return jsonify({"poruka": "Trener obrisan"})



@app.route('/clanovi', methods=['GET'])
def clanovi():
    stranica = request.args.get('page', 1, type=int)
    po_stranici = request.args.get('per_page', 5, type=int)
    paginirani = Clan.query.paginate(page=stranica, per_page=po_stranici, error_out=False)

    return jsonify({
        "podaci": [c.to_dict() for c in paginirani.items],
        "ukupno_stranica": paginirani.pages,
        "trenutna_stranica": paginirani.page
    })


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
    return jsonify({"poruka": "Clan dodan"}), 201


@app.route('/clanovi/<id>', methods=['PUT'])
def azuriraj_clana(id):
    c = Clan.query.get_or_404(id)
    data = request.get_json()

    c.ime = data.get('ime', c.ime)
    c.prezime = data.get('prezime', c.prezime)
    c.email = data.get('email', c.email)

    db.session.commit()
    return jsonify({"poruka": "Clan ažuriran"})


@app.route('/clanovi/<id>', methods=['DELETE'])
def izbrisi_clana(id):
    c = Clan.query.get_or_404(id)
    db.session.delete(c)
    db.session.commit()
    return jsonify({"poruka": "Clan obrisan"})



@app.route('/treninzi', methods=['GET'])
def treninzi():
    stranica = request.args.get('page', 1, type=int)
    po_stranici = request.args.get('per_page', 5, type=int)
    paginirani = Trening.query.paginate(page=stranica, per_page=po_stranici, error_out=False)

    return jsonify({
        "podaci": [t.to_dict() for t in paginirani.items],
        "ukupno_stranica": paginirani.pages,
        "trenutna_stranica": paginirani.page
    })


@app.route('/treninzi/<id>', methods=['GET'])
def trening(id):
    t = Trening.query.get_or_404(id)
    return jsonify(t.to_dict())


@app.route('/treninzi', methods=['POST'])
def dodaj_trening():
    data = request.get_json()
    vrijeme_pocetka_str = data.get('vrijeme_pocetka')
    vrijeme_kraja_str = data.get('vrijeme_kraja')

    novi = Trening(
        naziv=data.get('naziv'),
        opis=data.get('opis'),
        dan_u_tjednu=data.get('dan_u_tjednu'),
        vrijeme_pocetka=datetime.fromisoformat(vrijeme_pocetka_str) if vrijeme_pocetka_str else None,
        vrijeme_kraja=datetime.fromisoformat(vrijeme_kraja_str) if vrijeme_kraja_str else None,
        kapacitet=data.get('kapacitet'),
        trener_id=data.get('trener_id')
    )
    db.session.add(novi)
    db.session.commit()
    return jsonify({"poruka": "Trening uspješno dodan"}), 201


@app.route('/treninzi/<id>', methods=['PUT'])
def azuriraj_trening(id):
    t = Trening.query.get_or_404(id)
    data = request.get_json()

    t.naziv = data.get('naziv', t.naziv)
    t.opis = data.get('opis', t.opis)
    t.dan_u_tjednu = data.get('dan_u_tjednu', t.dan_u_tjednu)
    t.kapacitet = data.get('kapacitet', t.kapacitet)
    t.trener_id = data.get('trener_id', t.trener_id)

    if data.get('vrijeme_pocetka'):
        t.vrijeme_pocetka = datetime.fromisoformat(data.get('vrijeme_pocetka'))
    if data.get('vrijeme_kraja'):
        t.vrijeme_kraja = datetime.fromisoformat(data.get('vrijeme_kraja'))

    db.session.commit()
    return jsonify({"poruka": "Trening uspješno ažuriran"})


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


@app.route('/specijalnosti/<id>', methods=['GET'])
def specijalnost(id):
    s = Specijalnost.query.get_or_404(id)
    return jsonify(s.to_dict())


@app.route('/specijalnosti', methods=['POST'])
def dodaj_specijalnost():
    data = request.get_json()
    nova = Specijalnost(naziv=data.get('naziv'))
    db.session.add(nova)
    db.session.commit()
    return jsonify({"poruka": "Specijalnost dodana"}), 201


@app.route('/specijalnosti/<id>', methods=['PUT'])
def azuriraj_specijalnost(id):
    s = Specijalnost.query.get_or_404(id)
    data = request.get_json()
    s.naziv = data.get('naziv', s.naziv)
    db.session.commit()
    return jsonify({"poruka": "Specijalnost azurirana"})


@app.route('/specijalnosti/<id>', methods=['DELETE'])
def izbrisi_specijalnost(id):
    s = Specijalnost.query.get_or_404(id)
    db.session.delete(s)
    db.session.commit()
    return jsonify({"poruka": "Specijalnost obrisana"})


if __name__ == '__main__':
    app.run(debug=True)