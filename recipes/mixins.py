from django.contrib.auth.mixins import AccessMixin

from .models import Recipe


class RecipeAuthorOnlyMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        slug = kwargs.get("slug")
        user = request.user
        try:
            Recipe.objects.get(slug=slug, author=user)
            return super().dispatch(request, *args, **kwargs)
        except Recipe.DoesNotExist:
            return self.handle_no_permission()
