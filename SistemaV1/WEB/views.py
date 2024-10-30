from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django import forms
from Sistema.models import Usuario
from django.views.generic import ListView, TemplateView


def lista_usuarios(request):
    usuarios = Usuario.objetos.all()
    contexto = {'usuarios': usuarios}
    return render(request, "templates/usuarios.html", contexto)

class ListaUsuarios(ListView):
    template_name = "tamplates/usuarios.html"
    model = Usuario
    context_object_name = "usuarios"


class FormulariodeCriacao:
    pass


def cria_usuario(request, pk):
    if request.method == 'POST':
        form = FormulariodeCriacao(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lista_usuarios'))
        else:
            return render(request, "templates/form.html", {'form': form})

class IndexTemplateView(TemplateView):
    template_name = "index.html"

class UsuarioListView(ListView):
    template_name = 'website/lista.hmtl'
    model = Usuario
    context_object_name = "usuarios"

class UsuarioUpdateView(UpdateView):
    template_name = "atualiza.html"
    model = Usuario
    fields = '__all__'
    context_object_name = 'usuario'

    def get_object(self, queryset=None):
        usuario = None
        id = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)

        if id is not None:
            usuario = Usuario.objects.filter(id=id).first()

        elif slug is not None:
            campo_slug = self.gete_slug_field()

            usuario = Usuario.objects.filter(**{campo_slug: slug}).first()

        return usuario

class UsuarioDeleteView(DeleteView):
    template_name = "website/excluir.html"
    model = Usuario
    context_object_name = 'usuario'
    success_url = reverse_lazy(
        "website:lista_usuarios"
    )


class InsereUsuarioForm:
    pass


class UsuarioCreateView(CreateView):
    template_name = "website/cria.html"
    model = Usuario
    form_class = InsereUsuarioForm
    success_url = reverse_lazy("website:lista_usuarios")

class InsereUsuarioForm(forms.Form):
    class Meta:

        model = Usuario

        fields = [
            'nome',
            'usuario',
            'senha'
        ]
# Create your views here.
