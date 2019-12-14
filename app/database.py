from app import app, db
from app.models import User, Book, Log, Role

app_ctx = app.app_context()
app_ctx.push()
db.create_all()
Role.insert_roles()

admin = User(name=u'darek', email='darek@gmail.com', password='password', major='administrator',
             headline=u"Nazywam się Darek", about_me=u"Jestem ownerem tej biblioteki.")
user1 = User(name=u'Janusz', email='james@Gmail.com', password='123456', major='Computer Science', headline=u"Zwykły user")
user2 = User(name=u'test', email='test@test.com', password='123456')
user3 = User(name=u'test2', email='test2@test.com', password='123456')
user4 = User(name=u'test3', email='test3@test.com', password='123456')

# książki do zrobienia
book1 = Book(title=u"Zbrodnia i kara", subtitle=u"Bantam Classics", author=u"Fyodor Dostoyevski", isbn='9788897572657',
             tags_string=u"Lektura szkolna", image='C:\\Users\\Dariusz Marczewski\\PycharmProjects\\Biblioteka_Mikroserwisy\\api\\static\\img\\C&P.jpg',
             summary=u"""
# Powieść Fiodora Dostojewskiego napisana w 1866 i w tym samym roku opublikowana w odcinkach w czasopiśmie „Russkij Wiestnik”. W formie książkowej ukazała się w 1867, a w Polsce wydano ją po raz pierwszy w latach 1887–1888.

* W formie książkowej ukazała się w 1867, a w Polsce wydano ją po raz pierwszy w latach 1887–1888.
* Tematem powieści są losy byłego studenta, Rodiona Raskolnikowa, który postanawia zamordować i obrabować starą lichwiarkę.
""")
book2 = Book(title=u"Zbrodnia i kara", subtitle=u"Bantam Classics", author=u"Fyodor Dostoyevski", isbn='9788897572657',
             tags_string=u"Lektura szkolna", image='C:\\Users\\Dariusz Marczewski\\PycharmProjects\\Biblioteka_Mikroserwisy\\api\\static\\img\\C&P.jpg',
             summary=u"""
# Powieść Fiodora Dostojewskiego napisana w 1866 i w tym samym roku opublikowana w odcinkach w czasopiśmie „Russkij Wiestnik”. W formie książkowej ukazała się w 1867, a w Polsce wydano ją po raz pierwszy w latach 1887–1888.

* W formie książkowej ukazała się w 1867, a w Polsce wydano ją po raz pierwszy w latach 1887–1888.
* Tematem powieści są losy byłego studenta, Rodiona Raskolnikowa, który postanawia zamordować i obrabować starą lichwiarkę.
""")
book3 = Book(title=u"Zbrodnia i kara", subtitle=u"Bantam Classics", author=u"Fyodor Dostoyevski", isbn='9788897572657',
             tags_string=u"Lektura szkolna", image='C:\\Users\\Dariusz Marczewski\\PycharmProjects\\Biblioteka_Mikroserwisy\\api\\static\\img\\C&P.jpg',
             summary=u"""
# Powieść Fiodora Dostojewskiego napisana w 1866 i w tym samym roku opublikowana w odcinkach w czasopiśmie „Russkij Wiestnik”. W formie książkowej ukazała się w 1867, a w Polsce wydano ją po raz pierwszy w latach 1887–1888.

* W formie książkowej ukazała się w 1867, a w Polsce wydano ją po raz pierwszy w latach 1887–1888.
* Tematem powieści są losy byłego studenta, Rodiona Raskolnikowa, który postanawia zamordować i obrabować starą lichwiarkę.
""")
book4 = Book(title=u"Zbrodnia i kara", subtitle=u"Bantam Classics", author=u"Fyodor Dostoyevski", isbn='9788897572657',
             tags_string=u"Lektura szkolna", image='C:\\Users\\Dariusz Marczewski\\PycharmProjects\\Biblioteka_Mikroserwisy\\api\\static\\img\\C&P.jpg',
             summary=u"""
# Powieść Fiodora Dostojewskiego napisana w 1866 i w tym samym roku opublikowana w odcinkach w czasopiśmie „Russkij Wiestnik”. W formie książkowej ukazała się w 1867, a w Polsce wydano ją po raz pierwszy w latach 1887–1888.

* W formie książkowej ukazała się w 1867, a w Polsce wydano ją po raz pierwszy w latach 1887–1888.
* Tematem powieści są losy byłego studenta, Rodiona Raskolnikowa, który postanawia zamordować i obrabować starą lichwiarkę.
""")
book5 = Book(title=u"Zbrodnia i kara", subtitle=u"Bantam Classics", author=u"Fyodor Dostoyevski", isbn='9788897572657',
             tags_string=u"Lektura szkolna", image='C:\\Users\\Dariusz Marczewski\\PycharmProjects\\Biblioteka_Mikroserwisy\\api\\static\\img\\C&P.jpg',
             summary=u"""
# Powieść Fiodora Dostojewskiego napisana w 1866 i w tym samym roku opublikowana w odcinkach w czasopiśmie „Russkij Wiestnik”. W formie książkowej ukazała się w 1867, a w Polsce wydano ją po raz pierwszy w latach 1887–1888.

* W formie książkowej ukazała się w 1867, a w Polsce wydano ją po raz pierwszy w latach 1887–1888.
* Tematem powieści są losy byłego studenta, Rodiona Raskolnikowa, który postanawia zamordować i obrabować starą lichwiarkę.
""")
book6 = Book(title=u"Zbrodnia i kara", subtitle=u"Bantam Classics", author=u"Fyodor Dostoyevski", isbn='9788897572657',
             tags_string=u"Lektura szkolna", image='C:\\Users\\Dariusz Marczewski\\PycharmProjects\\Biblioteka_Mikroserwisy\\api\\static\\img\\C&P.jpg',
             summary=u"""
# Powieść Fiodora Dostojewskiego napisana w 1866 i w tym samym roku opublikowana w odcinkach w czasopiśmie „Russkij Wiestnik”. W formie książkowej ukazała się w 1867, a w Polsce wydano ją po raz pierwszy w latach 1887–1888.

* W formie książkowej ukazała się w 1867, a w Polsce wydano ją po raz pierwszy w latach 1887–1888.
* Tematem powieści są losy byłego studenta, Rodiona Raskolnikowa, który postanawia zamordować i obrabować starą lichwiarkę.
""")
logs = [Log(user1, book2), Log(user1, book3), Log(user1, book4), Log(user1, book6),
        Log(user2, book1), Log(user2, book3), Log(user2, book5),
        Log(user3, book2), Log(user3, book5)]

db.session.add_all([admin, user1, user2, user3, user4, book1, book2, book3, book4, book5, book6] + logs)
db.session.commit()

app_ctx.pop()
