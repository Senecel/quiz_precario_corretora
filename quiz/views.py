from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render

from .models import Quiz, ResultadoQuiz


def home(request):
    quizzes = Quiz.objects.filter(ativo=True).order_by("-criado_em")
    return render(request, "quiz/home.html", {"quizzes": quizzes})


def registo(request):
    if request.user.is_authenticated:
        return redirect("quiz:home")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("quiz:home")
    else:
        form = UserCreationForm()
    return render(request, "registration/registo.html", {"form": form})


@login_required
def quiz_detalhe(request, quiz_id: int):
    quiz = get_object_or_404(
        Quiz.objects.prefetch_related("perguntas__opcoes"),
        pk=quiz_id,
        ativo=True,
    )
    return render(request, "quiz/quiz_detalhe.html", {"quiz": quiz})


@login_required
def quiz_resultado(request, quiz_id: int):
    quiz = get_object_or_404(
        Quiz.objects.prefetch_related("perguntas__opcoes"),
        pk=quiz_id,
        ativo=True,
    )
    if request.method != "POST":
        return redirect("quiz:quiz_detalhe", quiz_id=quiz.id)

    total = quiz.perguntas.count()
    corretas = 0
    respondidas = 0

    for pergunta in quiz.perguntas.all():
        escolha = request.POST.get(f"pergunta_{pergunta.id}")
        if not escolha:
            continue
        respondidas += 1
        if pergunta.opcoes.filter(id=escolha, correta=True).exists():
            corretas += 1

    percentagem = round((corretas / total) * 100) if total else 0
    nao_respondidas = total - respondidas

    ResultadoQuiz.objects.create(
        utilizador=request.user,
        quiz=quiz,
        total=total,
        corretas=corretas,
        respondidas=respondidas,
        percentagem=percentagem,
    )

    contexto = {
        "quiz": quiz,
        "total": total,
        "corretas": corretas,
        "respondidas": respondidas,
        "percentagem": percentagem,
        "nao_respondidas": nao_respondidas,
    }
    return render(request, "quiz/resultado.html", contexto)


@login_required
def meus_resultados(request):
    resultados = (
        ResultadoQuiz.objects.select_related("quiz")
        .filter(utilizador=request.user)
        .order_by("-criado_em")
    )
    return render(request, "quiz/meus_resultados.html", {"resultados": resultados})

# Create your views here.
