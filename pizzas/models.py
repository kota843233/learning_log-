from django.db import models

# Create your models here.

class Pizza(models.Model):
    """ピザの名前を格納する"""
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.topping}({self.pizza.name})"


