from . import db


class The_User(db.Model):
    __tablename__ = "the_user"
    user_id = db.Column(db.Integer, primary_key=True)
    user_role = db.Column(db.String, nullable=False)
    givenname = db.Column(db.String, nullable=False)
    surname = db.Column(db.String, nullable=False)
    middle_name = db.Column(db.String)
    phone = db.Column(db.String)
    email = db.Column(db.String, unique=True, nullable=False)
    address = db.Column(db.String)
    the_password = db.Column(db.String, nullable=False)
    username = db.Column(db.String)
    salt = db.Column(db.String)
    government_id = db.Column(db.String)


class The_Admin(db.Model):
    __tablename__ = "the_admin"
    admin_id = db.Column(
        db.Integer, db.ForeignKey("the_user.user_id"), nullable=False, primary_key=True
    )
    user = db.relationship("The_User", uselist=False)


class MaintenancePerson(db.Model):
    __tablename__ = "maintenance_person"
    maintenance_person_id = db.Column(
        db.Integer, db.ForeignKey("the_user.user_id"), nullable=False, primary_key=True
    )
    user = db.relationship("The_User", uselist=False)


class Driver(db.Model):
    __tablename__ = "driver"
    driver_id = db.Column(
        db.Integer, db.ForeignKey("the_user.user_id"), nullable=False, primary_key=True
    )
    user = db.relationship("The_User", uselist=False)


class FuelingPerson(db.Model):
    __tablename__ = "fueling_person"
    fueling_person_id = db.Column(
        db.Integer, db.ForeignKey("the_user.user_id"), nullable=False, primary_key=True
    )
    user = db.relationship("The_User", uselist=False)