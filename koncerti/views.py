from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.utils.translation import gettext
from django.utils.translation import activate
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect

from .models import Koncert
from smetnakipublic import settings
from .forms import AddKoncertForm

def index(request): # Landing page, translated to the browser's language (default is english)
    template = loader.get_template("koncerti/index.html")

    # Translators: This is the text on the homepage buttons
    concerts = gettext("Concerts")
    band = gettext("Band")
    # Translators: This is the option in the language-switch box
    foreignLanguage = gettext("eng")

    koncertiUrl = '/koncerti/international' # The URL slug leading to 'koncerti' page
    bandUrl = '/band/international' # The URL slug leading to 'band' page

    context = {
        'Concerts' : concerts,
        'Band' : band,
        'foreignLanguage' : foreignLanguage,
        'koncertiUrl' : koncertiUrl,
        'bandUrl' : bandUrl,
    }
    
    return HttpResponse(template.render(context, request))

def sloIndex(request): # Landing page in slovenian
    template = loader.get_template("koncerti/index.html")

    # Translators: This is the option in the language-switch box
    foreignLanguage = gettext("eng")

    concerts = "Koncerti"
    band = "Band"

    koncertiUrl = '/koncerti' # The URL slug leading to 'koncerti' page
    bandUrl = '/band' # The URL slug leading to 'band' page
    context = {
        'Concerts' : concerts,
        'Band' : band,
        'foreignLanguage' : foreignLanguage,
        'koncertiUrl' : koncertiUrl,
        'bandUrl' : bandUrl,
    }
    return HttpResponse(template.render(context, request))


def band(request): # Band information view
    template = loader.get_template("koncerti/band.html")

    # Translators: This is the navigation button text
    Concerts = gettext("Concerts")
    # Translators: These are instruments on the band page
    Trumpet = gettext("Trumpet")
    Bass_guitar = gettext("Bass guitar")
    Guitar = gettext("Guitar")
    Precussion = gettext("Percussions")
    Trombone = gettext("Trombone")
    Saxophone = gettext("Saxophone")
    Drums = gettext("Drums")
    # Translators: This long string is a band description. May take some creative effort to translate, don't translate ad-lib if it translates funny
    Description = gettext("S stands for SKA! Please look at the picture again! Feel the groove. Feeeel the grrrroooove! For us It's all in the groove. The Žiga spends his time in his basement like a nerd with man boobs, but instead he beats the drums up to 69 hours a day! The Žan is taking his trombone everywhere in case the inspiration kicks in! Come to the show! Listen to the music!")
    # Translators: This is the option in the language-switch box
    foreignLanguage = gettext("eng")
    
    # This are the URL links
    homePage = "/international"

    context = {
        'Concerts' : Concerts,
        'Trumpet' : Trumpet,
        'Bass_guitar' : Bass_guitar,
        'Guitar' : Guitar,
        'Precussion' : Precussion,
        'Trombone' : Trombone,
        'Saxophone' : Saxophone,
        'Drums' : Drums,
        'Description' : Description,
        'homePage' : homePage,
        'foreignLanguage' : foreignLanguage,
    }
    return HttpResponse(template.render(context, request))

def sloBand(request):
    template = loader.get_template("koncerti/band.html")
    # Translators: This is the navigation button text
    Concerts = "Koncerti"
    # Translators: These are instruments on the band page
    Trumpet = "Trobenta"
    Bass_guitar = "Bas kitara"
    Guitar = "Kitara"
    Precussion = "Tolkala"
    Trombone = "Pozavna"
    Saxophone = "Saksofon"
    Drums = "Bobni"
    # Translators: This long string is a band description. May take some creative effort to translate, don't translate ad-lib if it translates funny
    Description = "Smetnaki so tisto kar moškim manjka, da bi žensko dokončno osvojili. So manjkajoči člen slovenske glasbene scene. So tista muha, ki konstantno brenči in ti gre na živce, a se njene oči in trup svetijo v prelepem zelenem odtenku, da bi jo speštal. So zadrga na hlačah lokalnega top modela, ki zapeljivo stoji na glavni avtobusni postaji. Vse to se združi v kombinaciji geliranih frizur drznega punka, črno-belih oblek skaja, prešvicanih afro frizur funka in svetlečih na zvonec hlač diska."
    # Translators: This is the option in the language-switch box
    foreignLanguage = gettext("eng")

    homePage = ""

    context = {
        'Concerts' : Concerts,
        'Trumpet' : Trumpet,
        'Bass_guitar' : Bass_guitar,
        'Guitar' : Guitar,
        'Precussion' : Precussion,
        'Trombone' : Trombone,
        'Saxophone' : Saxophone,
        'Drums' : Drums,
        'Description' : Description,
        'homePage' : homePage,
        'foreignLanguage' : foreignLanguage,
    }
    return HttpResponse(template.render(context, request))

def koncerti(request):
    # Translators: This is the navigation button text
    Band = gettext("Band")
    # Translators: This is the option in the language-switch box
    foreignLanguage = gettext("eng")

    # One concert listing is currently one model instance. Arrange them, so that earliest date is at the beginning of a list
    concert_list = Koncert.objects.order_by('concert_date_time')

    template = loader.get_template("koncerti/koncerti.html")

    homePage = "/international"

    mode = "/international"

    context = {
        'Band' : Band,
        'concert_list': concert_list,
        'homePage' : homePage,
        'foreignLanguage' : foreignLanguage,
        'mode' : mode
    }
    return HttpResponse(template.render(context, request))

def sloKoncerti(request):
    # Highest order number will be the first one on the list
    concert_list = Koncert.objects.order_by('concert_date_time')
    # Translators: This is the option in the language-switch box
    foreignLanguage = gettext("eng")
    Band = "Band"
    template = loader.get_template("koncerti/koncerti.html")

    homePage = ""

    mode = ""

    context = {
        'Band' : Band,
        'concert_list': concert_list,
        'homePage' : homePage,
        'foreignLanguage' : foreignLanguage,
        'mode' : mode
    }
    return HttpResponse(template.render(context, request))