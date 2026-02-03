from django.core.management.base import BaseCommand
from django.db import transaction

from quiz.models import Opcao, Pergunta, Quiz


class Command(BaseCommand):
    help = "Cria um quiz baseado no precario LT 2025."

    @transaction.atomic
    def handle(self, *args, **options):
        titulo_quiz = "Precario LT 2025"
        quiz, created = Quiz.objects.get_or_create(
            titulo=titulo_quiz,
            defaults={
                "descricao": "Perguntas baseadas no precario em vigor a 05 de Marco de 2025.",
                "ativo": True,
            },
        )

        if not created and quiz.perguntas.exists():
            self.stdout.write(self.style.WARNING("Quiz ja existe e tem perguntas."))
            return

        perguntas = [
            (
                "Qual e o valor de abertura de conta Estudante?",
                ["1 000,00", "500,00", "2 000,00", "5 000,00"],
                0,
            ),
            (
                "Qual e o valor de abertura de conta Empresa?",
                ["5 000,00", "1 000,00", "10 000,00", "25 000,00"],
                0,
            ),
            (
                "Qual e o valor de encerramento de conta?",
                ["25 000,00", "5 000,00", "10 000,00", "1 000,00"],
                0,
            ),
            (
                "Manutencao mensal de conta para cliente nao institucional?",
                ["200,00", "400,00", "600,00", "1 000,00"],
                0,
            ),
            (
                "Manutencao mensal de conta para cliente institucional?",
                ["400,00", "200,00", "600,00", "1 000,00"],
                0,
            ),
            (
                "Deposito e levantamento de valores mobiliarios junto da Cevama?",
                ["600,00", "200,00", "1 000,00", "5 000,00"],
                0,
            ),
            (
                "Transferencia com a mesma estrutura de titularidade (Titulos): percentagem?",
                ["0,15%", "0,30%", "0,40%", "0,10%"],
                0,
            ),
            (
                "Cancelamento de oferta: valor?",
                ["1 000,00", "5 000,00", "10 000,00", "25 000,00"],
                0,
            ),
            (
                "Compra e venda de valores mobiliarios no Portal do Investidor: percentagem?",
                ["0,10%", "0,15%", "0,20%", "0,05%"],
                0,
            ),
            (
                "Unidades de participacao: percentagem?",
                ["0,80%", "0,50%", "1,00%", "0,20%"],
                0,
            ),
            (
                "Pagamento de juros/dividendos: percentagem?",
                ["2%", "1%", "0,5%", "0,24%"],
                0,
            ),
            (
                "Amortizacoes e Reembolsos: percentagem?",
                ["0,24%", "2%", "0,80%", "0,15%"],
                0,
            ),
            (
                "Consultoria para Investimento Ocasional: valor?",
                ["150 000,00", "600 000,00", "1 200 000,00", "50 000,00"],
                0,
            ),
            (
                "Solicitacao de Declaracao: valor?",
                ["10 000,00", "5 000,00", "25 000,00", "1 000,00"],
                0,
            ),
            (
                "Pedido de Penhor: valor?",
                ["5 000,00", "10 000,00", "1 000,00", "25 000,00"],
                0,
            ),
        ]

        for ordem, (enunciado, opcoes, correta_idx) in enumerate(perguntas, start=1):
            pergunta = Pergunta.objects.create(quiz=quiz, enunciado=enunciado, ordem=ordem)
            for idx, texto in enumerate(opcoes):
                Opcao.objects.create(
                    pergunta=pergunta,
                    texto=texto,
                    correta=(idx == correta_idx),
                )

        self.stdout.write(self.style.SUCCESS("Quiz criado com sucesso."))
