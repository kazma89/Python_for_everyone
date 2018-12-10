ht = input('Ingrese sus horas: ')
ir = input('Ingrese su impuesto: ')
try:
    fh = float(ht)
    fr = float(ir)
except:
    print("Error, favor ingresar un valor numerico")
    quit()
if fh > 40:
    pago = ft*fr
    otp = (fh - 40.0) * (fr * 0.5)
    xp = pago + otp
else:
    xp = fh * fr
print('Su pago es:',xp)
