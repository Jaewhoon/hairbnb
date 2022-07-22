import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django_seed import Seed
from reservations import models as models_reservation
from rooms import models as models_room
from users import models as models_user


class Command(BaseCommand):

    help = "This command creates many reservations"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help="How many reservations do you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_guests = models_user.User.objects.all()
        all_rooms = models_room.Room.objects.all()
        seeder.add_entity(
            models_reservation.Reservation,
            number,
            {
                "status": lambda x: random.choice(["pending", "confirmed", "canceled"]),
                "guest": lambda x: random.choice(all_guests),
                "room": lambda x: random.choice(all_rooms),
                "check_in": lambda x: datetime.now()
                - timedelta(days=random.randint(-2, 2)),
                "check_out": lambda x: datetime.now()
                + timedelta(days=random.randint(3, 25)),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} reservations created!"))
