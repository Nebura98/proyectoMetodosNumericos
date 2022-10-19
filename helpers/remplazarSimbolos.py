def remplazarSimbolos(text):
    trigonometria = {
        'e': 'math.exp',
        '√': 'math.sqrt',
        'cos': 'math.cos',
        'sin': 'math.sin',
        'tan': 'math.tan',
        '^': '**'}
    for simbolo in trigonometria:
        text = text.replace(simbolo, trigonometria[simbolo])

    print(text)
    return text
