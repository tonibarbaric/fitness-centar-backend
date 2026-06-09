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

        print("Dodajem specijalnosti (8)...")
        s1 = Specijalnost(naziv="Bodybuilding")
        s2 = Specijalnost(naziv="Yoga & Pilates")
        s3 = Specijalnost(naziv="Crossfit")
        s4 = Specijalnost(naziv="Kardio i mršavljenje")
        s5 = Specijalnost(naziv="Borilačke vještine")
        s6 = Specijalnost(naziv="Rehabilitacija i korekcija")
        s7 = Specijalnost(naziv="Zumba i ples")
        s8 = Specijalnost(naziv="Powerlifting")

        db.session.add_all([s1, s2, s3, s4, s5, s6, s7, s8])
        db.session.flush()

        print("Dodajem trenere (10)...")
        t1 = Trener(ime="Marko", prezime="Kraljević", specijalnost_id=s1.id)
        t2 = Trener(ime="Jelena", prezime="Rosić", specijalnost_id=s2.id)
        t3 = Trener(ime="Darko", prezime="Mišić", specijalnost_id=s3.id)
        t4 = Trener(ime="Ivana", prezime="Kovač", specijalnost_id=s4.id)
        t5 = Trener(ime="Goran", prezime="Tadić", specijalnost_id=s5.id)
        t6 = Trener(ime="Maja", prezime="Horvat", specijalnost_id=s6.id)
        t7 = Trener(ime="Ana", prezime="Zukić", specijalnost_id=s7.id)
        t8 = Trener(ime="Ivan", prezime="Petrović", specijalnost_id=s8.id)
        t9 = Trener(ime="Luka", prezime="Marić", specijalnost_id=s1.id)  # Dijeli bodybuilding
        t10 = Trener(ime="Sanja", prezime="Barić", specijalnost_id=s2.id)  # Dijeli yogu

        db.session.add_all([t1, t2, t3, t4, t5, t6, t7, t8, t9, t10])
        db.session.flush()

        print("Dodajem treninge (10)...")
        sada = datetime.now().replace(microsecond=0)

        tr1 = Trening(
            naziv="Hardcore Chest", opis="Trening prsa i tricepsa", dan_u_tjednu="Ponedjeljak",
            vrijeme_pocetka=sada + timedelta(days=1, hours=10), vrijeme_kraja=sada + timedelta(days=1, hours=11),
            kapacitet=15, trener_id=t1.id
        )
        tr2 = Trening(
            naziv="Morning Flow", opis="Lagano buđenje uz yogu", dan_u_tjednu="Srijeda",
            vrijeme_pocetka=sada + timedelta(days=3, hours=8), vrijeme_kraja=sada + timedelta(days=3, hours=9),
            kapacitet=10, trener_id=t2.id
        )
        tr3 = Trening(
            naziv="WOD 101", opis="Workout of the day - visok intenzitet", dan_u_tjednu="Petak",
            vrijeme_pocetka=sada + timedelta(days=5, hours=17), vrijeme_kraja=sada + timedelta(days=5, hours=19),
            kapacitet=20, trener_id=t3.id
        )
        tr4 = Trening(
            naziv="Fat Burner", opis="Intenzivan kardio trening za gubitak masnoća", dan_u_tjednu="Utorak",
            vrijeme_pocetka=sada + timedelta(days=2, hours=18), vrijeme_kraja=sada + timedelta(days=2, hours=19),
            kapacitet=25, trener_id=t4.id
        )
        tr5 = Trening(
            naziv="Kickbox Fit", opis="Osnove boksa i kickboksa za kondiciju", dan_u_tjednu="Četvrtak",
            vrijeme_pocetka=sada + timedelta(days=4, hours=19), vrijeme_kraja=sada + timedelta(days=4, hours=20),
            kapacitet=12, trener_id=t5.id
        )
        tr6 = Trening(
            naziv="Zdrava Kralježnica", opis="Korekcijske vježbe i istezanje", dan_u_tjednu="Subota",
            vrijeme_pocetka=sada + timedelta(days=6, hours=9), vrijeme_kraja=sada + timedelta(days=6, hours=10),
            kapacitet=8, trener_id=t6.id
        )
        tr7 = Trening(
            naziv="Zumba Party", opis="Plesni trening uz latino ritmove", dan_u_tjednu="Petak",
            vrijeme_pocetka=sada + timedelta(days=5, hours=20), vrijeme_kraja=sada + timedelta(days=5, hours=21),
            kapacitet=30, trener_id=t7.id
        )
        tr8 = Trening(
            naziv="Max Power", opis="Trening snage, čučanj i mrtvo dizanje", dan_u_tjednu="Ponedjeljak",
            vrijeme_pocetka=sada + timedelta(days=1, hours=16), vrijeme_kraja=sada + timedelta(days=1, hours=18),
            kapacitet=10, trener_id=t8.id
        )
        tr9 = Trening(
            naziv="Leg Day Hell", opis="Izgradnja mišića nogu", dan_u_tjednu="Četvrtak",
            vrijeme_pocetka=sada + timedelta(days=4, hours=11), vrijeme_kraja=sada + timedelta(days=4, hours=12),
            kapacitet=15, trener_id=t9.id
        )
        tr10 = Trening(
            naziv="Deep Pilates", opis="Jačanje core mišića i stabilnosti", dan_u_tjednu="Utorak",
            vrijeme_pocetka=sada + timedelta(days=2, hours=8), vrijeme_kraja=sada + timedelta(days=2, hours=9),
            kapacitet=12, trener_id=t10.id
        )

        db.session.add_all([tr1, tr2, tr3, tr4, tr5, tr6, tr7, tr8, tr9, tr10])

        print("Dodajem članove (40)...")
        clanovi = [
            Clan(ime="Ivan", prezime="Horvat", email="ivan.h@gmail.com"),
            Clan(ime="Petra", prezime="Marić", email="petra.m@yahoo.com"),
            Clan(ime="Luka", prezime="Babić", email="luka.b@outlook.com"),
            Clan(ime="Marija", prezime="Kovačević", email="marija.k@gmail.com"),
            Clan(ime="Stjepan", prezime="Filipović", email="stjepan.f@net.hr"),
            Clan(ime="Elena", prezime="Tomarić", email="elena.t@gmail.com"),
            Clan(ime="Tomislav", prezime="Kralj", email="tomislav.k@yahoo.com"),
            Clan(ime="Ana", prezime="Vidović", email="ana.v@outlook.com"),
            Clan(ime="Karlo", prezime="Jurić", email="karlo.j@gmail.com"),
            Clan(ime="Martina", prezime="Pavlović", email="martina.p@net.hr"),
            Clan(ime="Josip", prezime="Blažević", email="josip.b@gmail.com"),
            Clan(ime="Nika", prezime="Kosić", email="nika.k@yahoo.com"),
            Clan(ime="Filip", prezime="Lovrić", email="filip.l@outlook.com"),
            Clan(ime="Lucija", prezime="Knežević", email="lucija.k@gmail.com"),
            Clan(ime="Marko", prezime="Popović", email="marko.p@net.hr"),
            Clan(ime="Lana", prezime="Šimić", email="lana.s@gmail.com"),
            Clan(ime="David", prezime="Jukić", email="david.j@yahoo.com"),
            Clan(ime="Sara", prezime="Lončar", email="sara.l@outlook.com"),
            Clan(ime="Mateo", prezime="Vuković", email="mateo.v@gmail.com"),
            Clan(ime="Barbara", prezime="Ramić", email="barbara.r@net.hr"),
            Clan(ime="Bruno", prezime="Abramović", email="bruno.a@gmail.com"),
            Clan(ime="Mia", prezime="Puljić", email="mia.p@yahoo.com"),
            Clan(ime="Antonio", prezime="Galić", email="antonio.g@outlook.com"),
            Clan(ime="Dora", prezime="Pavić", email="dora.p@gmail.com"),
            Clan(ime="Marin", prezime="Ilić", email="marin.i@net.hr"),
            Clan(ime="Iva", prezime="Grgić", email="iva.g@gmail.com"),
            Clan(ime="Jan", prezime="Hodak", email="jan.h@yahoo.com"),
            Clan(ime="Katarina", prezime="Zeba", email="katarina.z@outlook.com"),
            Clan(ime="Patrik", prezime="Burić", email="patrik.b@gmail.com"),
            Clan(ime="Tea", prezime="Milas", email="tea.m@net.hr"),
            Clan(ime="Viktor", prezime="Barišić", email="viktor.b@gmail.com"),
            Clan(ime="Ema", prezime="Radić", email="ema.r@yahoo.com"),
            Clan(ime="Sven", prezime="Perić", email="sven.p@outlook.com"),
            Clan(ime="Laura", prezime="Nikolić", email="laura.n@gmail.com"),
            Clan(ime="Robert", prezime="Sever", email="robert.s@net.hr"),
            Clan(ime="Klara", prezime="Matić", email="klara.m@gmail.com"),
            Clan(ime="Leon", prezime="Novak", email="leon.n@yahoo.com"),
            Clan(ime="Nina", prezime="Kovačić", email="nina.k@outlook.com"),
            Clan(ime="Borist", prezime="Grabar", email="boris.g@gmail.com"),
            Clan(ime="Tena", prezime="Kranjčar", email="tena.k@net.hr")
        ]

        db.session.add_all(clanovi)

        db.session.commit()

if __name__ == "__main__":
    seed_data()