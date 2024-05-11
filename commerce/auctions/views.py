from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render ,redirect
from django.urls import reverse
from .forms import *
from decimal import Decimal
from .models import *


def index(request):
    return redirect('active_listing')

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("active_listing")
        else:
            return render(
                request,
                "auctions/login.html",
                {"message": "Invalid username and/or password."},
            )
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("active_listing")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(
                request, "auctions/register.html", {"message": "Passwords must match."}
            )

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(
                request,
                "auctions/register.html",
                {"message": "Username already taken."},
            )
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def create_listing(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    if request.method == "POST":
        form = NewListingForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.created_by = request.user
            obj.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = NewListingForm
        return render(request, "auctions/create_listing.html", {"form": form})


def active_listing(request):
    listings = AuctionListing.objects.filter(active=True)
    listings_end = AuctionListing.objects.filter(active=False)
    
    for list in listings:
        print("---->", list)
    return render(request, "auctions/index.html", {"listings": listings,"listings_end":listings_end})


def categories(request):
    categories = AuctionListing.objects.values_list("category", flat=True).distinct()

    print(categories)
    return render(request, "auctions/categories.html", {"categories": categories})


def category_listing(request, cat):
    listings = AuctionListing.objects.filter(category=cat)
    return render(request, "auctions/index.html", {"listings": listings, "cat": cat})


def close_auction(request, pk):
    auction = AuctionListing.objects.get(id=pk)
    if request.user.is_authenticated and auction.created_by == request.user:
        # user is authenticated, and owner of that auction
        auction.active = False
        auction.save()

    return HttpResponseRedirect(reverse("auction_view", args=[pk]))


def auction_view(request, pk):
    listing = AuctionListing.objects.get(id=pk)
    if request.user.is_authenticated:
        try:
            top_bid = Bid.objects.filter(listing=listing.id).order_by("-bid_amount")[0]
        except:
            top_bid = None

        if request.method == "POST":
            if "bid" in request.POST:
                bid_form = BidForm(request.POST, listing=listing)
                if bid_form.is_valid() and request.user.is_authenticated:
                    temp = bid_form.save(commit=False)
                    temp.bidder = request.user
                    temp.listing = listing
                    temp.save()
                    listing.current_bid = temp.bid_amount
                    listing.save()
                    return redirect(auction_view, pk=listing.pk)

        # new comment was submitted
            elif "comment" in request.POST:
                comment_form = CommentForm(request.POST)
                if comment_form.is_valid() and request.user.is_authenticated:
                    temp = comment_form.save(commit=False)
                    temp.commenter = request.user
                    temp.listing = listing
                    temp.save()
                    return redirect(auction_view, pk=listing.pk)

        else:
            
            form_comment = CommentForm()
            minimum_bid = listing.current_bid + Decimal(0.01).quantize(Decimal("1.00"))
            bid_form = BidForm(initial={"amount": minimum_bid}, listing=listing)

            bids = Bid.objects.filter(listing=listing.id).order_by("-bid_amount")
            comments = Comment.objects.filter(listing=listing)

            print("----->", listing)
            return render(
                request,
                "auctions/specific_listing.html",
                {
                    "listing": listing,
                    "form_comment": form_comment,
                    "bids": bids,
                    "top_bid": top_bid,
                    "min_bid": minimum_bid,
                    "bid_form": bid_form,
                    "comments": comments,
                },
            )
    else:
        return HttpResponseRedirect(reverse("login"))

def wishlist(request,pk):
    if request.user.is_authenticated:
        auction = AuctionListing.objects.get(pk=pk)
        if request.user in auction.favoured.all():
            # User already favoured, unfavourite auction
            auction.favoured.remove(request.user)
        else:
            # add auction to favourites
            auction.favoured.add(request.user)
    return HttpResponseRedirect(reverse("auction_view", args=[pk]))

def bookmarks(request):
    if request.user.is_authenticated:
        auctions = AuctionListing.objects.filter(favoured=request.user)
        return render(request, "auctions/bookmark.html", {"listings": auctions})
    else:
        return HttpResponseRedirect(reverse("login"))