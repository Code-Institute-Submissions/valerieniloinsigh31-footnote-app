from django.urls import path
from . import views

app_name = 'writer_profile'

urlpatterns = [
    path('', views.writerprofile, name='writerprofile'),
    path('', views.footnote_history, name='footnote_history'),
    path('edit/<footnote_id>', views.edit_footnote, name='edit'),
    path('delete/<footnote_id>', views.delete_footnote, name='delete'),
]

# think about '' contents for edit footnote path