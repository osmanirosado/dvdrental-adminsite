from django.db import models


class ActorInfo(models.Model):
    actor_id = models.IntegerField(blank=True, primary_key=True)
    first_name = models.CharField(max_length=45, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    film_info = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Actor Info'
        verbose_name_plural = 'Actor Info List'
        managed = False  # Created from a view. Don't remove.
        db_table = 'actor_info'


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
        verbose_name = 'Customer Info'
        verbose_name_plural = 'Customer List'
        managed = False  # Created from a view. Don't remove.
        db_table = 'customer_list'


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
        verbose_name = 'Film Info'
        verbose_name_plural = 'Film List'
        managed = False  # Created from a view. Don't remove.
        db_table = 'film_list'


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
        verbose_name = 'Film Info'
        verbose_name_plural = 'Nice But Slower Film List'
        managed = False  # Created from a view. Don't remove.
        db_table = 'nicer_but_slower_film_list'


class SalesByFilmCategory(models.Model):
    category = models.CharField(max_length=25, blank=True, primary_key=True)
    total_sales = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        verbose_name = 'Film Category Sales'
        verbose_name_plural = 'Sales by Film Category'
        managed = False  # Created from a view. Don't remove.
        db_table = 'sales_by_film_category'


class SalesByStore(models.Model):
    store = models.TextField(blank=True, primary_key=True)
    manager = models.TextField(blank=True, null=True)
    total_sales = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        verbose_name = 'Store Sales'
        verbose_name_plural = 'Sales by Store'
        managed = False  # Created from a view. Don't remove.
        db_table = 'sales_by_store'


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
        verbose_name = 'Staff Info'
        verbose_name_plural = 'Staff List'
        managed = False  # Created from a view. Don't remove.
        db_table = 'staff_list'
