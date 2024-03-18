from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from uav.models import UAV, RentedUAVs
from django.contrib.auth.decorators import login_required
from .forms import UAVForm, RentedUAVsForm
from .models import RentedUAVs



def index(request):
    # Ana sayfayı render et
    return render(request, "index.html")

def uavs(request):
    # İHA listesi sayfasını oluştur ve isteğe bağlı olarak anahtar kelimeye göre filtreleme yap
    keyword = request.GET.get("keyword")
    if keyword:
        UAVs = UAV.objects.filter(model_name__contains=keyword)
        return render(request, "uavs.html", context={"UAVs": UAVs})
    else:
        UAVs = UAV.objects.all()
        return render(request, "uavs.html", context={"UAVs": UAVs})

def detail(request, id):
    # İHA detaylarını göster
    uav = get_object_or_404(UAV, id=id)
    return render(request, "uav_details.html", context={"uav": uav})

def rent(request):
    # Kiralık İHA listesi sayfasını oluştur
    uavs = UAV.objects.filter(company=request.user)
    return render(request, "uav_rent.html", context={"UAVs": uavs})

@login_required(login_url='/user/login')
def rent_an_uav(request, id):
    # İHA kiralama formunu oluştur ve işlemi gerçekleştir
    if request.method == "GET":
        form = RentedUAVsForm()
        return render(request, "rent_form.html", context={"form": form})
    else:
        form = RentedUAVsForm(request.POST)
        if form.is_valid():
            uav_rent = form.save(commit=False)
            uav_rent.user = request.user
            uav_rent.save()
            messages.success(request, "İha kiralandı")
            return redirect("index")

@login_required(login_url='/user/login')
def give_back(request, id):
    # Kiralanan İHA'yı geri ver
    rented_uav = get_object_or_404(RentedUAVs, id=id)
    rented_uav.delete()
    return redirect("index")

@login_required(login_url='/user/login')
def add(request):
    # İHA ekleme formunu oluştur ve işlemi gerçekleştir
    if request.method == "POST":
        form = UAVForm(request.POST, request.FILES)
        if form.is_valid():
            uav = form.save(commit=False)
            uav.company = request.user
            uav.save()
            messages.success(request, "Başarıyla Kaydedildi")
            return redirect("index")
        else:
            messages.error(request, "Yükleme Başarısız")
            return render(request, "addarticle.html")
    else:
        form = UAVForm()
        return render(request, "add.html", {"form": form})

@login_required(login_url='/user/login')
def update(request, id):
    # İHA güncelleme formunu oluştur ve işlemi gerçekleştir
    article = get_object_or_404(UAV, id=id)
    if request.method == "POST":
        form = UAVForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            uav = form.save(commit=False)
            uav.author = request.user
            uav.save()
            messages.success(request, "Başarıyla Güncellendi")
            return redirect("uav:rent")
        else:
            messages.error(request, message="Güncelleme Başarısız, lütfen kriterlere uygun yazdığınızdan emin olun")
            return redirect("uav:rent")
    else:
        form = UAVForm(instance=article)
        return render(request, "update.html", context={"form": form})

@login_required(login_url='/user/login')
def delete(request, id):
    # İHA'yı sil
    uav = get_object_or_404(UAV, id=id)
    uav.delete()
    messages.success(request, "İha ilandan Silindi")
    return redirect("uav:rent")

@login_required(login_url='/user/login')
def rented(request):
    # Kiralanan İHA'ları göster
    user_rented_uavs = RentedUAVs.objects.filter(user=request.user)
    return render(request, "uavs_rented.html", context={"UAVs": user_rented_uavs})
