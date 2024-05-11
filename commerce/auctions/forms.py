from django import forms
from auctions.models import AuctionListing, Bid, Comment


class NewListingForm(forms.ModelForm):
    image_url = forms.URLField(required=False) 
    class Meta:
        model = AuctionListing
        fields = ['title', 'description', 'category', 'image_url', 'starting_bid']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter description'}),
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter category'}),
            'image_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter image URL'}),
            'starting_bid': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter starting bid'}),
        }
        


class BidForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.listing = kwargs.pop('listing')
        super(BidForm, self).__init__(*args, **kwargs)

    def clean(self):
        amount = self.cleaned_data['bid_amount']
        if amount <= self.listing.current_bid:
            raise forms.ValidationError("Your bid is lower than current bid")

        return self.cleaned_data

    class Meta:
        model = Bid
        fields = ['bid_amount']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your comment'})
        }