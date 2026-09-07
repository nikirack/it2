from collections.abc import Callable

type Handler = Callable[[str], None]


HANDLERS: dict[str, Handler] = {}

def register_handler(name:str):
    def decorator(func:Handler):
        HANDLERS[name] = func
        return func
    
    return decorator

@register_handler("email")
def handle_email(data:str):
    print(data)

register_handler("sugma")(handle_email)

def send_notification(channel:str, data:str):
    handler = HANDLERS.get(channel)
    if handler:
        handler(data)


send_notification("email","test")