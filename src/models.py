from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    last_name = db.Column(db.String(250), nullable=False)
    rol = db.Column(db.String(250), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    father_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    mother_id = db.Column(db.Integer, db.ForeignKey('person.id'))

    def __repr__(self):
        return '<Person %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            # do not serialize the password, its a security breach
        }
    def getAll():
        people = Person.query.order_by(Person.age.desc())
        people = list(map(lambda person: person.serialize(), people))
        return people
    
    def create_person(name,last_name,rol,age,father_id,mother_id):
        person = Person(name=name, last_name=last_name, rol=rol, age=age, father_id=father_id, mother_id=mother_id)
        db.session.add(person)
        db.session.commit()