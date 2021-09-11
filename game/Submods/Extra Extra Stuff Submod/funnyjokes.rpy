init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_randomjokes",category=["misc"],prompt="¿Puedes decirme algo gracioso?",pool=True,unlocked=True))

label monika_randomjokes:
    $ joke = renpy.random.randint(1,2)

    m 1eua "¡Oh! ¿Quieres que te cuente algo divertido, [player]?"
    m 1eub "Dame un segundo para que se me ocurra algo."
    m 1duc "Hmmm..."
    m 3eub "¡Ya tengo uno!"

    if joke == 1:
        m 1eua "¿Cómo se llama un montón de gatos?"
        m 1tub "Una {i}¡Miautaña!{/i}"
        m 1hua "Ehehehe~"
    if joke == 2:
        m 1eua "¿Quieres escuchar un chiste sobre pizzas?"
        m 1tub "No importa... Es demasiado quesoso."
        m 1hua "Ehehe~"
    if joke == 3:
        m 1eua "Oye [player], ¿has visto alguna vez la película 'Forest Gump'?"
        m 6eub "Si no, no entenderás el chiste"
        m 1eua "Pero no pasa nada.."
        m 3hub "Siempre podemos ver la película juntos~"
        m 1hua "Ehehe"
        m 1hub "Sin embargo, si la viste, entonces entenderás la broma."
        m 1eua "¿Cuál es la contraseña de Forest Gump?"
        m 1tub "{i}¡1forest1!{/i}"
        m 1eua "Es un juego de palabras para 'Run Forest Run' ehehe~"
return