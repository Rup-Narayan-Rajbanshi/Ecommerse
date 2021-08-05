from company.models.company import CompanyUser
from django.http import HttpResponse, HttpResponseNotFound, Http404


class CompanyOwnerOnlyMixin(object):

    def has_permissions(self):
        # Assumes that your Ticket model has a foreign key called user.
        if self.request.user.is_authenticated and self.request.user.group.filter(name='owner').exists():
            user_company = CompanyUser.objects.filter(user=self.request.user).first().company
            if self.get_object() == user_company:
                return True
        return False

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            html = "<html><body><h2> Permission Denied </h2></body></html>"
            return HttpResponse(html)

        return super(CompanyOwnerOnlyMixin, self).dispatch(
            request, *args, **kwargs)
