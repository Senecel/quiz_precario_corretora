from django.test import TestCase
from django.urls import reverse

from .models import Opcao, Pergunta, Quiz


class QuizViewsTests(TestCase):
    def _criar_quiz_com_perguntas(self) -> Quiz:
        quiz = Quiz.objects.create(titulo="Quiz de Teste", descricao="Desc", ativo=True)
        pergunta_1 = Pergunta.objects.create(quiz=quiz, enunciado="Pergunta 1", ordem=1)
        pergunta_2 = Pergunta.objects.create(quiz=quiz, enunciado="Pergunta 2", ordem=2)
        Opcao.objects.create(pergunta=pergunta_1, texto="Opção 1", correta=True)
        Opcao.objects.create(pergunta=pergunta_1, texto="Opção 2", correta=False)
        Opcao.objects.create(pergunta=pergunta_2, texto="Opção 1", correta=False)
        Opcao.objects.create(pergunta=pergunta_2, texto="Opção 2", correta=True)
        return quiz

    def test_home_lista_quizzes_ativos(self) -> None:
        Quiz.objects.create(titulo="Quiz Ativo", ativo=True)
        Quiz.objects.create(titulo="Quiz Inativo", ativo=False)

        response = self.client.get(reverse("quiz:home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Quiz Ativo")
        self.assertNotContains(response, "Quiz Inativo")

    def test_quiz_resultado_calcula_percentagem(self) -> None:
        quiz = self._criar_quiz_com_perguntas()
        perguntas = list(quiz.perguntas.all())
        primeira_opcao = perguntas[0].opcoes.filter(correta=True).first()
        segunda_opcao = perguntas[1].opcoes.filter(correta=False).first()

        response = self.client.post(
            reverse("quiz:quiz_resultado", kwargs={"quiz_id": quiz.id}),
            {
                f"pergunta_{perguntas[0].id}": str(primeira_opcao.id),
                f"pergunta_{perguntas[1].id}": str(segunda_opcao.id),
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["total"], 2)
        self.assertEqual(response.context["corretas"], 1)
        self.assertEqual(response.context["respondidas"], 2)
        self.assertEqual(response.context["percentagem"], 50)
