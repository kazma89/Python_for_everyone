ht = input('Ingrese sus horas: ')
ir = input('Ingrese su impuesto: ')
fh = float(ht)
fr = float(if)

if fh > 40:
    pago = ft*fr
    otp = (fh - 40.0) * (fr * 0.5)
    xp = pago + otp
else:
    xp = fh * fr
print('Su pago es:',xp)
