import re

regex = r'(on|off|=|[+-]?\d+)'

state = True
current = 0

while True:
    user_input = input("Input: ")

    symbols = re.findall(regex, user_input, flags=re.IGNORECASE)

    for symbol in symbols:
        if symbol.lower() == 'on':
            state = True
        elif symbol.lower() == 'off':
            state = False
        elif symbol == '=':
            print(f'Total: {current}')
        elif state:
            current += int(symbol)