from django.urls import path
from django.shortcuts import redirect
from django.contrib import admin
from django.urls import path, include
from . import views
from quiz.views import redirect_to_quiz

app_name = 'quiz'
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('quiz/', include('quiz.urls')),
    # path('', lambda request: redirect('quiz/', permanent=False)),
    # ex: /quiz/
    path('', views.index, name='index'),

    # ex: /quiz/5/
    path('<int:quiz_id>/', views.single_quiz, name='single_quiz'),

    # ex: /quiz/5/3/
    path('<int:quiz_id>/<int:question_id>/', views.single_question, name='single_question'),

    # ex: /quiz/5/3/vote/
    path('<int:quiz_id>/<int:question_id>/vote/', views.vote, name='vote'),

    # ex: /quiz/5/results/
    path('<int:quiz_id>/results/', views.results, name='results'),

    # ex: /quiz/create/
    path('create/', views.create_quiz, name='create_quiz'),

    # ex: /quiz/create/7/2/
    path('create/<int:quiz_id>/<int:question_id>/', views.create_question, name='create_question'),

    path('admin/', views.admin.site.urls, name='admin'),
    path('quiz/', views.include('quiz.urls'), name='quiz'),
    path('', viewsredirect_to_quiz, name='redirect_to_quiz'),
]