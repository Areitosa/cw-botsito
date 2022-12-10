# pyTeleGame Bot
El presente git continene el codigo fuente utilizado para ayudar con Bastion + CW

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/CesarJER/pyBots/tree/master)


## Colaboradores
<b>Principal:</b> [@cmee123](https://t.me/cmee123)
Colaboración: [@GrayFang](https://t.me/GrayFang)

Tester: [@WednesdayAdam](https://t.me/WednesdayAdam)
## Comandos

### Módulo BS
El bot se controla desde [@DRKyEKE_helpbot](https://t.me/@DRKyEKE_helpbot):
- `AA` desactiva/activa la busqueda automática de ataques
- `Buy` gasta el dinero comprando recursos
- `Up` 
    - Si va solo muestra el edificio que se busca actualizar ahora
    - Si va precedido de un emoji (edificio) modifica el edificio a actualizar
    - Para desactivarlo poner un emoji falso (p.ej 📙, 😃,💁,👌,🎍,😍...)
- `War` realiza 1 búsqueda de ataque automática (solo funciona con la función de busqueda automática activada)

Los comandos son no case-sensible (acepta MAYUSCULAS y minusculas)
```diff
- ¡¡IMPORTANTE!! NO OLVIDARSE DE APAGAR AA cada X tiempo. Hay un antibot que sospecharía...

! ¡¡REQUIERE MAYORDOMO PARA TODAS LAS FUNCIONES!!
```
### Módulo CW
Para el uso de la app ha de activarse el bot [@mad_witch_bot](https://t.me/mad_witch_bot) y hacer uso de sus comandos para el manejo de las siguientes fucionalidad referentes a CW:

- Fijos:
    - /go
    - /pledge
    - Solicitar ayuda ambush en el grupo de órdenes reenviando el mensaje del ambush
    - /report en [@mad_witch_bot](https://t.me/mad_witch_bot) da el estado de las funciones  

- Configurables (on/off):
    - Autoarena (/arena, fastfight loop)
    - Autoquest (/aq, cada 8 min loop y se puede escoger a donde ir con /quest y luego el texto del quest)
    - Órdenes automáticas (/ordenes, toma las órdenes que manda al chat de ordenes el GC el cual las Lee del squad)
    - Asistencia en las ambush (/ambush, Envía el mensaje de ayuda del chat de ordenes al CW)
    - Caza de mobs (/caza, Captura las fight del pve y del chat de fight de owl que estén en tu rango, con /level [tu level] fijas rango ej /level 23 y toma -9 y +3 fight o sea de lvl 14 a 26)

- Especiales (Solo se aplican a algunos usuarios)
    - Funciones GC (/g_invite automático, avisar con /everyone en ambush, mandar órdenes de batalla)
    - Funciones del BS (Abre la tienda un tiempo que oscila entre 6 minutos y 10 minutos luego de los resultados de cada batalla, así como en cualquier momento con el comando #open_link

## Cosas por hacer:
Las cosas por arreglar proximamente:
TO DO:
- [X] Reenvio automático de batalla al bot (BSA)
- [X] /dig automática (DEBE activarse manualmente diariamente)
    - [ ] Activar automáticamente cada X tiempo.
- [X] Relleno automático y reparación en batalla
    - [ ] Falta hacer más relleno si hay mucha diferencia.
- [X] Búsqueda y ataque automáticos
    - [ ] Incluir selección de karma
    - [ ] incluye optimización BSA en lugar de karma
- [ ] Unión automática a AA
    - [ ] Control por medio del chat de la alianza
- [ ] Gasto automático de oro
    - [X] función buy_item () para comprar recursos
    - [X] Función de actualización automática (`Up`)
- [ ] Hacer un manual de funciones (tal vez con ´´Help´´ o ´´Ayuda´´)
