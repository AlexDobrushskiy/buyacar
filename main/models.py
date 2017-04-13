from django.db import models

CAR_MARKS = (('Ford', 'Ford'),
             ('Hyundai', 'Hyundai'),
             ('Chevrolet', 'Chevrolet'),
             ('Citroen', 'Citroen'),
             ('VW', 'VW'),
             ('Renault', 'Renault'),
             ('Peugeot', 'Peugeot'),
             ('Opel', 'Opel'),
             )

CAR_MODELS = (('Fusion', 'Fusion'),
              ('Solaris', 'Solaris'),
              ('Lacetti', 'Lacetti'),
              ('C4', 'C4'),
              ('Aveo', 'Aveo'),
              ('Polo', 'Polo'),
              ('Symbol', 'Symbol'),
              ('308', '308'),
              ('Cobalt', 'Cobalt'),
              ('Astra', 'Astra'),
              )

CAR_BODY_TYPES = (('Hatchback', 'Hatchback'),
                  ('Sedan', 'Sedan'),
                  ('Wagon', 'Wagon'),
                  )


# Create your models here.
class Car(models.Model):
    mark = models.CharField(choices=CAR_MARKS, max_length=255)
    model = models.CharField(choices=CAR_MODELS, max_length=255)
    body_type = models.CharField(choices=CAR_BODY_TYPES, max_length=255)
    year = models.PositiveIntegerField()
    mileage = models.PositiveIntegerField()
    number_of_owner = models.PositiveSmallIntegerField()
    announced_price = models.PositiveIntegerField()
    negotiated_price = models.PositiveIntegerField(null=True)
    phone_number = models.CharField(max_length=255, verbose_name='79200393289')
    link = models.CharField(max_length=1024)
