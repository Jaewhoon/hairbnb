from django.db import models
from core import models as models_core


class Conversation(models_core.TimeStampedModel):

    """Conversation Model Definition"""

    pasticipants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        return str(self.created)


class Message(models_core.TimeStampedModel):

    """Message Model Definition"""

    message = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    conversation = models.ForeignKey("Conversation", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} says: {self.text}"
