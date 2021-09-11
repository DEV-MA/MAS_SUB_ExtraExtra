init 3 python in mas_compliments:

    compliment_database = dict()

init 22 python in mas_compliments:
    import store

    thanking_quips = [
        _("¡Aww! ¡Gracias [player]!"),
        _("¡Gracias por decir eso otra vez, [player]! Eres tan dulce"),
        _("¡Gracias por decírmelo de nuevo, [mas_get_player_nickname()]!"),
        _("You always make me feel special, [mas_get_player_nickname()]. Thank you"),
        _("Aww, [player]~ Eres tan dulce"),
        _("¡Gracias, [mas_get_player_nickname()]!"),
        _("Siempre sabes qué decir para hacerme feliz, [player]."),
        _("¡Eres tan dulce [mas_get_player_nickname()]! ¡Siempre me haces sentir muy especial!"),
        _("Aww, ¡Gracias [player]!"),
    ]


    thanks_quip = renpy.substitute(renpy.random.choice(thanking_quips))

    def compliment_delegate_callback():
        """
        A callback for the compliments delegate label
        """
        global thanks_quip
        
        thanks_quip = renpy.substitute(renpy.random.choice(thanking_quips))
        store.mas_gainAffection()

init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="mas_compliment_gorgeous",
            prompt="Hoy estás preciosa, [m_name]",
            unlocked=True
        ),
        code="CMP"
    )

label mas_compliment_gorgeous:
    if not renpy.seen_label("mas_compliment_gorgeous_2"):
        call mas_compliment_gorgeous_2 from _call_mas_compliment_gorgeous_2
    else:
        call mas_compliment_gorgeous_3 from _call_mas_compliment_gorgeous_3
    return

label mas_compliment_gorgeous_2:
    $ mas_gainAffection(5,bypass=True)
    m 1hub "Ehehe, gracias [player]~"
    m 1eua "Apuesto a que siempre te ves increíble."
    m 1ekbsa "Te amo~"
return "love"

label mas_compliment_gorgeous_3:
    m 1eub "[mas_compliments.thanks_quip]"
    m 1hua "¡Apuesto a que te ves mucho mejor!"
    m "Ehehe~"
return

init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="mas_compliment_sweetgirl",
            prompt="Eres la chica más dulce que he conocido, [m_name]",
            unlocked=True
        ),
        code="CMP"
    )

label mas_compliment_sweetgirl:
    if not renpy.seen_label("mas_compliment_sweetgirl_2"):
        call mas_compliment_sweetgirl_2 from _call_mas_compliment_sweetgirl_2
    else:
        call mas_compliment_sweetgirl_3 from _call_mas_compliment_sweetgirl_3
    return

label mas_compliment_sweetgirl_2:
    $ mas_gainAffection(5,bypass=True)
    m 1hub "Ehehe gracias [player]~"
    m "Te amo~"
return "love"

label mas_compliment_sweetgirl_3:
    m 1hub "[mas_compliments.thanks_quip]"
    m "Ehehe~"
return