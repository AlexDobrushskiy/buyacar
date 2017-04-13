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

CAR_BODY_TYPES = (('Sedan', 'Sedan'),
                  ('Hatchback', 'Hatchback'),
                  ('Wagon', 'Wagon'),
                  )

CAR_COLORS = (('White', 'White'),
              ('Red', 'Red'),
              ('Dark grey', 'Dark grey'),
              ('Blue', 'Blue'),
              ('Silver', 'Silver'),
              ('Silver-blue', 'Silver-blue'),
              ('Silver-beige', 'Silver-beige'),
              ('Black', 'Black'),
              )


# Create your models here.
class Car(models.Model):
    mark = models.CharField(choices=CAR_MARKS, max_length=255)
    model = models.CharField(choices=CAR_MODELS, max_length=255)
    color = models.CharField(choices=CAR_COLORS, max_length=255, null=True, blank=True)
    body_type = models.CharField(choices=CAR_BODY_TYPES, max_length=255, default=CAR_BODY_TYPES[1])
    year = models.PositiveIntegerField()
    mileage = models.PositiveIntegerField(null=True, blank=True)
    number_of_owners = models.PositiveSmallIntegerField(null=True, blank=True)
    announced_price = models.PositiveIntegerField(null=True, blank=True)
    negotiated_price = models.PositiveIntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=255, verbose_name='Phone', null=True, blank=True)
    link = models.URLField(max_length=1024)
    comment = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return '{} {} {}'.format(self.mark, self.model, self.year)
