from django import forms 
# from . models import UserRegistration

class HeartDiseaseForm(forms.Form): 
	# Define form fields for heart disease prediction 

	age = forms.FloatField(label='Age', widget=forms.NumberInput(attrs={'class': 'form-control'})) 
	# Field for age, represented as a float input widget 

	sex = forms.FloatField(label='Sex (1=Male,2=Female,3=other)', widget=forms.NumberInput(attrs={'class': 'form-control'})) 
	# Field for sex, represented as a float input widget 

	cp = forms.FloatField(label='CP', widget=forms.NumberInput(attrs={'class': 'form-control'})) 
	# Field for chest pain type (CP), represented as a float input widget 

	trestbps = forms.FloatField(label='TRESTBPS', widget=forms.NumberInput(attrs={'class': 'form-control'})) 
	# Field for resting blood pressure (TRESTBPS), represented as a float input widget 

	chol = forms.FloatField(label='CHOL', widget=forms.NumberInput(attrs={'class': 'form-control'})) 
	# Field for serum cholesterol level (CHOL), represented as a float input widget 

	fbs = forms.FloatField(label='FBS', widget=forms.NumberInput(attrs={'class': 'form-control'})) 
	# Field for fasting blood sugar (FBS), represented as a float input widget 

	restecg = forms.FloatField(label='RESTECG', widget=forms.NumberInput(attrs={'class': 'form-control'})) 
	# Field for resting electrocardiographic results (RESTECG), represented as a float input widget 

	thalach = forms.FloatField(label='THALACH', widget=forms.NumberInput(attrs={'class': 'form-control'})) 
	# Field for maximum heart rate achieved (THALACH), represented as a float input widget 

	exang = forms.FloatField(label='EXANG', widget=forms.NumberInput(attrs={'class': 'form-control'})) 
	# Field for exercise-induced angina (EXANG), represented as a float input widget 

	oldpeak = forms.FloatField(label='OLDPEAK', widget=forms.NumberInput(attrs={'class': 'form-control'})) 
	# Field for ST depression induced by exercise relative to rest (OLDPEAK), represented as a float input widget 

	slope = forms.FloatField(label='SLOPE', widget=forms.NumberInput(attrs={'class': 'form-control'})) 
	# Field for the slope of the peak exercise ST segment (SLOPE), represented as a float input widget 

	ca = forms.FloatField(label='CA', widget=forms.NumberInput(attrs={'class': 'form-control'})) 
	# Field for the number of major vessels colored by fluoroscopy (CA), represented as a float input widget 

	thal = forms.FloatField(label='THAL', widget=forms.NumberInput(attrs={'class': 'form-control'})) 
	# Field for thalassemia (THAL), represented as a float input widget 




# class UserRegistrationForm(forms.ModelForm):
# 	password1=forms.CharField(widget=forms.PasswordInput)
# 	password2=forms.CharField(widget=forms.PasswordInput)
# 	class Meta:
# 		model=UserRegistration

# 		fields=('first_name','last_name','username','email','password1','password2')



# class LoginUserform(forms.ModelForm):
# 	password1=forms.CharField(widget=forms.PasswordInput())
# 	class Meta:
# 		model=UserRegistration
# 		fields=('username','password1')
	
    
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserRegistrationForm(UserCreationForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=('first_name','last_name','username','email','password1','password2')



class LoginUserform(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
         model=User
         fields=('username','password')

		
