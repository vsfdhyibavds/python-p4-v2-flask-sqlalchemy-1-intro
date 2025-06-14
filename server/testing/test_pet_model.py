from server.app import app
from server.models import db, Pet

def test_pet_model():
    with app.app_context():
        # Create all tables
        db.create_all()

        # Create a new pet
        new_pet = Pet(name='Fido', species='Dog')
        db.session.add(new_pet)
        db.session.commit()

        # Query the pet
        pet = Pet.query.filter_by(name='Fido').first()
        if pet:
            print(f"Pet found: id={pet.id}, name={pet.name}, species={pet.species}")
        else:
            print("Pet not found")

        # Update the pet's species
        if pet:
            pet.species = 'Canine'
            db.session.commit()
            print(f"Pet updated: id={pet.id}, name={pet.name}, species={pet.species}")

        # Delete the pet
        if pet:
            db.session.delete(pet)
            db.session.commit()
            print(f"Pet deleted: id={pet.id}")

        # Query deleted pet to confirm deletion
        deleted_pet = Pet.query.filter_by(name='Fido').first()
        if deleted_pet:
            print("Delete failed: Pet still found")
        else:
            print("Delete confirmed: Pet not found")

        # Test querying a non-existent pet
        non_existent_pet = Pet.query.filter_by(name='NonExistent').first()
        if non_existent_pet is None:
            print("Query for non-existent pet returned None as expected")
        else:
            print("Unexpected result for non-existent pet query")

        # Clean up by dropping all tables
        db.drop_all()

if __name__ == '__main__':
    test_pet_model()
