from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from .models import *
from django import forms
import datetime


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Email Address"}
        ),
    )

    first_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "First Name"}
        ),
    )

    last_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Last Name"}
        ),
    )

    group = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        required=True,
        label="Group",
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "group",
        )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["placeholder"] = "User Name"
        self.fields["username"].label = ""
        self.fields["username"].help_text = (
            '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
        )

        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["placeholder"] = "Password"
        self.fields["password1"].label = ""
        self.fields["password1"].help_text = (
            "<ul class=\"form-text text-muted small\"><li>Your password can't be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can't be a commonly used password.</li><li>Your password can't be entirely numeric.</li></ul>"
        )

        self.fields["password2"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["placeholder"] = "Confirm Password"
        self.fields["password2"].label = ""
        self.fields["password2"].help_text = (
            '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
        )


class AddNIPDetailsForm(forms.ModelForm):

    vehicle_no = forms.CharField(
        required=False,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Vehicle_Number", "class": "form-control"}
        ),
        label="",
    )

    reason = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Reason for the visit/entry", "class": "form-control"}
        ),
        label="",
    )

    name = forms.CharField(
        required=False,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Name", "class": "form-control"}
        ),
        label="",
    )

    phone = forms.CharField(
        required=False,
        widget=forms.NumberInput(
            attrs={"placeholder": "Phone", "class": "form-control"},
        ),
        label="",
    )

    created_at = forms.CharField(
        initial=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        disabled=True,
        widget=forms.widgets.DateTimeInput(
            attrs={"placeholder": "Date and Time", "class": "form-control"}
        ),
        label="",
    )
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["created_at"].initial = datetime.datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )

    class Meta:
        model = NON_INSTITUTE_ADMITTED
        exclude = ["user"]


class AddInstituteAdmittedDetailsForm(forms.ModelForm):

    created_at = forms.CharField(
        initial=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        disabled=True,
        widget=forms.widgets.DateTimeInput(
            attrs={"placeholder": "Date and Time", "class": "form-control"}
        ),
        label="",
    )

    name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Name", "class": "form-control"}
        ),
        label="",
    )

    roll_no = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={"placeholder": "Roll Number", "class": "form-control"}
        ),
        label="",
    )

    reason = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Reason for the visit/entry", "class": "form-control"}
        ),
        label="",
    )

    permission = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Permission", "class": "form-control"}
        ),
        label="",
    )

    phone = forms.CharField(
        required=True,
        widget=forms.NumberInput(
            attrs={"placeholder": "Phone", "class": "form-control"}
        ),
        label="",
    )

    vehicle_no = forms.CharField(
        required=False,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Vehicle Number", "class": "form-control"}
        ),
        label="",
    )
    
    BATCH_CHOICES = (
        ('','Select a batch'),
        ('First Year', 'First Year'),
        ('Second Year', 'Second Year'),
        ('Third Year', 'Third Year'),
        ('Fourth Year', 'Fourth Year'),
        ('M.Tech', 'M.Tech'),
        ('PhD', 'PhD'),
    )
    
    batch = forms.ChoiceField(
        choices=BATCH_CHOICES,
        required=True,
        label="",
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    
    BRANCH_CHOICES = (
        ('','Select a branch'),
        ('CSE','CSE'),
        ('ECE','ECE'),
        ('HSS','HSS')
    )
    
    branch = forms.ChoiceField(
        choices=BRANCH_CHOICES,
        required=True,
        label="",
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["created_at"].initial = datetime.datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )

    class Meta:
        model = INSTITUTE_ADMITTED
        exclude = ["user"]
            
        
class AddStudentDetailsForm(forms.ModelForm):

    name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Name", "class": "form-control"}
        ),
        label="",
    )

    roll_no = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={"placeholder": "Roll Number", "class": "form-control"}
        ),
        label="",
    )

    email = forms.EmailField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Email", "class": "form-control"}
        ),
        label="",
    )

    room_no = forms.IntegerField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Room Number", "class": "form-control"}
        ),
        label="",
    )

    phone = forms.CharField(
        required=True,
        widget=forms.NumberInput(
            attrs={"placeholder": "Phone", "class": "form-control"}
        ),
        label="",
    )
    
    BATCH_CHOICES = (
        ('','Select a batch'),
        ('First Year', 'First Year'),
        ('Second Year', 'Second Year'),
        ('Third Year', 'Third Year'),
        ('Fourth Year', 'Fourth Year'),
        ('M.Tech', 'M.Tech'),
        ('PhD', 'PhD'),
    )
    
    batch = forms.ChoiceField(
        choices=BATCH_CHOICES,
        required=True,
        label="",
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    
    BRANCH_CHOICES = (
        ('','Select a branch'),
        ('CSE','CSE'),
        ('ECE','ECE'),
        ('HSS','HSS')
    )
    
    branch = forms.ChoiceField(
        choices=BRANCH_CHOICES,
        required=True,
        label="",
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    class Meta:
        model = STUDENTS_DATA
        exclude = ["user"]


class UpdateStudentForm(forms.ModelForm):
    roll_no = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={"placeholder": "Roll Number", "class": "form-control"}
        ),
        label="",
    )

    class Meta:
        model = STUDENTS_DATA
        exclude = ['user','name','email','phone','room_no','batch','branch']
