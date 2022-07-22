from django.core.management.base import BaseCommand
from rooms import models as models_room


class Command(BaseCommand):

    help = "This command creates facilities"

    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for f in facilities:
            models_room.Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"len(facilities) created!"))
