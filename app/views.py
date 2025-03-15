from django.shortcuts import render


def render_home_page(request):
    return render(request, "app/index.html")


def render_contact_page(request):
    return render(request, "app/contact.html")


def render_about_page(request):
    return render(request, "app/about.html")


def render_services_page(request):
    return render(request, "app/services.html")
