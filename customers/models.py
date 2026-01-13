from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=250,
                            blank=False,
                            null=False,
                            help_text='Naziv musterije')
    vat_id = models.IntegerField(blank=False,
                                 null=False,
                                 unique=True,
                                 help_text='Vat id broj')
    street = models.CharField(max_length=250,
                              blank=False,
                              null=False,
                              help_text='Naziv ulice')
    city = models.CharField(max_length=250,
                            blank=False,
                            null=False,
                            help_text='Ime grada')
    country = models.CharField(max_length=250,
                               blank=False,
                               null=False,
                               help_text='Ime drzave')
    
    def __str__(self):
        return f'{self.name} {self.vat_id} {self.street} {self.city} {self.country}'