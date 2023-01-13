from django.db import models

OPERATION_CHOICES = (
    ('add', 'add'),
    ('sub', 'sub'),
    ('mul', 'mul'),
    ('div', 'div'),
)

class Math(models.Model):
    operation = models.CharField(max_length=5, choices = OPERATION_CHOICES)
    a = models.IntegerField()
    b = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    result = models.ForeignKey(
        'maths.Result',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"id:{self.id}, a={self.a}, b={self.b}, op={self.operation}"


class Result(models.Model):
    value = models.FloatField(blank=True, null=True, unique=True)
    error = models.CharField(max_length=255, null=True, blank=True, unique=True)

    def __str__(self):
        return f"value:{self.value} | error:{self.error}"


    class Meta:   #sprawdza aby tylko jedna ze zmiennych byla wypelniona, a druga pusta
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_value_error_together",
                check=(
                    models.Q(
                        value__isnull=False,
                        error__isnull=True,
                    )
                    | models.Q(
                        value__isnull=True,
                        error__isnull=False,
                    )
                ),
            )
        ]