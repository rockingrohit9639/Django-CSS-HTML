from django.urls import path
from .views import (
	ChallengesListView,
	ChallengesDetailView,
	ChallengesCreateView,
	ChallengesUpdateView,
	ChallengesDeleteView
)

app_name = 'challenges'
urlpatterns = [
	path('', ChallengesListView.as_view(), name='challenges-list'),
	path('<int:id>/', ChallengesDetailView.as_view(), name='challenges-detail'),
	path('create/', ChallengesCreateView.as_view(), name='challenges_create'),
	path('<int:id>/update/', ChallengesUpdateView.as_view(), name='challenges-update'),
	path('<int:id>/delete/', ChallengesDeleteView.as_view(), name='challenges-delete'),

]
