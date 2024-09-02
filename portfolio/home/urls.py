# home/urls.py

from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views

urlpatterns = [
    # English version
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutMeView.as_view(), name='about'),
    path('python/', views.PythonView.as_view(), name='python'),
    path('dataAnalysis/', views.DataAnalysisView.as_view(), name='dataAnalysis'),
    path('dataScience/', views.DataScienceView.as_view(), name='dataScience'),
    path('machineLearning/', views.MachineLearningView.as_view(), name='machineLearning'),
    path('deepLearning/', views.DeepLearningView.as_view(), name='deepLearning'),
    path('techSkills/', views.TechSkillsView.as_view(), name='techSkills'),
    path('certificates/', views.CertificatesView.as_view(), name='certificates'),
    
    # Spanish version
    path('spanish/', views.PrincialView.as_view(), name='inicio'),
    path('sobreMi/', views.SobreMiView.as_view(), name='sobreMi'),
    path('pythonEs/', views.PythonEsView.as_view(), name='pythonEs'),
    path('analisisDeDatos/', views.AnalisisDeDatosView.as_view(), name='analisisDeDatos'),
    path('cienciaDeDatos/', views.CienciaDeDatosView.as_view(), name='cienciaDeDatos'),
    path('aprendizajeAutomatico/', views.AprendizajeAutomaticoView.as_view(), name='aprendizajeAutomatico'),
    path('aprendizajeProfundo/', views.AprendizajeProfundoView.as_view(), name='aprendizajeProfundo'),
    path('habilidadesTecnicas/', views.HabilidadesTecnicasView.as_view(), name='habilidadesTecnicas'),
    path('certificados/', views.CertificadosView.as_view(), name='certificados'),
    
]