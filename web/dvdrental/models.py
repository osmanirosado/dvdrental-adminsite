# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Language(models.Model):
    language_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'
        managed = True
        db_table = 'language'

    def __str__(self):
        return self.name


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        managed = True
        db_table = 'category'

    def __str__(self):
        return self.name


class Actor(models.Model):
    actor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Actor'
        verbose_name_plural = 'Actors'
        managed = True
        db_table = 'actor'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Film(models.Model):
    RATING_G = 'G'
    RATING_PG = 'PG'
    RATING_PG_13 = 'PG-13'
    RATING_R = 'R'
    RATING_NC_17 = 'NC-17'

    RATING_VALUES = (
        # name, value
        (RATING_G, RATING_G),
        (RATING_PG, RATING_PG),
        (RATING_R, RATING_R),
        (RATING_NC_17, RATING_NC_17)
    )

    film_id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    release_year = models.PositiveSmallIntegerField(
        null=True, blank=True,
        validators=[MinValueValidator(limit_value=1901), MaxValueValidator(limit_value=2155)]
    )
    language = models.ForeignKey(to=Language, on_delete=models.PROTECT)
    rental_duration = models.PositiveSmallIntegerField(default=3, blank=True, help_text='Default value: 3')
    rental_rate = models.DecimalField(
        max_digits=4, decimal_places=2, default=4.99, blank=True, help_text='Default value: 4.99'
    )
    length = models.PositiveSmallIntegerField(null=True, blank=True)
    replacement_cost = models.DecimalField(
        max_digits=5, decimal_places=2, default=19.99, blank=True, help_text='Default value: 19.99'
    )
    rating = models.CharField(
        max_length=8, choices=RATING_VALUES, default=RATING_G, blank=True, help_text=f'Default value: {RATING_G}'
    )
    last_update = models.DateTimeField(auto_now=True)
    special_features = ArrayField(base_field=models.TextField(), null=True, blank=True)
    fulltext = models.TextField()  # This field type is a guess.

    actors = models.ManyToManyField(to=Actor, through='FilmActor')
    categories = models.ManyToManyField(to=Category, through='FilmCategory')

    class Meta:
        verbose_name = 'Film'
        verbose_name_plural = 'Films'
        managed = True
        db_table = 'film'

    def __str__(self):
        return f'{self.title}, {self.release_year}' if self.release_year else self.title


class FilmActor(models.Model):
    film_actor_id = models.AutoField(primary_key=True)
    actor = models.ForeignKey(to=Actor, on_delete=models.PROTECT)
    film = models.ForeignKey(to=Film, on_delete=models.PROTECT)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'film_actor'
        unique_together = (('film', 'actor'),)


class FilmCategory(models.Model):
    film_category_id = models.AutoField(primary_key=True)
    film = models.ForeignKey(to=Film, on_delete=models.PROTECT)
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'film_category'
        unique_together = (('film', 'category'),)


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=50)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        managed = True
        db_table = 'country'

    def __str__(self):
        return self.country


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=50)
    country = models.ForeignKey(to=Country, on_delete=models.PROTECT)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        managed = True
        db_table = 'city'

    def __str__(self):
        return self.city


class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=20)
    city = models.ForeignKey(to=City, on_delete=models.PROTECT)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=20)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
        managed = True
        db_table = 'address'

    def __str__(self):
        return f'{self.address}, {self.district}'


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    store_id = models.SmallIntegerField()
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=50, blank=True, null=True)
    address = models.ForeignKey(to=Address, on_delete=models.PROTECT)
    active_bool = models.BooleanField(default=True, blank=True, help_text='Default: True')
    create_date = models.DateField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    active = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        managed = True
        db_table = 'customer'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    address = models.ForeignKey(to=Address, on_delete=models.PROTECT)
    email = models.EmailField(max_length=50, blank=True, null=True)
    store_id = models.SmallIntegerField()
    active = models.BooleanField(default=True, help_text='Default: True')
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=40, blank=True, null=True)
    last_update = models.DateTimeField(auto_now=True)
    picture = models.BinaryField(blank=True, null=True)

    class Meta:
        verbose_name = 'Staff'
        verbose_name_plural = 'Staff'
        managed = True
        db_table = 'staff'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    film = models.ForeignKey(to=Film, on_delete=models.PROTECT)
    store_id = models.SmallIntegerField()
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Inventory'
        verbose_name_plural = 'Inventory'
        managed = True
        db_table = 'inventory'


class Rental(models.Model):
    rental_id = models.AutoField(primary_key=True)
    rental_date = models.DateTimeField()
    inventory = models.ForeignKey(to=Inventory, on_delete=models.PROTECT)
    customer = models.ForeignKey(to=Customer, on_delete=models.PROTECT)
    return_date = models.DateTimeField(blank=True, null=True)
    staff = models.ForeignKey(to=Staff, on_delete=models.PROTECT)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Rental'
        verbose_name_plural = 'Rental'
        managed = True
        db_table = 'rental'
        unique_together = (('rental_date', 'inventory', 'customer'),)


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(to=Customer, on_delete=models.PROTECT)
    staff = models.ForeignKey(to=Staff, on_delete=models.PROTECT)
    rental = models.ForeignKey(to=Rental, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    payment_date = models.DateTimeField()

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
        managed = True
        db_table = 'payment'


class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    manager_staff = models.OneToOneField(to=Staff, on_delete=models.PROTECT)
    address = models.ForeignKey(to=Address, on_delete=models.PROTECT)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'
        managed = True
        db_table = 'store'
