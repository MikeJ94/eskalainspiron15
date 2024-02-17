from django.contrib import admin
from django.urls import path, include
from agenda import views  
from django.conf.urls.static import static
from django.conf import settings
 
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('agenda.urls')), 

    
    path('', views.index, name='index'), 
    path('all_events/', views.all_events, name='all_events'), 
    path('add_event/', views.add_event, name='add_event'), 
    path('update/', views.update, name='update'),
    path('remove/', views.remove, name='remove'),
  
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
