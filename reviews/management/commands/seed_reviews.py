import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from reviews import models as models_review
from users import models as models_user
from rooms import models as models_room


class Command(BaseCommand):

    help = "This command creates reviews"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help="How many reviews do you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = models_user.User.objects.all()
        all_rooms = models_room.Room.objects.all()
        seeder.add_entity(
            models_review.Review,
            number,
            {
                "user": lambda x: random.choice(all_users),
                "room": lambda x: random.choice(all_rooms),
                "cleanliness": lambda x: random.randint(1, 5),
                "accuracy": lambda x: random.randint(1, 5),
                "communication": lambda x: random.randint(1, 5),
                "location": lambda x: random.randint(1, 5),
                "check_in": lambda x: random.randint(1, 5),
                "value": lambda x: random.randint(1, 5),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} reviews created!"))
