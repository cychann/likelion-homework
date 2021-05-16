from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import blog.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name="home"),
    path('blog/<int:blog_id>', blog.views.detail, name="detail"),
    path('blog/new', blog.views.new, name="new"),
    path('blog/create', blog.views.create, name="create"),
    path('blog/edit/<int:blog_id>', blog.views.edit, name="edit"),
    path('blog/update/<int:blog_id>', blog.views.update, name="update"),
    path('blog/delete/<int:blog_id>', blog.views.delete, name="delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
