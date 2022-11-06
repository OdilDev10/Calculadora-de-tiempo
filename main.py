respuestas = ['next day', 'days later']

def add_time(hora, cantidadASumar, dia = ''):
    
    # hora actual
    horaActualDividida = hora.split()
    horaActual = horaActualDividida[0].split(':')

    horaActualHora =  int(horaActual[0])
    horaActualMinuto =  int(horaActual[1])

    # esta es la hora a sumar
    horaDividida = hora.split()
    cantidadDividida = cantidadASumar.split(':')
    cantidadDivididaHora =  int(cantidadDividida[0])
    cantidadDivididaMinuto =  int(cantidadDividida[1])

    # sumando horas
    horaFinal = horaActualHora + cantidadDivididaHora
    minutosFinal = horaActualMinuto + cantidadDivididaMinuto

    # validando si es am o pm
    if(horaDividida[1] == 'PM' or horaDividida[1] == 'pm' or horaDividida[1] == 'Pm' or horaDividida[1] == 'pM' or horaDividida[1] == 'AM' or horaDividida[1] == 'am' or horaDividida[1] == 'Am' or horaDividida[1] == 'aM'):
        tanda = 0
        dias = 0

        while(horaFinal > 12):
            horaFinal = horaFinal - 12
            tanda = tanda + 1

            if(tanda >= 1 and horaActualDividida[1] == 'PM'):
                horaActualDividida[1] = 'AM'
            else:
                hornada = "PM"
                horaActualDividida[1] = 'PM'

            if(tanda == 2):
                dias = dias + 1
                tanda = 0
        
        if(dia == '' and dias >= 1):#next day 
            print(horaFinal,":",minutosFinal, horaActualDividida[1],",",dias,respuestas[0])                
        elif(dias and dia): #dia y dias despues
            print(horaFinal,":",minutosFinal, horaActualDividida[1],",",dia,",",dias,respuestas[1])                    
        elif(dia == '' and dias < 1):#limpio
            print(horaFinal,":",minutosFinal, horaActualDividida[1])            
        elif(dias):#con los dias de direfencia
            print(horaFinal,":",minutosFinal, horaActualDividida[1],",",dias,respuestas[1])            
        elif(dia): #con el dia
            print(horaFinal,":",minutosFinal, horaActualDividida[1],",",dia)    

        # print(tanda, 'tanda')
        # print(dias, 'dias')

    return print("Fin");

add_time("6:30 PM", "205:12")

