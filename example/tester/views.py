from django.views.generic import FormView, DetailView
from django.views.generic.detail import BaseDetailView
from django.http import JsonResponse
from django.urls import reverse

from .models import TestModel, PydanticTestModel
from .forms import BasicTestModelForm


class TestModelFormView(FormView):
    template_name = "form.html"
    form_class = BasicTestModelForm
    model = TestModel

    def form_valid(self, form):
        self.obj = form.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("detail", kwargs={"pk": self.obj.pk})


class TestModelDetailView(DetailView):
    template_name = "detail.html"
    model = TestModel


class PydanticJSONView(BaseDetailView):

    model = PydanticTestModel

    def render_to_response(self, context, **response_kwargs):
        # self.object._meta.get_field("nested").pydantic_schema
        # not sure if it'd ever be useful to reference this object, but
        # the pydantic model is available on the field.
        return JsonResponse(self.object.nested, **response_kwargs)
