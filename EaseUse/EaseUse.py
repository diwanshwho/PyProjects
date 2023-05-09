from modules.calculator import calc
from modules.converter import converter
from modules.rates import rates
import os

oper = input("What Tool you want to use [Calc, Conv, Rates] → ").strip()
if oper.lower() in ['calc', 'conv', 'rates']:
    if oper.lower() == 'calc':
        calc()
    elif oper.lower() == 'conv':
        converter()
    elif oper.lower() == 'rates':
        rates()
else:
    print("wrong choice!! ")

os.system('pause')