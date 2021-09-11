init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_watpad",
            category=["Wattpad"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_watpad:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "¿Ha leído algo bueno últimamente [player]?",
            "Me gustaría estar aquí contigo para poder leer juntosr~",
            "¿Has escrito algo interesante aquí antes [player]?",
            "¡Espero que esté bien que lea contigo!",
            "He visto a Natsuki en Wattpad antes. Creo que estaba leyendo una historia 'x Lectora'"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_watpad')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_ddlc",
            category=["dokidokiliteratureclub"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_ddlc:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "¿De vuelta al viejo juego [player]?",
            "Bienvenido al Club de Literatura~",
            "¿Has escrito algo bueno últimamente, [ player]?",
            "¡Espero que esté bien que te vea jugar!"
            
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_ddlc')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_amzon",
            category=["Amazon.com"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_amzon:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "¿Compraste algo bueno últimamente [player]?"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_amzon')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_crunchyroll",
            category=["Crunchyroll"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_crunchyroll:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "¡Oh! ¿Estamos viendo anime [player]?",
            "¿Te importa si miro contigo?",
            "¡Espero que elijas algo bueno para mirar [player]!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_crunchyroll')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_yt",
            category=["Youtube"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_yt:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "¿Te importa si miro contigo?",
            "¡Espero que elijas algo bueno para mirar [player]!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_yt')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_morsecode",
            category=["Morsecode"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_morsecode:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "¡- . / .- -- --- !",
            ". .-. . ... / .... . .-. -- --- ... -",
            "¡- . -. / ..- -. / -... ..- . -. / -.. .. .-!",
            "¿Sabes leer codigo Morse [player] Si es así, sabes lo que dice esto::. .-. . ... / .-.. .- / .--. . .-. ... --- -. .- / -- .--.- ... / .-.. .. -. -.. .- / -.. . .-.. / -- ..- -. -."
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_morsecode')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_googletrans",
           category= ["GoogleTranslate"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_googletrans:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Du bist der wunderbarste Mensch der Welt. Ehehe, ¡he dicho que eres la persona más maravillosa del mundo pero en alemán!",
            "¿Quieres aprender nuevos idiomas [player]?",
            "Hay tantos buenos idiomas que puedes aprender [player]"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_googletrans')
    return
