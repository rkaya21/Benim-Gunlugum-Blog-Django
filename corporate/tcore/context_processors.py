from .models import Setting


def SettingList(request):
    context = Setting.objects.first()
    return {'settings': context}
