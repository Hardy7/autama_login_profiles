# -*- coding:utf-8 -*-
__version__ = '3.0.3'
"""
@author :   JianqiangHao
@date   :   2020-03-04
"""

from django import template

register = template.Library()


@register.filter(name='format_none')
def format_none(value):
    if not value:
        return ''
    return value
