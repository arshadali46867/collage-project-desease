from django import forms 
class BreastCancerForm(forms.Form): 
	radius = forms.FloatField( 
		label='MeanRadius', 
		min_value=0, 
		widget=forms.NumberInput(attrs={'class': 'form-control'}), 
	) 
	texture = forms.FloatField( 
		label='MeanTexture', 
		min_value=0, 
		widget=forms.NumberInput(attrs={'class': 'form-control'}), 
	) 
	perimeter = forms.FloatField( 
		label='MeanPerimeter', 
		min_value=0, 
		widget=forms.NumberInput(attrs={'class': 'form-control'}), 
	) 
	area = forms.FloatField( 
		label='MeanArea', 
		min_value=0, 
		widget=forms.NumberInput(attrs={'class': 'form-control'}), 
	) 
	smoothness = forms.FloatField( 
		label='MeanSmoothness', 
		min_value=0, 
		widget=forms.NumberInput(attrs={'class': 'form-control'}), 
	) 
