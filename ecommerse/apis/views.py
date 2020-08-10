from django.views.generic.base import ContextMixin, TemplateResponseMixin
from django.views.generic.edit import ProcessFormView
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.core.exceptions import ImproperlyConfigured
import code
from django.contrib.auth.mixins import UserPassesTestMixin

class MultiFormsMixin(ContextMixin):
  form_classes = {}
  prefixes = {}
  initial = {}
  success_url = None

  def get_form_classes(self):
    return self.form_classes

  def get_prefix(self, form_name):
    return self.prefixes[form_name]

  def get_initial(self, form_name):
    return self.initial[form_name]

  def get_forms(self, form_classes = None):
    if form_classes is None:
      form_classes = self.get_form_classes()

    return dict([(key, klass(**self.get_form_kwargs(key))) for key, klass in form_classes.items()])

  def forms_valid(self, forms):
    return HttpResponseRedirect(self.get_success_url())

  def forms_invalid(self, forms):
    return self.render_to_response(self.get_context_data(**forms))

  def get_form_kwargs(self, form_name):
    kwargs = {}
    try:
      kwargs.update({'initial':self.get_initial(form_name)})
    except:
      pass
      
    if self.prefixes:
      kwargs.update({'prefix':self.get_prefix(form_name)})

    if self.request.method in ("POST", "PUT"):
      kwargs.update({
        'data':self.request.POST,
        'files':self.request.FILES,
      })

    return kwargs

  def get_success_url(self):
    if not self.success_url:
      raise ImproperlyConfigured("No URL to redirect to. Provide a success_url.")
    # code.interact(local=dict(globals(),**locals()))
    return str(self.success_url)

  def get_context_data(self, **kwargs):
    if "forms" not in kwargs:
      kwargs.update(**self.get_forms())
    # code.interact(local=dict(globals(),**locals()))
    return super().get_context_data(**kwargs)

class ProcessMultiFormsView(ProcessFormView):
  def post(self, request, *args, **kwargs):
    forms = self.get_forms()
    if all([form.is_valid() for form in forms.values()]):
      return self.forms_valid(forms)
    else:
      return self.forms_invalid(forms)

class BaseMultiFormsView(MultiFormsMixin, ProcessMultiFormsView):
    """
    A base view for displaying several forms.
    """

class MultiFormsView(TemplateResponseMixin, BaseMultiFormsView):
    """
    A view for displaing several forms, and rendering a template response.
    """

class AjaxTemplateMixin(object):
  def dispatch(self, request, *args, **kwargs):
    if not hasattr(self, 'ajax_template_name'):
      split = self.template_name.split(".html")
      split[-1] = "_inner"
      split.append(".html")
      self.ajax_template_name = ''.join(split)

    if request.is_ajax():
      self.template_name = self.ajax_template_name

    return super().dispatch(request, *args, **kwargs)

class GroupRequiredMixin(UserPassesTestMixin):
  login_url = 'dashboard:home'
  group_names = ["Admin",]

  def test_func(self):
    return self.request.user.groups.filter(name__in = self.group_names)

  def get_permission_denied_message(self):
    return "Must be {} to access this page".format(*self.group_names)
