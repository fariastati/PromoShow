from django.conf.urls import url, include

from apps.usuario.views import index, usuario_view, usuario_list, usuario_edit, usuario_delete, UsuarioList, UsuarioCreate, UsuarioUpdate, UsuarioDelete


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^novo$', UsuarioCreate.as_view(), name='usuario_criar'),
    url(r'^listar$', UsuarioList.as_view(), name='usuario_listar'),
    url(r'^editar/(?P<pk>\d+)/$', UsuarioUpdate.as_view(), name='usuario_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', UsuarioDelete.as_view(), name='usuario_eliminar'),

]
