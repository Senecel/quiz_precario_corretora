from django.contrib import admin

from .models import Opcao, Pergunta, Quiz, ResultadoQuiz


class OpcaoInline(admin.TabularInline):
    model = Opcao
    extra = 2


class PerguntaAdmin(admin.ModelAdmin):
    list_display = ("enunciado", "quiz", "ordem")
    list_filter = ("quiz",)
    inlines = [OpcaoInline]


class QuizAdmin(admin.ModelAdmin):
    list_display = ("titulo", "ativo", "criado_em")
    list_filter = ("ativo",)


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Pergunta, PerguntaAdmin)
admin.site.register(ResultadoQuiz)

# Register your models here.
