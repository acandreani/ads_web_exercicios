from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///exemplo.db')

Session = sessionmaker(bind=engine)

Base = declarative_base()

from sqlalchemy import Column, String, Integer, Date



class Filmes(Base):
    __tablename__ = 'filmes'

    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    genero = Column(String)

    def __init__(self, titulo, genero):
        self.titulo = titulo
        self.genero = genero


Base.metadata.create_all(engine)


# 3 - create a new session
session = Session()

# 4 - create movies
f1 = Filmes("t1", "comedia")
f2 = Filmes("t2", "drama")
f3 = Filmes("t3", "suspense")

session.add(f1)
session.add(f2)
session.add(f3)

session.commit()
session.close()

filmes = session.query(Filmes).all()

for filme in filmes:
    print(filme.titulo,filme.genero)





