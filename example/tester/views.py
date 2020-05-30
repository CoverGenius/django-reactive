from django.views.generic import FormView, DetailView
from django.urls import reverse

from .models import TestModel
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
