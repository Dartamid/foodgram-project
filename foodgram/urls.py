from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from recipes.views import RecipeListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("users.urls")),
    path("", RecipeListView.as_view(), name="recipe-list"),
    path("recipes/", include("recipes.urls")),
    path("api/", include("api.urls")),
    path("account/", include("accounts.urls")),
]
