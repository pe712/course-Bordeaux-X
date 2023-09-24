from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from silk.profiling.profiler import silk_profile
from course_drapeau.forms.account import AdvancedRunnerForm

from course_drapeau.models import Runner, Section
from django.contrib.auth.models import User
import logging


class WipView(View):
    """
    Usefull view for work in progress and testing purposes.
    """
    @silk_profile()
    def get(self, request, *args, **kwargs):
        # for key, value in request.session['attributes'].items():
        #     logging.info(f"{key}: {value}")
        content = '<html><body><h1>WIP</h1></body></html>'
        # Runner.objects.create(user=request.user)
        # logging.info(self.request.user.__class__)

        # user = User.objects.all().first()
        # user.is_staff = True
        # user.is_superuser = True
        # user.save()

        # user.delete()
        # return HttpResponseRedirect('/admin/')
        # runner = Runner.objects.all().first()
        # runner.user
        form = AdvancedRunnerForm(instance=request.user.runner)
        logging.info(form)
        return HttpResponse(content)
