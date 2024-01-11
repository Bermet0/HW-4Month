from django.db import models


class CustomerCl(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class TagCl(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return f"#{self.name}"


class ProductCl(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    tags = models.ManyToManyField(TagCl)

    def __str__(self):
        return self.name


class OrderCl(models.Model):
    STATUS_CHOICES = (
        ('На обработке', 'На обработке'),
        ('В пути', 'В пути'),
        ('Доставлено', 'Доставлено'),
    )
    product = models.ForeignKey(CustomerCl, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status
