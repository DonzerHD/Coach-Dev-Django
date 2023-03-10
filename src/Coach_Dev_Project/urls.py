"""Coach_Dev_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Gestion_Rendez_Vous.views import create_appointment , liste_appointment , delete_appointment , appointments_view
from .views import accueil
from Authentification.views import login_page , logout_user , create_user, liste_utilisateurs , delete_user , details_utilisateur , update_profile

"""Coach_Dev_Project URL Configuration"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accueil/', accueil, name='accueil'),
    path('', login_page, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create/', create_user, name='create_user'),
    path('liste_utilisateur/', liste_utilisateurs , name='liste_utilisateurs'),
    path('delete_user/<int:user_id>/', delete_user, name='delete_user'),
    path('details_utilisateur/<int:user_id>/', details_utilisateur, name='details_utilisateur'),
    path('rendez-vous-client/', create_appointment, name='make_appointment'),
    path('update/', update_profile, name='update'),
    path('liste_rdv/', liste_appointment, name='appointment_list'),
    path("delete_rdv/<int:appointment_id>/", delete_appointment, name="delete_appointment"),
    path("mes-rendez-vous/", appointments_view, name="appointments_view")
]


