from django.contrib.auth import views as auth_views
from django.urls import path

from . import views


app_name = "quiz"

urlpatterns = [
    path("", views.home, name="home"),
    path("registo/", views.registo, name="registo"),
    path(
        "entrar/",
        auth_views.LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path("sair/", auth_views.LogoutView.as_view(), name="logout"),
    path("resultados/", views.meus_resultados, name="meus_resultados"),
    path("quiz/<int:quiz_id>/", views.quiz_detalhe, name="quiz_detalhe"),
    path("quiz/<int:quiz_id>/resultado/", views.quiz_resultado, name="quiz_resultado"),
]
