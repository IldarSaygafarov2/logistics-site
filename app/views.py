from django.shortcuts import redirect, render
from logistics import settings
import requests
from .forms import RequestMessageForm


def render_home_page(request):
    return render(request, "app/index.html")


def render_contact_page(request):
    form = RequestMessageForm()
    context = {
        "form": form,
    }
    return render(request, "app/contact.html", context)


def render_about_page(request):
    return render(request, "app/about.html")


def send_message_to_request(request):
    data = request.POST
    form = RequestMessageForm(data=data)
    form.save()

    msg = f"""
Имя: {data['first_name']}
Почта: {data['email']}
Тема: {data['subject']}
Сообщение: {data['message']}
    """

    resp = requests.post(
        settings.TG_API_URL.format(
            token=settings.BOT_TOKEN, channel_id="@newavialogisticmessages", text=msg
        )
    )
    print(resp.text)

    return redirect("contact")
