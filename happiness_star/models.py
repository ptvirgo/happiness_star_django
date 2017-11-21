from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


def one_to_five(number):

    if number < 1 or number > 5:
        raise ValidationError('Must be between 1 and 5')


class Star(models.Model):

    class Meta:
        unique_together = ('user', 'date')

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    date = models.DateField()

    spirit = models.IntegerField(validators=[one_to_five])
    exercise = models.IntegerField(validators=[one_to_five])
    work = models.IntegerField(validators=[one_to_five])
    play = models.IntegerField(validators=[one_to_five])
    friends = models.IntegerField(validators=[one_to_five])
    adventure = models.IntegerField(
        'romance / adventure', validators=[one_to_five])

    def overall(self):
        return (self.spirit + self.exercise + self.play + self.work +
                self.friends + self.adventure) / 6.0

    def __repr__(self):
        return "<Star user=%s date=%s>" % (self.user.email,
                                           self.date.isoformat())


class Tag(models.Model):

    name = models.CharField(max_length=64, unique=True)
    star = models.ManyToManyField(Star)