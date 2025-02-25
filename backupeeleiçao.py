import streamlit as st

print('Bem-vindo ao Sistema de Votos !')
print('  Sua voz é o nosso futuro.')
print('Para votar digite: CONTINUAR')
resposta = input("Digite aqui: ")
 
if resposta.upper() == "CONTINUAR":
    print("\n" * 50)  
    print('Sistema de Votação inicializado !')


    votos = {
        1: 0,  # Juscelino KubitscheK
        2: 0,  # Itamar Franco
        3: 0   # Afonso Pena
    }

   
    while True:
        print("\nEscolha seu candidato:")
        print("1 - Juscelino KubitscheK")
        print("2 - Itamar Franco")
        print("3 - Afonso Pena")
        print("0 - Sair e ver resultados")

        voto = input("Digite o número do candidato: ")

        if voto == "0":
            break  
        elif voto.isdigit():
            voto = int(voto)
            if voto in votos:
                votos[voto] += 1
                print("Voto registrado com sucesso!")
            else:
                print("Candidato inválido.")
        else:
            print("Entrada inválida. Digite um número.")

    
    print("\nResultado da votação:")
    for candidato, quantidade in votos.items():
        print(f"Candidato {candidato}: {quantidade} votos")
else:
    print("Comando inválido. Digite CONTINUAR para prosseguir.")
