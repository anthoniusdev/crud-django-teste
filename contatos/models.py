from django.db import models

# Create your models here.
class Contato(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    def __str__(self) -> str:
        return self.nome