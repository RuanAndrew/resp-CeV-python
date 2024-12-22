palavras = ('aprender','programar','linguagem','python','curso','gratis','estudar','praticar','trabalhar','mercado','programar','futuro')
for p in palavras:
    print(f'\n{p} tem ',end='')
    for letras in p:
        if letras.lower() in 'aeiou':
            print(letras,end=' ')