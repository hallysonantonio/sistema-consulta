from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.nome+ ' - ' +self.cpf
    
class Consultas(models.Model):
    cliente = models.ForeignKey(Paciente, on_delete=models.CASCADE)  
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)  

    def __str__(self): 
        return f"{self.descricao} - {self.valor}"