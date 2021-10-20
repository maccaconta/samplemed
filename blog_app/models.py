from django.core.files.storage import FileSystemStorage
import django.conf
# from django.contrib.postgres.fields import JSONField
from django.db import models

repository_ = django.conf.settings.REPOSITORY
path_ = FileSystemStorage(location=repository_)


class BaseModel(models.Model):

    """
    ------------------------
     Name            : BaseModel
    :Descrição       : Cmpos generico
    :create          : Outubro-2021
    ------------------------
    """

    created_at = models.DateTimeField('criado', auto_now_add=True)
    updated_at = models.DateTimeField('atualizado', auto_now=True)

    class Meta:
        abstract = True


class Blog(BaseModel):

    """"
    ------------------------
     Name      : Blog
     Descrição : Tabela dos assuntos tratados no blog
    :create    : Outubro-2021
    ------------------------
    """

    title = models.TextField('titulo', blank=False, default='')
    subtitle = models.TextField('subtítulo', default='', blank=True)
    type = models.IntegerField('tipo', default='1', blank=True)
    content = models.TextField('conteudo', default='', blank=True)
    status = models.IntegerField('status', default='1', blank=True)


class Keywords(BaseModel):

    """"
    ------------------------
     Name      : keywords
     Descrição : Tabela com palavras chaves
    :create    : Outubro-2021
    ------------------------
    """
    id_pub = models.IntegerField('id_publicacao')
    keyword = models.TextField('palavra', blank=True, default='')
