import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from lists import models as models_list
from users import models as models_user
from rooms import models as models_room


class Command(BaseCommand):

    help = "This command creates lists"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help="How many lists do you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = models_user.User.objects.all()
        seeder.add_entity(
            models_list.List,
            number,
            {
                "user": lambda x: random.choice(all_users),
            },
        )
        created = seeder.execute()
        cleaned = flatten(list(created.values()))
        rooms = models_room.Room.objects.all()
        for pk in cleaned:
            list_model = models_list.List.objects.get(pk=pk)
            to_add = rooms[random.randint(0, 5) : random.randint(6, 30)]
            list_model.rooms.add(*to_add)
        self.stdout.write(self.style.SUCCESS(f"{number} lists created!"))
