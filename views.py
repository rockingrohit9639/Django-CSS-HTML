from django.shortcuts import render, get_object_or_404
from django.urls import reverse
# Create your views here.
from django.views.generic import (
	CreateView,
	DetailView, 
	ListView,
	UpdateView,
	ListView,
	DeleteView
)
from .forms import ChallengesModelForm
from .models import Challenges

class ChallengesCreateView(CreateView):
	template_name = 'challenges_create.html'
	form_class = ChallengesModelForm
	queryset = Challenges.objects.all()
	#success_url = '/'

	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)

	#def get_success_url(self):
		#return '/'

class ChallengesListView(ListView):
	template_name = 'challenges_list.html'
	queryset = Challenges.objects.all()

class ChallengesDetailView(DetailView):
	template_name = 'challenges_detail.html'
	queryset = Challenges.objects.all()

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Challenges, id=id_)

class ChallengesUpdateView(UpdateView):
	template_name = 'challenges_create.html'
	form_class = ChallengesModelForm
	queryset = Challenges.objects.all()
	

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Challenges, id=id_)

	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)

class ChallengesDeleteView(DeleteView):
	template_name = 'challenges_delete.html'
	queryset = Challenges.objects.all()

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Challenges, id=id_)

	def get_success_url(self):
		return reverse('challenges:challenges-list')
# Create your views here