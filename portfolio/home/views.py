from django.shortcuts import render
from django.views import View
from django.conf import settings
from django.core.mail import send_mail


# Twilio msg

def send_email_notification(message):
    send_mail(
        subject='Notificación de Visita',
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=['rafaelmatteomourigan@gmail.com'],  
        fail_silently=False,
    )
    

## English Version

class HomeView(View):
    def get(self, request):
        
        # Procesar la solicitud
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
        }
        send_email_notification('¡Alguien ha visitado tu sitio web (English)!')
        return render(request, 'home/english/main.html', context)
    
    
class AboutMeView(View):
    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
        }
        return render(request, 'home/english/about_me.html', context)
    

class PythonView(View):
    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
        }
        return render(request, 'home/english/python.html', context)
    
    
class DataAnalysisView(View):
    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
        }
        return render(request, 'home/english/dataAnalysis.html', context)
    
    
class DataScienceView(View):
    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
        }
        return render(request, 'home/english/dataScience.html', context)
    
    
class MachineLearningView(View):
    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
        }
        return render(request, 'home/english/machineLearning.html', context)
    
    
class DeepLearningView(View):
    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
        }
        return render(request, 'home/english/deepLearning.html', context)
    
    
class TechSkillsView(View):
    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
        }
        return render(request, 'home/english/techSkills.html', context)
    
    
class CertificatesView(View):
    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
        }
        return render(request, 'home/english/certificates.html', context)
    
    
## Spanish Version

class PrincialView(View):
    def get(self, request):
        
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
        }
        send_email_notification('¡Alguien ha visitado tu sitio web (Español)!')        
        return render(request, 'home/spanish/principal.html', context)
    
    
class SobreMiView(View):
    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
        }
        return render(request, 'home/spanish/sobreMi.html', context)
    

class PythonEsView(View):
    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
        }
        return render(request, 'home/spanish/python.html', context)
    
    
class AnalisisDeDatosView(View):
    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
        }
        return render(request, 'home/spanish/analisisDeDatos.html', context)
    
    
class CienciaDeDatosView(View):
    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
        }
        return render(request, 'home/spanish/cienciaDeDatos.html', context)
    
    
class AprendizajeAutomaticoView(View):
    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
        }
        return render(request, 'home/spanish/aprendizajeAutomatico.html', context)
    
    
class AprendizajeProfundoView(View):
    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
        }
        return render(request, 'home/spanish/aprendizajeProfundo.html', context)
    
    
class HabilidadesTecnicasView(View):
    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
        }
        return render(request, 'home/spanish/habilidadesTecnicas.html', context)
    
    
class CertificadosView(View):
    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
        }
        return render(request, 'home/spanish/certificados.html', context)

