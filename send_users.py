from faker import Faker
from application import init_app
from application.database import db, User

app = init_app()

def create_faker_users():
    faker = Faker('en')
    Faker.seed(4321)
    user_list = []
    number_of_users = 6

    with app.app_context():
        for _ in range(number_of_users):
            user = User(
                name=faker.name(),
                password=faker.password(),
                email=faker.email(),
                phone=faker.phone_number(),
                address=faker.address()
            )
            user_list.append(user)

        db.session.add_all(user_list)
        db.session.commit()
        print(f"{number_of_users} users added successfully.")

if __name__ == "__main__":
    create_faker_users()
