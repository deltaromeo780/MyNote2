from django.urls import path   # 8 make base.html
from . import views

app_name = 'noteapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('tag/', views.tag, name='tag'),  # 11
    path('note/', views.note, name='note'),  # 13
    path('detail/<int:note_id>', views.detail, name='detail'),  # 15
    path('done/<int:note_id>', views.set_done, name='set_done'),  # 19
    path('delete/<int:note_id>', views.delete_note, name='delete'),  # 20
]
