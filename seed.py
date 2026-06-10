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

        print("Dodajem specijalnosti (5)...")
        s1 = Specijalnost(naziv="Bodybuilding")
        s2 = Specijalnost(naziv="Yoga & Pilates")
        s3 = Specijalnost(naziv="Crossfit")
        s4 = Specijalnost(naziv="Kardio i mršavljenje")
        s5 = Specijalnost(naziv="Powerlifting")

        db.session.add_all([s1, s2, s3, s4, s5])
        db.session.flush()

        print("Dodajem trenere (5)...")
        t1 = Trener(ime="Marko", prezime="Kraljević", specijalnost_id=s1.id)
        t2 = Trener(ime="Jelena", prezime="Rozga", specijalnost_id=s2.id)
        t3 = Trener(ime="Ivan", prezime="Horvat", specijalnost_id=s3.id)
        t4 = Trener(ime="Ana", prezime="Kovačić", specijalnost_id=s4.id)
        t5 = Trener(ime="Stjepan", prezime="Radić", specijalnost_id=s5.id)

        db.session.add_all([t1, t2, t3, t4, t5])
        db.session.flush()

        print("Dodajem članove (10)...")
        clanovi = [
            Clan(ime="Luka", prezime="Modrić", email="luka.m@gmail.com"),
            Clan(ime="Ivan", prezime="Perišić", email="ivan.p@yahoo.com"),
            Clan(ime="Mateo", prezime="Kovačić", email="mateo.k@outlook.com"),
            Clan(ime="Borist", prezime="Grabar", email="boris.g@net.hr"),
            Clan(ime="Marija", prezime="Jurić", email="marija.j@gmail.com"),
            Clan(ime="Antonio", prezime="Galić", email="antonio.g@outlook.com"),
            Clan(ime="Dora", prezime="Pavić", email="dora.p@gmail.com"),
            Clan(ime="Marin", prezime="Ilić", email="marin.i@net.hr"),
            Clan(ime="Iva", prezime="Grgić", email="iva.g@gmail.com"),
            Clan(ime="Jan", prezime="Hodak", email="jan.h@yahoo.com")
        ]
        db.session.add_all(clanovi)

        print("Dodajem treninge (5)...")
        sada = datetime.now()

        treninzi = [
            Trening(
                naziv="Snažan Torzo",
                opis="Intenzivan trening za prsa, leđa i ramena fokusiran na hipertrofiju.",
                dan_u_tjednu="Ponedjeljak",
                vrijeme_pocetka="18:00",
                vrijeme_kraja="19:00",
                kapacitet=12,
                trener_id=t1.id
            ),
            Trening(
                naziv="Jutarnja Vinyasa Yoga",
                opis="Lagano buđenje tijela uz vježbe disanja, istezanja i fleksibilnosti.",
                dan_u_tjednu="Utorak",
                vrijeme_pocetka="08:30",
                vrijeme_kraja="09:30",
                kapacitet=15,
                trener_id=t2.id
            ),
            Trening(
                naziv="Crossfit WOD",
                opis="Workout of the Day - kombinacija olimpijskih dizanja, gimnastike i kardija.",
                dan_u_tjednu="Srijeda",
                vrijeme_pocetka="19:30",
                vrijeme_kraja="20:30",
                kapacitet=10,
                trener_id=t3.id
            ),
            Trening(
                naziv="Kardio HIIT Pakao",
                opis="Visoko intenzivni intervalni trening za maksimalno trošenje kalorija.",
                dan_u_tjednu="Četvrtak",
                vrijeme_pocetka="17:00",
                vrijeme_kraja="18:00",
                kapacitet=20,
                trener_id=t4.id
            ),
            Trening(
                naziv="Powerlifting Osnove",
                opis="Trening tehnike za čučanj, potisak s klupe i mrtvo dizanje.",
                dan_u_tjednu="Petak",
                vrijeme_pocetka="16:00",
                vrijeme_kraja="17:30",
                kapacitet=8,
                trener_id=t5.id
            )
        ]
        db.session.add_all(treninzi)

        db.session.commit()
        print("Baza podataka uspješno napunjena novim podacima!")


if __name__ == "__main__":
    seed_data()