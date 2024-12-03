from utils.db_utils import DatabaseUtils
from faker import Faker

faker = Faker()

class DatabaseSeeder:
    @staticmethod
    def seed_users(count=10):
        """Seed the database with users."""
        for _ in range(count):
            DatabaseUtils.add_user(
                name=faker.name(),
                email=faker.email(),
                password="password123",  # Default password for seeded users
                phone=faker.phone_number(),
                address=faker.address()
            )

    @staticmethod
    def seed_products(count=10):
        """Seed the database with products."""
        for _ in range(count):
            DatabaseUtils.add_product(
                name=faker.word().capitalize(),
                description=faker.text(max_nb_chars=100),
                price=round(faker.random_number(digits=4) / 100, 2),
                stock=faker.random_int(min=10, max=100)
            )

if __name__ == "__main__":
    print("Seeding the database...")
    DatabaseSeeder.seed_users()
    DatabaseSeeder.seed_products()
    print("Database seeding complete.")

