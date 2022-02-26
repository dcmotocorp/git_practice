from django.db import models
from django.db.models.functions import Coalesce


class manana(models.Manager):
    def with_counts(self):
        return self.annotate(
            num_responses=Coalesce(models.Count("response"), 0)
        )


class OpinionPoll(models.Model):
    question = models.CharField(max_length=200)
    objects = PollManager()

    
class Opinionchain(models.Model):
    qudffdfon = models.CharField(max_length=200)
    objectsddsfsdfs = PollManager()

 
