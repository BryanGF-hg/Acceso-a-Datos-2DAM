
from typing import Optional

from sqlalchemy import create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


# PASO 1: conectar con la base de datos SQLite
engine = create_engine("sqlite:///biblioteca.db")


# PASO 2: crear la clase Base
class Base(DeclarativeBase):
    pass


# PASO 3: definir la clase Libro
class Libro(Base):
    __tablename__ = "libros"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(nullable=False)
    autor: Mapped[str] = mapped_column(nullable=False)
    paginas: Mapped[Optional[int]] = mapped_column(nullable=True)


# PASO 4: crear la tabla
Base.metadata.create_all(engine)


# PASOS 5 A 9: trabajar dentro de una misma sesión
with Session(engine) as session:

    # PASO 5: guardar los tres libros
    libro1 = Libro(
        titulo="Don Quijote de la Mancha",
        autor="Miguel de Cervantes",
        paginas=1250
    )

    libro2 = Libro(
        titulo="La casa de los espíritus",
        autor="Isabel Allende",
        paginas=480
    )

    libro3 = Libro(
        titulo="Platero y yo",
        autor="Juan Ramón Jiménez",
        paginas=None
    )

    session.add(libro1)
    session.add(libro2)
    session.add(libro3)

    session.commit()

    # PASO 6: consultar el libro con id 1
    libro = session.get(Libro, 1)

    if libro is not None:
        print(f"{libro.titulo} - {libro.autor}")

    # Consultar libros con más de 400 páginas
    consulta = select(Libro).where(Libro.paginas > 400)

    for libro in session.scalars(consulta):
        print(libro.titulo, libro.paginas)

    # PASO 7: actualizar Platero y yo
    libro = session.get(Libro, 3)

    if libro is not None:
        libro.paginas = 150
        session.commit()

    # PASO 8: eliminar La casa de los espíritus
    libro = session.get(Libro, 2)

    if libro is not None:
        session.delete(libro)
        session.commit()

    # PASO 9: mostrar los libros restantes
    consulta = select(Libro)

    for libro in session.scalars(consulta):
        print(libro.id, libro.titulo, libro.paginas)

