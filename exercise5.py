num = 0
tot = 0.0
while True :
    sval = input('Ingrese un número: ')
    if sval == 'done' :
        break
        try :
            fval = float(sval)
        except :
            print('Digito invalido')
            continue
    #print(fval)
    num = num + 1
    tot = tot + fval
#print('ALL DONE')
print(tot, num, tot/num)
