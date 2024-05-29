from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    qte = models.PositiveIntegerField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('rejected', 'Rejected'),
        ('confirmed', 'Confirmed'),
    ]
    
    client_name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    telephone = models.CharField(max_length=15)
    email = models.EmailField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qte = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Order {self.id} by {self.client_name}"
