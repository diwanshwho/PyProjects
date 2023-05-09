import pint


def converter():
    u = pint.UnitRegistry()
    t = u.Quantity

    def mainconverter(val, u1, u2):
        temp = t(val, u1).to(u2)
        print('\n\t', f'{t(val,u1):~P} → {temp:~P}')

    convert = ['Length', 'Area', 'Volume', 'Speed', 'Weight', 'Temperature', 'Power']
    print("You have entered CONVERTER mode ▼ \nWhich Parameter you want to convert", convert, "-→ ")
    parameter = input().strip()
    if parameter.capitalize() in convert:
        value = float(input('Provide value -→ '))
        match parameter.lower():
            case 'length':
                unit1, unit2 = input("\t[dm, mm, km, cm, m, mile, ly, micrometer, parsec, yard, ft, inch]\n"
                                     "Enter the Units for Conversions(seperated by comma)-→ ").split(',')
                mainconverter(value, unit1, unit2)

            case 'area':
                unit1, unit2 = input("\t[m**2, dm**2, cm**2, km**2, mm**2, ha,mi**2, yd**2, ft**2, in**2]\n"
                                     "Enter the Units for Conversions(seperated by comma)-→ ").split(',')
                mainconverter(value, unit1, unit2)

            case 'volume':
                unit1, unit2 = input("\t[m**3, cm**3, dl, l, dm**3, mm**3, ml, ft**3, in**3, yd**3]\nEnter the Units for Conversions"
                                     "(seperated by comma)-→ ").split(',')
                mainconverter(value, unit1, unit2)

            case 'speed':
                unit1, unit2 = input("\t[km/s, m/s, mph, km/h]\nEnter the Units for Conversions"
                                     "(seperated by comma)-→ ").split(',')
                mainconverter(value, unit1, unit2)

            case 'weight':
                unit1, unit2 = input("\t[g, ct, t, mg, kg, oz, gr, lb, dr]\nEnter the Units for Conversions"
                                     "(seperated by comma)-→ ").split(',')
                mainconverter(value, unit1, unit2)

            case 'temperature':
                unit1, unit2 = input("\t[K, degC, degF, degR, degRe]\nEnter the Units for Conversions"
                                     "(seperated by comma)-→ ").split(',')
                mainconverter(value, unit1, unit2)

            case 'power':
                unit1, unit2 = input("\t[W, kW, J/s, Btu/s, hp, kcal/s]\nEnter the Units for Conversions"
                                     "(seperated by comma)-→ ").split(',')
                mainconverter(value, unit1, unit2)
