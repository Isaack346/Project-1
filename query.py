# from app import db, Product
from application.database import User, db
from application import init_app

from faker import Faker

app = init_app()

def create_faker_users():
    faker = Faker('en')
    Faker.seed(4321)
    user_list = []
    number_of_users = 50

    with app.app_context():
        for i in range(number_of_users):
            user = User()
            user.name = faker.name()
            user.password = faker.password()
            user.email = faker.email()
            user.phone = faker.phone_number()
            user.address = faker.address()
            user_list.append(user)

        db.session.add_all(user_list)
        db.session.commit()

if __name__ == "__main__":

    with app.app_context():
        create_faker_users()
        # User.query.delete()
        # db.session.commit()
        for p in User.query.all():
            print(p.name, p.id)