import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from rooms import models as models_room
from users import models as models_user


class Command(BaseCommand):

    help = "This command creates many rooms"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help="How many rooms do you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = models_user.User.objects.all()
        room_types = models_room.RoomType.objects.all()
        seeder.add_entity(
            models_room.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "price": lambda x: random.randint(1000, 10000000),
                "guests": lambda x: random.randint(1, 20),
                "beds": lambda x: random.randint(1, 10),
                "bedrooms": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
            },
        )
        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        amenities = models_room.Amenity.objects.all()
        facilities = models_room.Facility.objects.all()
        rules = models_room.HouseRule.objects.all()
        for pk in created_clean:
            room = models_room.Room.objects.get(pk=pk)
            for i in range(3, random.randint(10, 17)):
                models_room.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"/room_photos/{random.randint(1,32)}.webp",
                )
            for a in amenities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.amenities.add(a)
            for f in facilities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.facilities.add(f)
            for r in rules:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.house_rules.add(r)
        self.stdout.write(self.style.SUCCESS(f"{number} rooms created!"))
