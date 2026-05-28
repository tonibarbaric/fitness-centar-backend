from app import app, db
from models import Trener, Clan, Trening, Specijalnost
from datetime import datetime, timedelta


def seed_data():
    with app.app_context():
        Trening.query.delete()
        Trener.query.delete()
        Clan.query.delete()
        Specijalnost.query.delete()

        print("Stari podaci obrisani. Dodajem nove...")

        print("Dodajem specijalnosti...")
        s1 = Specijalnost(naziv="Bodybuilding")
        s2 = Specijalnost(naziv="Yoga & Pilates")
        s3 = Specijalnost(naziv="Crossfit")
        db.session.add_all([s1, s2, s3])
        db.session.flush()

        print("Dodajem trenere...")
        t1 = Trener(ime="Marko", prezime="Kraljević", specijalnost_id=s1.id)
        t2 = Trener(ime="Jelena", prezime="Rosić", specijalnost_id=s2.id)
        t3 = Trener(ime="Darko", prezime="Mišić", specijalnost_id=s3.id)
        db.session.add_all([t1, t2, t3])
        db.session.flush()

        print("Dodajem treninge...")
        sada = datetime.now().replace(microsecond=0)

        tr1 = Trening(
            naziv="Hardcore Chest",
            opis="Trening prsa i tricepsa",
            dan_u_tjednu="Ponedjeljak",
            vrijeme_pocetka=sada + timedelta(days=1, hours=10),
            vrijeme_kraja=sada + timedelta(days=1, hours=11),
            kapacitet=15,
            trener_id=t1.id
        )

        tr2 = Trening(
            naziv="Morning Flow",
            opis="Lagano buđenje uz yogu",
            dan_u_tjednu="Srijeda",
            vrijeme_pocetka=sada + timedelta(days=3, hours=8),
            vrijeme_kraja=sada + timedelta(days=3, hours=9),
            kapacitet=10,
            trener_id=t2.id
        )

        tr3 = Trening(
            naziv="WOD 101",
            opis="Workout of the day - visok intenzitet",
            dan_u_tjednu="Petak",
            vrijeme_pocetka=sada + timedelta(days=5, hours=17),
            vrijeme_kraja=sada + timedelta(days=5, hours=19),
            kapacitet=20,
            trener_id=t3.id
        )

        db.session.add_all([tr1, tr2, tr3])

        print("Dodajem članove...")
        c1 = Clan(ime="Ivan", prezime="Horvat", email="ivan.h@gmail.com")
        c2 = Clan(ime="Petra", prezime="Marić", email="petra.m@yahoo.com")
        c3 = Clan(ime="Luka", prezime="Babić", email="luka.b@outlook.com")
        db.session.add_all([c1, c2, c3])

        db.session.commit()
        print("Baza uspješno napunjena podacima u novoj strukturi!")


if __name__ == "__main__":
    seed_data()