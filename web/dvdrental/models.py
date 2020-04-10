# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Actor(models.Model):
    actor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'actor'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class ActorInfo(models.Model):
    actor_id = models.IntegerField(blank=True, primary_key=True)
    first_name = models.CharField(max_length=45, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    film_info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'actor_info'


class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=20)
    city = models.ForeignKey('City', models.PROTECT)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=20)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'address'


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'category'

    def __str__(self):
        return self.name


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=50)
    country = models.ForeignKey('Country', models.PROTECT)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'city'


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=50)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'country'

    def __str__(self):
        return self.country


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    store_id = models.SmallIntegerField()
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=50, blank=True, null=True)
    address = models.ForeignKey(Address, models.PROTECT)
    active_bool = models.BooleanField()
    create_date = models.DateField()
    last_update = models.DateTimeField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'customer'


class CustomerList(models.Model):
    id = models.IntegerField(blank=True, primary_key=True)
    name = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.CharField(db_column='zip code', max_length=10, blank=True,
                                null=True)  # Field renamed to remove unsuitable characters.
    phone = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    sid = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'customer_list'


class Film(models.Model):
    film_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True)
    language = models.ForeignKey('Language', models.PROTECT)
    rental_duration = models.SmallIntegerField()
    rental_rate = models.DecimalField(max_digits=4, decimal_places=2)
    length = models.SmallIntegerField(blank=True, null=True)
    replacement_cost = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.TextField(blank=True, null=True)  # This field type is a guess.
    last_update = models.DateTimeField(auto_now=True)
    special_features = models.TextField(blank=True, null=True)  # This field type is a guess.
    fulltext = models.TextField()  # This field type is a guess.
    categories = models.ManyToManyField('Category', through='FilmCategory')
    actors = models.ManyToManyField('Actor', through='FilmActor')

    class Meta:
        managed = True
        db_table = 'film'

    def __str__(self):
        return self.title


class FilmActor(models.Model):
    film_actor_id = models.AutoField(primary_key=True)
    actor = models.OneToOneField(Actor, on_delete=models.PROTECT)
    film = models.OneToOneField(Film, models.PROTECT)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'film_actor'
        unique_together = (('film', 'actor'),)


class FilmCategory(models.Model):
    film_category_id = models.AutoField(primary_key=True)
    film = models.OneToOneField(Film, models.PROTECT)
    category = models.OneToOneField(Category, models.PROTECT)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'film_category'
        unique_together = (('film', 'category'),)


class FilmList(models.Model):
    fid = models.IntegerField(blank=True, primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=25, blank=True, null=True)
    price = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    length = models.SmallIntegerField(blank=True, null=True)
    rating = models.TextField(blank=True, null=True)  # This field type is a guess.
    actors = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'film_list'


class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    film = models.ForeignKey(Film, models.PROTECT)
    store_id = models.SmallIntegerField()
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'inventory'


class Language(models.Model):
    language_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'language'

    def __str__(self):
        return self.name


class NicerButSlowerFilmList(models.Model):
    fid = models.IntegerField(blank=True, primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=25, blank=True, null=True)
    price = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    length = models.SmallIntegerField(blank=True, null=True)
    rating = models.TextField(blank=True, null=True)  # This field type is a guess.
    actors = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'nicer_but_slower_film_list'


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, models.PROTECT)
    staff = models.ForeignKey('Staff', models.PROTECT)
    rental = models.ForeignKey('Rental', models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    payment_date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'payment'


class Rental(models.Model):
    rental_id = models.AutoField(primary_key=True)
    rental_date = models.DateTimeField()
    inventory = models.OneToOneField(Inventory, models.PROTECT)
    customer = models.OneToOneField(Customer, models.PROTECT)
    return_date = models.DateTimeField(blank=True, null=True)
    staff = models.ForeignKey('Staff', models.PROTECT)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'rental'
        unique_together = (('rental_date', 'inventory', 'customer'),)


class SalesByFilmCategory(models.Model):
    category = models.CharField(max_length=25, blank=True, primary_key=True)
    total_sales = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'sales_by_film_category'


class SalesByStore(models.Model):
    store = models.TextField(blank=True, primary_key=True)
    manager = models.TextField(blank=True, null=True)
    total_sales = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'sales_by_store'


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    address = models.ForeignKey(Address, models.PROTECT)
    email = models.CharField(max_length=50, blank=True, null=True)
    store_id = models.SmallIntegerField()
    active = models.BooleanField()
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=40, blank=True, null=True)
    last_update = models.DateTimeField(auto_now=True)
    picture = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'staff'


class StaffList(models.Model):
    id = models.IntegerField(blank=True, primary_key=True)
    name = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.CharField(db_column='zip code', max_length=10, blank=True,
                                null=True)  # Field renamed to remove unsuitable characters.
    phone = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    sid = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'staff_list'


class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    manager_staff = models.OneToOneField(Staff, models.PROTECT)
    address = models.ForeignKey(Address, models.PROTECT)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'store'
