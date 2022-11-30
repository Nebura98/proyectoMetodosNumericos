def remplazarSimbolos(text):
    trigonometria = {
        'e': 'math.exp',
        '√': 'math.sqrt',
        'cos': 'math.cos',
        'sin': 'math.sin',
        'tan': 'math.tan',
        '^': '**',
        'log':'math.log',
        'π':'math.pi'}
    for simbolo in trigonometria:
        text = text.replace(simbolo, trigonometria[simbolo])
    return text
