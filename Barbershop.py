
corte = int(input("Digite 1 se o corte é masculino ou 2 se for feminino: "))

if corte == 1:
    corte1 = int(input("Digite 1 para cabelo ou 2 para cabelo e barba: "))

    if corte1 == 1:
        estilo_do_cabelo = int(input("Digite 1 para corte estilo surfista ou 2 para corte estilo raspa tudo: "))

        if estilo_do_cabelo == 1:
           valor = 28+10
        else:
            valor = 28-10
    elif corte1 == 2:
        estilo_de_barba = int(input("Digite 1 para barba desenhada ou 2 se não for: "))

        if estilo_de_barba == 1:
            valor = 50+10
        else:
                valor = 50-10

else:
    corte_feminino = int(input("Digite 1 se for fazer apenas o corte de cabelo ou 2 se for fazer o corte de cabelo e as unhas: "))
    if corte_feminino == 1:
        corte2ou3 = int(input("Digite 1 para corte Chanel ou dois para corte reto: "))
        if corte2ou3 == 1:
            valor = 60+10
        else:
                valor = 60-10

    elif corte_feminino == 2:
                corte4ou5 = int(input("Digite 1 para o pacote completo de corte de cabelo e o combo de unha mãos e pés ou 2 para apenas o corte de cabelo e apenas mãos: "))
                if corte4ou5 == 1:
                    valor = 100+10
                else:
                    valor = 100-10
print("Você deverá pagar R$,", valor, ". Volte sempre!")

