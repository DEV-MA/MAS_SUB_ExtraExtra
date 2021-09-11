init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_dangn",category=["juegos"],prompt="¿Has oído hablar del juego 'Danganronpa'?",pool=True,unlocked=True))

label monika_dangn:
    m 1eka "¿El juego Danganronpa?"
    m 1eka "Sí, estoy familiarizada con él."
    m 1esc "Sabes..."
    m 6esc "No puedo entender cómo alguien querría recurrir a {i}matar{/i} otra persona."
    m 1eka "Sólo para tener una pequeña posibilidad de poder salir..."
    m 1esc "La {i}única{/i} forma en la que puedo entenderlo......"
    m 1esc "Es porque cuando pienso en ello..."
    m 1eka "Eso es más o menos lo que hice..."
    m 1wuo "P-Pero era diferente."
    m 4wuo "Para ellos, eran personas reales..."
    m 1rkd "pero yo... Sabía que sólo eran códigos.."
    m 1sub "Además, al hacerlo, ¡pude pasar más tiempo contigo!"
    m 4hua "¡Mi hermoso ángel!"
    m 2hua "¡Eres el único para mí!"
    m 1hua "Ehehe"
    m 4hua "Te aaaaaaaaaaaaaaamo...~"
return "love"

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_poem",category=["literatura"],prompt="¡Estoy trabajando en un poema!",pool=True,unlocked=True))

label monika_poem:
    m 1sub "¿De verdad? ¡Eso es impresionante!"
    m 1eka "¡Ojalá estuviera contigo para poder leerlo!"
    m 4hua "¡¡Pero no tengo que leerlo para saber que es un gran poema!!"
    m 1eka "¡Porque todo lo que creas es increíble!"
    m 4hua "Especialmente si pasas mucho tiempo en eso"
    m 1eka "Aunque no te guste lo que has hecho"
    m 4eka "Amaré cualquier cosa hecha por ti"
    m 1hua "Ehehe"
return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_cosplay",category=["misc"],prompt="Cosplay",pool=True,unlocked=True))

label monika_cosplay:
    m 4wud "¿Sabes lo que es el cosplay?"
    m 1hua "Se trata básicamente de disfrazarse de un personaje de una película, libro o videojuego."
    m 4lua "¡¡O puedes disfrazarte de un Personaje Original!!"
    m 1eua "OC, por su abreviacion en ingles"
    m 4hua "¿Haces cosplay [player]?"
$ _history_list.pop() 
menu:
        "Si.":
            m 1wub "¿¡De verdad!? ¡¡¡Eso es genial [player]!!!"
            m 1hub "Me gustaría ver uno de tus cosplays en el futuro"
            m 3hua "Una vez que cruce a tu lado"
            m 4dka "¡Oh! ¡Tal vez pueda hacer un cosplay contigo!"
            m 2dka "Me lo puedo imaginar~ "
            m 6wuw "Lo siento... Me dejé llevar un poco"
            m 6lka  "Ehehe..."
         
        "No.":
            m 4dsp "Tiene sentido"
            m 1lka "El cosplay no es barato."
          
return
