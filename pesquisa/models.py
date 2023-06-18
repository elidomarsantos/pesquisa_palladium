from django.db import models


class Pesquisa(models.Model):
    
    colaborador = models.CharField(max_length=60, blank=True, null=True, verbose_name='')
    departamento = models.CharField(max_length=60, blank=True, null=True, verbose_name='')
    função = models.CharField(max_length=60, blank=True, null=True, verbose_name='')
    atitude_positiva = models.CharField(max_length=300, blank=True, null=True,)
    justificativa01 = models.CharField(max_length=300, blank=True, null=True, verbose_name='')
    trabalho_em_equipe = models.CharField(max_length=60, blank=True, null=True, verbose_name='')
    justificativa02 = models.CharField(max_length=300,blank=True, null=True, verbose_name='')
    atendimento_eficaz_cliente = models.CharField(max_length=60, blank=True, null=True, verbose_name='')
    justificativa03 = models.CharField(max_length=300,blank=True, null=True, verbose_name='')
    comunicação_com_liderança = models.CharField(max_length=60, blank=True, null=True, verbose_name='')
    justificativa04 = models.CharField(max_length=300,blank=True, null=True, verbose_name='')
    promoção_união = models.CharField(max_length=60, blank=True, null=True, verbose_name='')
    justificativa05 = models.CharField(max_length=300,blank=True, null=True, verbose_name='')
    melhorar_qualidade = models.CharField(max_length=60, blank=True, null=True, verbose_name='')
    justificativa06 = models.CharField(max_length=300,blank=True, null=True, verbose_name='')
    criatividade_redução_custos = models.CharField(max_length=60, blank=True, null=True, verbose_name='')
    justificativa07 = models.CharField(max_length=300,blank=True, null=True, verbose_name='')
    atitude_diante_mudanças = models.CharField(max_length=60, blank=True, null=True, verbose_name='')
    justificativa08 = models.CharField(max_length=300,blank=True, null=True, verbose_name='')
    ideias_para_bom_ambiente = models.CharField(max_length=60, blank=True, null=True, verbose_name='')
    justificativa09 = models.CharField(max_length=300,blank=True, null=True, verbose_name='')
    pontos_fortes = models.CharField(max_length=300, blank=True, null=True, verbose_name='', )
    pontos_reforçar = models.CharField(max_length=300, blank=True, null=True, verbose_name='')
    compromissos =  models.TextField(max_length=300, blank=True, null=True, verbose_name='')