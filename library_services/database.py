# -*- coding: utf-8 -*-
from library_services import app, db
from library_services.models import User, Book, Log, Role

app_ctx = app.app_context()
app_ctx.push()
db.create_all()
Role.insert_roles()

admin = User(name=u'darek', email=u'darek@gmail.com', password=u'password', major=u'administrator',
             headline=u"Nazywam się Darek", about_me=u"Jestem ownerem tej biblioteki.")
user1 = User(name=u'Janusz', email=u'james@Gmail.com', password=u'123456', major=u'Informatyka', headline=u"Zwykły user")
user2 = User(name=u'test', email=u'test@test.com', password=u'123456')
user3 = User(name=u'test2', email=u'test2@test.com', password=u'123456')
user4 = User(name=u'test3', email=u'test3@test.com', password=u'123456')

book1 = Book(title=u"Sezon Burz", subtitle=u"Cykl wiedźmiński", author=u"Andrzej Sapkowski", isbn='9782811212995',
             tags_string=u"Fantasy", image='C:\\Users\\Dariusz Marczewski\\PycharmProjects\\Biblioteka_Mikroserwisy\\app\\static\\img\\sezon_burz.jpg',
             summary=u"""
# Akcja powieści rozgrywa się w świecie wiedźmińskim, w którym osadzona jest również fabuła Sagi o wiedźminie tego samego autora. Głównym miejscem, w którym rozgrywa się akcja jest królestwo Kerack oraz okoliczne ziemie.

* Głównym bohaterem powieści jest wiedźmin Geralt z Rivii – najemny łowca potworów, za młodu poddany morderczemu treningowi i mutacjom w wiedźmińskiej warowni Kaer Morhen.
* Ze względu na swoją odmienność (zmiany wyglądu spowodowane mutacją), jest traktowany przez społeczeństwo w najlepszym wypadku jako zło konieczne.
""")
book2 = Book(title=u"Krew elfów", subtitle=u"Saga o wiedźminie", author=u"Andrzej Sapkowski", isbn='9788025905340',
             tags_string=u"fantasy", image='C:\\Users\\Dariusz Marczewski\\PycharmProjects\\Biblioteka_Mikroserwisy\\app\\static\\img\\krew_elfow.jpg',
             summary=u"""
# Akcja powieści rozgrywa się – wedle określenia samego autora – w quasi-średniowiecznej allotopii i jest kontynuacją wcześniejszych opowiadań.

* Głównymi bohaterami powieści są Geralt z Rivii, wiedźmin, zawodowo trudniący się zabijaniem groźnych dla ludzi potworów,
* oraz królewna Ciri, nastoletnia dziewczyna, która w wyniku wojny utraciła rodzinę i tron.
""")
book3 = Book(title=u"Czas pogardy", subtitle=u"Saga o wiedźminie", author=u"Andrzej Sapkowski", isbn='9788498890532',
             tags_string=u"fantasy", image='C:\\Users\\Dariusz Marczewski\\PycharmProjects\\Biblioteka_Mikroserwisy\\app\\static\\img\\czas_pogardy.jpg',
             summary=u"""
# Geralt w mieście Dorian spotyka się ze Codringherem, prywatnym detektywem i specjalistą od wszelkiej czarnej roboty, którego najął celem zdobycia informacji o czarowniku imieniem Rience.

* Czarodziejka Yennefer wraz z Ciri jadą do Gors Velen i dalej na Wyspę Thanedd.
* W Hirundum spotykają się z Geraltem. Yennefer zamierza oddać Ciri do Szkoły Czarodziejek – Aretuzy.
""")
book4 = Book(title=u"Chrzest ognia", subtitle=u"Saga o wiedźminie", author=u"Andrzej Sapkowski", isbn='9783423407090',
             tags_string=u"fantasy", image='C:\\Users\\Dariusz Marczewski\\PycharmProjects\\Biblioteka_Mikroserwisy\\app\\static\\img\\chrzest_ognia.jpg',
             summary=u"""
# Wiedźmin Geralt po wyleczeniu się w lesie Brokilon i zaciągnięciu informacji od łuczniczki Milvy wyrusza wraz z Jaskrem, by uratować Ciri.

* Ruszają wzdłuż rzeki Wstążki na zachód w kierunku Verden. Wpadają na havekarów – kupców handlujących ze Scoia'tael, do których przybywa kilku nilfgaardzkich rycerzy.
* Dochodzi do walki, w której Geraltowi i Jaskrowi z pomocą nagle nadciąga Milva.
""")
book5 = Book(title=u"Wieża Jaskółki", subtitle=u"Saga o wiedźminie", author=u"Andrzej Sapkowski", isbn='9783423247863',
             tags_string=u"fantasy", image='C:\\Users\\Dariusz Marczewski\\PycharmProjects\\Biblioteka_Mikroserwisy\\app\\static\\img\\wieza_jaskolki.jpg',
             summary=u"""
# Ranna i ledwo żywa Ciri zostaje odnaleziona na bagnach Pereplutu przez pustelnika Vysogotę z Corvo, który zaczyna się nią opiekować.

* Między młodą dziewczyną i starym wykładowcą oxenfurckiej uczelni stopniowo nawiązuje się przyjaźń.
* Cirilla postanawia opowiedzieć mu swoją historię.
""")
book6 = Book(title=u"Pani Jeziora", subtitle=u"Saga o wiedźminie", author=u"Andrzej Sapkowski", isbn='9781473211605',
             tags_string=u"fantasy", image='C:\\Users\\Dariusz Marczewski\\PycharmProjects\\Biblioteka_Mikroserwisy\\app\\static\\img\\pani_jeziora.jpg',
             summary=u"""
# Ciri dostaje się do władanego przez Auberona królestwa Aen Elle – Ludu Olch, po którym jej przewodnikiem staje się elf Avallac'h.

* Wiedźmińska drużyna opuszcza Caed Myrkvid, gdyż bytujący tam druidzi odmawiają jakiejkolwiek pomocy.
* Kompania dociera do idyllicznego księstwa Toussaint, w którym Jaskier wdaje się w powtórny romans z księżną Anną Henriettą.
""")
logs = [Log(user1, book2), Log(user1, book3), Log(user1, book4), Log(user1, book6),
        Log(user2, book1), Log(user2, book3), Log(user2, book5),
        Log(user3, book2), Log(user3, book5)]

db.session.add_all([admin, user1, user2, user3, user4, book1, book2, book3, book4, book5, book6] + logs)
db.session.commit()

app_ctx.pop()
