from datetime import datetime

from django import template

register = template.Library()


@register.filter  # type: ignore
def mostrar_duracao(value1, value2):
    if all((isinstance(value1, datetime), isinstance(value2, datetime))):  # type: ignore
        dias = (value1 - value2).days
        dia = "Dias"

        if dias == 1:
            dia = 'Dia'

        return f"{dias} {dia}"
    return "Ainda não foi emprestado"
