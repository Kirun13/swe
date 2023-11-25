from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

class Base(DeclarativeBase):
    pass

class The_User(Base):
    __tablename__ = "the_user"
    user_id:Mapped[int] = mapped_column(primary_key=True)
    user_role:Mapped[str] = mapped_column(nullable=False)
    givenname:Mapped[str] = mapped_column(nullable=False)
    surname:Mapped[str] = mapped_column(nullable=False)
    middle_name:Mapped[str] = mapped_column()
    phone:Mapped[str] = mapped_column()
    email:Mapped[str] = mapped_column(unique=True, nullable=False)
    address:Mapped[str] = mapped_column()
    the_password:Mapped[str] = mapped_column(nullable=False)
    username:Mapped[str] = mapped_column()
    salt:Mapped[str] = mapped_column()
    government_id:Mapped[str] = mapped_column()



class The_Admin(Base):
    __tablename__ = "the_admin"
    admin_id:Mapped[int] = mapped_column(ForeignKey('the_user.user_id'), nullable=False, primary_key=True)
    user:Mapped[int] = mapped_column(primary_key=True)
    user = relationship("The_User", uselist=False)


class MaintenancePerson(Base):
    __tablename__ = "maintenance_person"
    maintenance_person_id:Mapped[int] = mapped_column(ForeignKey('the_user.user_id'), nullable=False, primary_key=True)
    user = relationship("The_User", uselist=False)


class Driver(Base):
    __tablename__ = "driver"
    driver_id:Mapped[int] = mapped_column(ForeignKey('the_user.user_id'), nullable=False, primary_key=True)
    user = relationship("The_User", uselist=False)


class FuelingPerson(Base):
    __tablename__ = "fueling_person"
    fueling_person_id:Mapped[int] = mapped_column(ForeignKey('the_user.user_id'), nullable=False, primary_key=True)
    user = relationship("The_User", uselist=False)