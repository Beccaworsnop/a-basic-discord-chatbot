import random

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
     return 'yo wassup !'

    if message == 'roll':
     return str(random.randint(1, 6))

    if p_message == '!help' :
     return 'what do you need help for :3 ?'

    return 'dunno what u talking about.. try typing !help'