from django.urls import path
from.import views
from .views import index_view, form_submit

app_name = "instagram"

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.sign_up, name="sign_up"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path ("", views.index_view, name=" profile_view"),
    path ("submit/", form_submit, name="profile_submit"),
]
