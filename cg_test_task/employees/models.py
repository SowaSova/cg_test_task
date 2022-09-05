from django.db import models


class JobRelation(models.Model):
    job_title = models.CharField(max_length=40)
    supervisor = models.ForeignKey(
        "self",
        models.CASCADE,
        related_name="subordinant",
        blank=True,
        null=True,
    )


class Employee(models.Model):
    name = models.CharField(
        max_length=120,
    )
    post = models.ForeignKey(
        JobRelation, on_delete=models.DO_NOTHING, null=True
    )
    employment_date = models.DateField()
    salary = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.post} {self.name}"
