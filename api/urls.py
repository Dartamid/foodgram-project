from django.urls import path, include

from . import views


api_v1 = [
    path(
        "subscriptions/<int:pk>/",
        views.SubscriptionDeleteAPIView.as_view(),
        name="delete_subscriptions",
    ),
    path(
        "subscriptions/",
        views.SubscriptionCreateAPIView.as_view(),
        name="create_subscriptions",
    ),
    path(
        "favorites/<int:pk>/",
        views.FavoriteDeleteAPIView.as_view(),
        name="delete_favorites",
    ),
    path(
        "favorites/",
        views.FavoriteCreateAPIView.as_view(),
        name="create_favorites",
    ),
    path(
        "purchases/",
        views.ShoppingListCreateAPIView.as_view(),
        name="create_purchases",
    ),
    path(
        "purchases/<int:pk>/",
        views.ShoppingListDestroyAPIView.as_view(),
        name="delete_purchases",
    ),
    path(
        "ingredients/",
        views.IngredientListAPIView.as_view(),
        name="ingredients_list",
    ),
]


urlpatterns = [
    path('v1/', include(api_v1))
]