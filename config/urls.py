from django.contrib import admin
from django.urls import path, include
from patches import routers
from users.urls import users_router


router = routers.DefaultRouter()
router.extend(users_router)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include(router.urls)),
]
