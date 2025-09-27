"""Django models for the application."""

# Uncomment the following imports before adding the Model code
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class CarMake(models.Model):
    """Car make entity (e.g., Toyota, Ford)."""

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    country = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    """Car model entity linked to a car make."""

    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name="car_models")
    dealer_id = models.IntegerField(help_text="External dealer identifier")
    name = models.CharField(max_length=100)

    CAR_TYPES = [
        ("SEDAN", "Sedan"),
        ("SUV", "SUV"),
        ("WAGON", "Wagon"),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default="SUV")
    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015),
        ],
    )
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.car_make.name} {self.name}"
