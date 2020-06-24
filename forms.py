from django import forms

from .models import Challenges

class ChallengesModelForm(forms.ModelForm):
	class Meta:
		model = Challenges
		fields = [
			'title',
			'content',
			'active',
			]