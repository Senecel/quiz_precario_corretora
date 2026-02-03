from django.conf import settings
from django.db import models


class Quiz(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.titulo


class Pergunta(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="perguntas")
    enunciado = models.CharField(max_length=300)
    ordem = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["ordem", "id"]

    def __str__(self) -> str:
        return self.enunciado


class Opcao(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, related_name="opcoes")
    texto = models.CharField(max_length=200)
    correta = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.texto


class ResultadoQuiz(models.Model):
    utilizador = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="resultados_quiz",
    )
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="resultados")
    total = models.PositiveIntegerField()
    corretas = models.PositiveIntegerField()
    respondidas = models.PositiveIntegerField()
    percentagem = models.PositiveIntegerField()
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-criado_em", "-id"]

    def __str__(self) -> str:
        return f"{self.utilizador} - {self.quiz} ({self.percentagem}%)"

# Create your models here.
