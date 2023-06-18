from django.urls import path

from . import views

urlpatterns = [
   path('', views.home),
   path('novo_pesquisa/', views.novo_pesquisa),
   path('consultas/', views.consultas),
   path('editar_lista/<int:id>', views.editar_lista),
   path('deletar_entrevista/<int:id>', views.deletar_entrevista),
    
]


