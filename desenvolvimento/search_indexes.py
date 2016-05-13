import datetime
import site

from haystack import indexes
from desenvolvimento.models import *


class ProjetoSearch(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    nome = indexes.CharField(model_attr='nome')
    resumo = indexes.CharField(model_attr='resumo')
    professor = indexes.CharField()

    def prepare_tag_name(self, object):
        return object.professor.nome

    def get_model(self):
        return Projeto

    def index_queryset(self,using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter().all()

class ArtigoSearch(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    nome = indexes.CharField(model_attr='titulo')


    # def prepare_tag_name(self, object):
    #     return object.professor.nome

    def get_model(self):
        return ArtigoEmPeriodico

    def index_queryset(self,using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter().all()