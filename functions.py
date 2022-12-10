class main:
    def __init__(self, api_id, api_hash, api_session, CW_ids:dict={}):
        import logging
        log = logging.getLogger()
        
        self.api_id = api_id
        self.api_hash = api_hash
        self.api_session = api_session

        from pyrogram import Client, MessageHandler, Filters
        from pyrogram.api import functions
        from numpy.random import randint
        
        import re
        import time
        from datetime import datetime
        import os
        import random
        from pyrogram.errors import AuthKeyUnregistered, MessageIdInvalid, AuthKeyDuplicated

        app = Client(api_session, api_id, api_hash)
        try:
            app.start()
        except AuthKeyUnregistered:
            log.warning("Han desactivado este HASH: "+api_session)
            return
        except AuthKeyDuplicated:
            raise Exception("ERROR!! HASH DUPLICADO" + api_session)
        ids = {}

        """
        CW CODE
        """

        ids["CW"] = 408101137 #game
        ids["helper"] = 1360129753
        ids["Caza"] = 807376493
        ids["Reports"] = -1001108112459
        ids["craft_daniel"] = -487602549
        ids["angry_birds"] = 833409972
        ids["Caza_moon"] = -1001408823679
        ids["Waifu"] = 1976201765

        try:
            ids.update(CW_ids)
        except:
            log.warning("CW_ids not found or is an incorrect dict")
        
        me=app.get_me()
        me.username = me.username if me.username else me.first_name
        
        auto_quest=False
        caza=True if (me.id == 714046873) else False
        hp = 700
        quest = "🍄Swamp"
        level=100
        leer_level = True
        ff=True
        ambush=True
        Blacksmith =True if (me.id == 855272604) else False
        gast_stmn=True
        sentinela = True if (me.id == 836357204) else False
        tactics = "/tactics_moonlight"
        cod_trader = "09" if me.id == 873541475 else "41"
        knight = True if (me.id == 668189411) else False
        collector = True if (me.id == 876771760) else False
        alch = True if (me.id == 714046873) else False
        ranger = True if (me.id == 434324721) else False
        ordenes = False if ranger else True
        tregua = False
        rango_max = 6
        dice = False
        stamina_alt = False
        taberna = False
        orden_adelantada = True
        defensores = True if (me.id == 954888757) else False
        apuntar = True
        contratar_adv = False
        cod_adv = 'abcd'
        advisor = "Strategist"
        tesorero = True if me.id == 859343342 else False
        pet = True if me.id == 859343342 else False
        pasador = True if me.id == 859343342 else False
        pasapasa = False
        cazador = True if ((me.id == 859343342) or (me.id == 843329755) or (me.id == 714046873)) else False
        dadero = True if me.id == 714046873 else False
        ateder_pet = False
        ciclo_quest = True
        habilidad = False if me.id == 926174535 else True
        enviar_caza = True  
        waifus = True
        fast_waifu = False
        waifu_notif = True
        aux_fast_waifu = False       

        import time 


        def cazar(mensaje):
            nonlocal level, ids, rango_max
            has_link = False
            if mensaje.edit_date: return None
            if re.search("lvl\.([0-9]+)", mensaje.text):
                mob_info = int(re.findall("lvl\.([0-9]+)", mensaje.text)[0])
                log.info (mob_info)
            else:
                mob_info = 999
                log.info ('No level encontrado en caza')
            
            if mensaje.reply_markup:
                if mensaje.reply_markup.inline_keyboard:
                    if re.search("(\/fight_[A-z0-9]+)",mensaje.reply_markup.inline_keyboard[0][0].url):
                        has_link=re.search("(\/fight_[A-z0-9]+)",mensaje.reply_markup.inline_keyboard[0][0].url).group()
            
            if int(level-9)< mob_info < int(level+rango_max):
                if re.search("an ambush\!", mensaje.text):
                    if GC or int(level)>mob_info:
                        if has_link:
                            app.send_message(ids["CW"], str(has_link))
                        else:
                            mensaje.forward(ids["CW"])
                    else:
                        time.sleep(abs(int(level)-mob_info))
                        if has_link:
                            app.send_message(ids["CW"], str(has_link))
                        else:
                            mensaje.forward(ids["CW"])
                else:
                    if has_link:
                        app.send_message(ids["CW"], str(has_link))
                    else:
                        mensaje.forward(ids["CW"])

        def reporte():
            nonlocal ids, app, ordenes, auto_quest, caza, level, quest, ff, ambush, Blacksmith, gast_stmn, sentinela, tactics, cod_trader, dice, apuntar, advisor, pet, tesorero, log
            app.send_message(ids["helper"], "Hola, las funciones de ayuda al CW están activadas"+"\n"+
                 ("El autoquest a "+str(quest)+" está activado" if auto_quest else "El autoquest está desactivado")+"\n"+
                 ("El tipo de advisor a contratar fijado es "+advisor+"\n" if tesorero else "")+ 
                 ("Las órdenes automáticas están activadas" if ordenes else "Las órdenes automáticas están desactivadas")+"\n"+
                 ("Captarás las órdenes adelantadas de Ranger" if apuntar else "No captarás las órdenes adelantadas de Ranger")+"\n"+
                 ("La caza de mobs está activada" if caza else "La caza de mobs se encuentra desactivada")+"\n"+
                 "El level medio para la caza y ayuda en ambush fijado es: "+str(level)+"\n"+
                 ("La autoarena está activada" if ff else "La autoarena está desactivada")+"\n"+
                 ("La ayuda a las ambush está activada" if ambush else "La ayuda a las ambush está desactivada")+"\n"+
                 ("Se activará el loop de quest cuando se llene la stamina" if gast_stmn else "No se activará el loop de quest cuando se llene la stamina")+"\n"+
                 ("El trader se encuentra activado con el recurso: "+cod_trader +"\n" if sentinela else "")+
                 ("Las tactics fijadas son: "+tactics +"\n" if sentinela else "")+
                 ("El loop de los dados se encuentra activado" if dice else "El loop de los dados se encuentra desactivado")+"\n"+
                 ("Looteo de waifus activado" if waifus else "Looteo de waifus desactivado")+"\n"+
                 ("Autoplay rápido para Looteo de waifus activado" if fast_waifu else "Autoplay rápido para Looteo de waifus desactivado")+"\n"+
                 ("La diversión y el baño de tu mascota está en mis manos 😘"+"\n" if pet else ""))

 
        def mascota():
            nonlocal ids, app, pet, log
            timer = randint(1, 60) 
            while pet:
                app.send_message(ids["CW"], "/pet")
                time.sleep(2)
                app.send_message(ids["CW"], "⚽Play")
                time.sleep(2)
                i = 0
                while (i < 6):
                    app.send_message(ids["CW"], "🛁Clean")
                    i += 1
                    time.sleep(2)                
                time.sleep(7200+timer) 




        def selector_CW(message):
            nonlocal ids, app, ordenes, auto_quest, caza, level, quest, ff, ambush, Blacksmith, sentinela, tactics, cod_trader, knight, collector, ranger, alch, tregua, rango_max, dice, taberna, orden_adelantada, defensores, apuntar, contratar_adv, cod_adv, advisor, tesorero, pet, pasapasa, pasador, hp, cazador, dadero, leer_level, ateder_pet, ciclo_quest, habilidad, enviar_caza, waifus, fast_waifu, waifu_notif, aux_fast_waifu, log
                  
            mensaje = message
            timer = randint(3, 7)
            tiempo = randint(7, 60)
            open_shop = randint(400,800)
            tiempo_or = randint(5,600)
            timer_aq = randint(1, 60) 
            timer_rep = randint (1, 7200)
            random_number = randint (1, 3)


            if (mensaje.chat.id==ids["CW"]) and (mensaje.from_user.id==ids["CW"]): #Game
                if "Congratulations! You are still alive." in mensaje.text: #Para que cuando llegue de un ambush diga con /f_report cómo fue la batalla y con /whois quién ayudo 
                    app.send_message(ids["CW"], '/f_report')
                    time.sleep(timer)  
                    mensaje.reply('/whois')
                 #   if cazador:
                 #       time.sleep(timer)
                   #     app.send_message(ids["CW"], "🏅Me")

                elif "This is sad but You are nearly dead." in mensaje.text: #Para que cuando llegue de un ambush diga con /f_report cómo fue la batalla y con /whois quién ayudo 
                    app.send_message(ids["CW"], '/f_report')
                    time.sleep(timer)  
                    mensaje.reply('/whois')
                  #  if cazador:
                   #     time.sleep(timer)
                   #     app.send_message(ids["CW"], "🏅Me")

                elif ('You were strolling around on your horse' in mensaje.text): # El más importante para que cuando llegue un foray de alguien más responda /go
                    if auto_quest:
                        auto_quest = False
                        time.sleep(tiempo)
                        mensaje.click(0)
                        auto_quest = True
                        time.sleep(timer+5)
                        app.send_message(ids["CW"], '🗺Quests')
                    else:
                        time.sleep(tiempo)
                        mensaje.click(0)

                elif '/pledge' in mensaje.text: # Para que cuando llegue un pledge a un knight lo coja
                    mensaje.reply('/pledge')
                elif 'Leaderboard of fighters' in mensaje.text and ff: # Loop para ir a la arena cuando da resultado de arena
                    time.sleep(timer)  
                    mensaje.reply('▶️Fast fight')
                elif 'You didn’t find an opponent. Return later.' in mensaje.text and ff:
                    time.sleep(timer)
                    mensaje.reply('▶️Fast fight')

                elif 'be back in' in mensaje.text and ciclo_quest:
                    time_enquest = int(re.findall("be back in (\d+)", mensaje.text)[0])
                    time.sleep(15+time_enquest*60)
                    time.sleep(timer)
                    mensaje.reply('🗺Quests')

                elif 'Many things can happen in the forest.' in mensaje.text and auto_quest:
                    if ranger:
                        if ('🌲Forest 4min 🔥' in mensaje.text) or ('🌲Forest 6min 🔥' in mensaje.text):
                            quest = '🌲Forest'
                        elif ('🍄Swamp 5min 🔥' in mensaje.text) or ('🍄Swamp 7min 🔥' in mensaje.text):
                            quest = '🍄Swamp'
                        elif ('🏔Mountain Valley 5min 🔥' in mensaje.text) or ('🏔Mountain Valley 7min 🔥' in mensaje.text):
                            quest = '⛰️Valley'
                    time.sleep(timer)
                    mensaje.click(quest)
                elif 'Stamina restored. You are ready for more adventures!' in mensaje.text and gast_stmn:
                    auto_quest=True
                    time.sleep(timer)
                    app.send_message(ids["CW"], '🗺Quests')

                elif ciclo_quest and (("You have satisfied your lust for violence and left back home." in mensaje.text) or ("Village was successfully pillaged." in mensaje.text) or ("You crawled back home to a nice warm bath." in mensaje.text)):
                    time.sleep(timer+5)
                    app.send_message(ids["CW"], '🗺Quests') 

                elif "You can track /tributes that they supplied you with" in mensaje.text:
                    auto_quest=False  
                    
                elif 'You took a pint of cold ale.' in mensaje.text and taberna:
                    time_enquest = int(re.findall("You will finish your drink in (\d+)", mensaje.text)[0])
                    time.sleep(13+time_enquest*60)
                    app.send_message(ids["CW"], '🍺Have a pint') 

                elif (re.search("🏅Level: ([0-9]+)", mensaje.text)) and ('Battle of the seven castles in' in mensaje.text):
                    hp = int(re.findall("Hp\:.([0-9]+)", mensaje.text)[0])
                    if leer_level:
                        level = int(re.findall("🏅Level: ([0-9]+)", mensaje.text)[0])
                   # if cazador: 
                     #   if hp < 500:
                       #     caza = False
                       #     time.sleep(1800+timer_aq)
                       #     app.send_message(ids["CW"], "🏅Me")
                    #    else:
                     #       caza = True
                    if re.search("(.)+ /pet", mensaje.text) and ateder_pet:
                        pet = True
                        pet_status = re.findall("(.)+ /pet", mensaje.text)[0]
                        if pet_status != "😁":
                            app.send_message(ids["CW"], "/pet")
                        time.sleep(3600+timer_aq)
                        app.send_message(ids["CW"], "🏅Me")

                elif "Food supply:" in mensaje.text and ateder_pet:
                    play_status = re.findall("⚽ +(..)", mensaje.text)[0]
                    food_status = re.findall("🍼 +(..)", mensaje.text)[0]
                    bath_status = re.findall("🛁 +(..)", mensaje.text)[0]
            
                    if play_status != "pe":
                        app.send_message(ids["CW"], "⚽Play")
                    if food_status != "pe":
                        time.sleep(2)
                        app.send_message(ids["CW"], "🍼Feed")
                    if bath_status != "pe":
                        time.sleep(4)
                        app.send_message(ids["CW"], "🛁Clean")
                           

                elif re.search("carry ([0-9]+)", mensaje.text.lower()) and sentinela:
                    carry = int(re.findall("carry ([0-9]+)", mensaje.text.lower())[0])
                    app.send_message(ids["CW"], "/sc "+str(cod_trader)+" "+str(carry))

                elif 'won! - he takes' in mensaje.text and dice and dadero:
                    app.send_message(ids["CW"], '🎲Play some dice') 

                elif 'Recipient shall send to bot:' in mensaje.text and pasapasa:
                    if pasador:
                       # mensaje.forward(ids["spam_LDC"])
                        pasapasa = False
                     
                elif ("lvl.1 "+advisor) in mensaje.text and tesorero:
                    contratar_adv = False
                    cod_adv = re.findall("\/adv_(....).*lvl.1 "+advisor, mensaje.text)[0]
                    app.send_message(ids["CW"], "/g_hire "+cod_adv)

                elif ('🔰Level: 1' in mensaje.text) and tesorero:
                    time.sleep(2)
                    app.send_message(ids["CW"], '/g_hire '+cod_adv)

                elif "Class info: /class" in mensaje.text:
                    if (re.search(".+?🏹.+?Class info: /class", mensaje.text)) or (re.search("🏹.+?Class info: /class", mensaje.text)) or (re.search("🏹+Class info: /class", mensaje.text)):
                        ranger = True
                    else:
                        ranger = False

                    if (re.search(".+?⚔.+?Class info: /class", mensaje.text)) or (re.search("⚔.+?Class info: /class", mensaje.text)) or (re.search("⚔+Class info: /class", mensaje.text)):
                        knight = True  
                    else:
                        knight = False                

                    if (re.search(".+?🛡.+?Class info: /class", mensaje.text)) or (re.search("🛡.+?Class info: /class", mensaje.text)) or (re.search("🛡+Class info: /class", mensaje.text)):
                        sentinela = True
                    else:
                        sentinela = False
                    
                    if (re.search(".+?⚗️.+?Class info: /class", mensaje.text)) or (re.search("⚗️.+?Class info: /class", mensaje.text)) or (re.search("⚗️+Class info: /class", mensaje.text)):
                        alch = True
                    else:
                        alch = False
                    
                    if (re.search(".+?📦.+?Class info: /class", mensaje.text)) or (re.search("📦.+?Class info: /class", mensaje.text)) or (re.search("📦+Class info: /class", mensaje.text)):
                        collector = True
                    else:
                        collector = False
                    
                    if (re.search(".+?⚒.+?Class info: /class", mensaje.text)) or (re.search("⚒.+?Class info: /class", mensaje.text)) or (re.search("⚒+Class info: /class", mensaje.text)):
                        Blacksmith = True
                    else:
                        Blacksmith = False
                    
                    time.sleep(timer)
                    app.send_message(ids["helper"], "Clase/es registrada: "+"\n"+("-Ranger"+"\n" if ranger else "")+("-Knight"+"\n" if knight else "")+("-Sentinel"+"\n" if sentinela else "")+("-Alchemist"+"\n" if alch else "")+("-Collector"+"\n" if collector else "")+("-Blacksmith"+"\n" if Blacksmith else ""))
                    
 


            elif mensaje.chat.id==ids["Reports"]:
                if ('Scores:' in mensaje.text):
                    time.sleep(timer+420)
                    app.send_message(ids["CW"], '/report')
                    
                    if cazador:
                        time.sleep(timer)
                        app.send_message(ids["CW"], "🏅Me")
                    if Blacksmith:
                        time.sleep(timer)
                        app.send_message(ids["CW"], '/myshop_open')
                    if habilidad:
                        if (sentinela) and (level > 49):
                            time.sleep(timer)
                            app.send_message(ids["CW"], '/use_tnt')
                        if (knight) and (level > 49):
                            time.sleep(timer)
                            app.send_message(ids["CW"], '/use_cry')
                        if (collector) and (level > 49):
                            time.sleep(timer)
                            app.send_message(ids["CW"], '/use_crl')  
                    if pet:
                        time.sleep(timer+450)
                        app.send_message(ids["CW"], '⚽Play') 
                        time.sleep(2)
                        i = 0
                        while (i < 6):
                            app.send_message(ids["CW"], "🛁Clean")
                            i += 1
                            time.sleep(2)



            elif mensaje.chat.id==ids["Waifu"] and waifus:
                if ("WHICH NUMBER DO YOU SEE IN THE IMAGE?" in mensaje.caption):
                    mensaje.click(random_number-1)
                elif "❌ Answer INCORRECT! ❌" in mensaje.text:
                    time.sleep(joda+30)
                    app.send_message(ids["Waifu"], "🎟")
                     
                elif "✅ Answer Correct! ✅" in mensaje.text:
                    time.sleep(joda)
                    app.send_message(ids["Waifu"], "🎟")
                elif "⚠️ You did not answer! ⚠️" in mensaje.text:
                    time.sleep(joda+60)
                    app.send_message(ids["Waifu"], "/start")
                    time.sleep(joda)
                    app.send_message(ids["Waifu"], "PLAY NOW! 🎟")
                    time.sleep(joda)
                    app.send_message(ids["Waifu"], "🎟") 
                       
                elif not waifu_notif:
                    if ("🎰" in mensaje.text) and aux_fast_waifu:
                        time.sleep(joda)
                        app.send_message(ids["Waifu"], "🎟")
                    elif "You have 0 tickets left," in mensaje.text:
                        aux_fast_waifu = False
                        time.sleep(14400+timer)
                        app.send_message(ids["Waifu"], "Back 🔙")
                        time.sleep(joda)
                        app.send_message(ids["Waifu"], "PLAY NOW! 🎟")
                        aux_fast_waifu = True
                    #    while aux_fast_waifu:
                     #       time.sleep(joda+5)
                        app.send_message(ids["Waifu"], "🎟")

                elif fast_waifu:
                    
                    if ("Unlucky :(  Try again! 🎰🍀" in mensaje.text) or ("🎉🏆 YOU WON! 🏆🎉" in mensaje.text) and not aux_fast_waifu:
                        app.send_message(ids["Waifu"], "Back 🔙")
                        time.sleep(joda)
                        app.send_message(ids["Waifu"], "PLAY NOW! 🎟")
                        time.sleep(joda)
                        app.send_message(ids["Waifu"], "Fast Autoplay 🎟🔄")
                        
                    elif "Click below to activate fast autoplay👇" in mensaje.text:
                        mensaje.click(0)
                        aux_fast_waifu = True
                    elif ("Autoplay disabled ❌🔄" in mensaje.text) or ("You have 0 tickets left," in mensaje.text):  
                        aux_fast_waifu = False
                        time.sleep(14400+timer)
                        app.send_message(ids["Waifu"], "Back 🔙")
                        time.sleep(joda)
                        app.send_message(ids["Waifu"], "PLAY NOW! 🎟")
                        time.sleep(joda)
                        app.send_message(ids["Waifu"], "Fast Autoplay 🎟🔄")

                else:
                    if ("Unlucky :(  Try again! 🎰🍀" in mensaje.text) or ("🎉🏆 YOU WON! 🏆🎉" in mensaje.text):
                        time.sleep(joda)
                        app.send_message(ids["Waifu"], "🎟")
                    elif "You have 0 tickets left," in mensaje.text:
                        time.sleep(14400+timer)
                        app.send_message(ids["Waifu"], "Back 🔙")
                        time.sleep(joda)
                        app.send_message(ids["Waifu"], "PLAY NOW! 🎟")
                        time.sleep(joda)
                        app.send_message(ids["Waifu"], "🎟")

            
            elif mensaje.chat.id==ids["craft_daniel"]:
                if ("Crafteo" in mensaje.text):
                    time.sleep(timer_rep)
                    if Blacksmith:
                        if level<22:
                            if level % 2 == 0:
                                i=0
                            else:
                                i=-1
                        elif level<38:
                            if level % 2 == 0:
                                i=1
                            else:
                                i=0
                        elif level<48:
                            i=2
                        else:
                            i=3
                    elif collector or alch:
                        if level % 2 == 0:
                            i=0
                        else:
                            i=-1
                    else:
                        i=5
                    while (i < 5):
                        i += 1
                        app.send_message(ids["CW"], "/c_21")
                        time.sleep(2)
                    if alch:
                        if level<26:
                            if level % 2 == 0:
                                i=0
                            else:
                                i=-1
                        elif level<48:
                            if level % 2 == 0:
                                i=1
                            else:
                                i=0
                        elif level<52:
                            i=2
                        else:
                            i=3

                        while (i < 5):
                            app.send_message(ids["CW"], "/brew_509")
                            i += 1
                            time.sleep(2)  
               
                if ("Arena" in mensaje.text): 
                    time.sleep(timer_rep)            
                    app.send_message(ids["CW"], "▶️Fast fight")   
                              
            
            elif caza and cazador and mensaje.chat.id==ids["Caza"] and ("Prepare yourself to fight:" in  mensaje.text):
                rango_max = 10
                cazar(mensaje)

            elif caza and cazador and mensaje.chat.id==ids["Caza_moon"] and ("Be careful:" in  mensaje.text):
                rango_max = 10
                cazar(mensaje)

             

                         
         #   elif caza and cazador and mensaje.chat.id==ids["angry_birds"]:        
           #     if not mensaje.edit_date and mensaje.reply_markup.inline_keyboard:
              #      enviar_caza = True
              #      mensaje.click(0)
              #  elif ("/fight" in  mensaje.text):
               #     mensaje.forward(ids["CW"])
               #     enviar_caza = False
                  #  rango_max = 10
                 #   rango_max = 10
                 #   cazar(mensaje)
                   
  

            elif mensaje.chat.id==ids["helper"]: 
                if ('#advisor_on' in mensaje.text) and tesorero:
                    contratar_adv = True
                    i = 0
                    while (i < 200) and contratar_adv:
                        app.send_message(ids["CW"], '/advlist')
                        i += 1
                        time.sleep(1)
                    contratar_adv = False
                    
                elif '#advisor_off' in mensaje.text and tesorero:
                    contratar_adv = False

                elif re.search("level ([0-9]+)", mensaje.text.lower()):
                    level = int(re.findall("level ([0-9]+)", mensaje.text.lower())[0])
                    leer_level = False
                    app.send_message(ids["helper"], "Level para caza registrado: "+str(level))

                elif re.search("sc ([0-9]+)", mensaje.text.lower()) and sentinela:
                    cod_trader = re.findall("sc ([0-9]+)", mensaje.text.lower())[0]
                    app.send_message(ids["helper"], "Recurso a vender al trader  registrado: "+cod_trader)
           
                elif "/aq"==mensaje.text.lower():
                    auto_quest = not auto_quest
                    app.send_message(ids["helper"], "Autoquest activado" if auto_quest else "Autoquest desactivado")
                elif 'swamp'==mensaje.text.lower():
                    quest='🍄Swamp'
                    time.sleep(2)
                    app.send_message(ids["helper"], "Información de quest actualizada: "+quest)
                elif 'forest'==mensaje.text.lower():
                    quest='🌲Forest'
                    time.sleep(2)
                    app.send_message(ids["helper"], "Información de quest actualizada: "+quest)
                elif 'valley'==mensaje.text.lower():
                    quest='⛰️Valley'
                    time.sleep(2)
                    app.send_message(ids["helper"], "Información de quest actualizada: "+quest)
                elif 'foray'==mensaje.text.lower():
                    quest='🗡Foray'
                    time.sleep(2)
                    app.send_message(ids["helper"], "Información de quest actualizada: "+quest)
 
                elif 'strategist'==mensaje.text.lower() and tesorero:
                    advisor='Strategist'
                    time.sleep(2)
                    app.send_message(ids["helper"], "Información del advisor a contratar actualizada: "+advisor)
                elif 'jaeger'==mensaje.text.lower() and tesorero:
                    advisor='Jaeger'
                    time.sleep(2)
                    app.send_message(ids["helper"], "Información del advisor a contratar actualizada: "+advisor)
                elif 'scout'==mensaje.text.lower() and tesorero:
                    advisor='Scout'
                    time.sleep(2)
                    app.send_message(ids["helper"], "Información del advisor a contratar actualizada: "+advisor)

                elif "/waifu"==mensaje.text.lower():
                    waifus = not waifus
                    app.send_message(ids["helper"], "Looteo de waifus activado" if waifus else "Looteo de waifus desactivado")
                elif "/fast_waifu"==mensaje.text.lower():
                    fast_waifu = not fast_waifu
                    app.send_message(ids["helper"], "Looteo rápido de waifus activado" if fast_waifu else "Looteo rápido de waifus desactivado")


                elif "/ff"==mensaje.text.lower():
                    ff = not ff
                    app.send_message(ids["helper"], "La autoarena está activada" if ff else "La autoarena está desactivada")

                elif "/ambush"==mensaje.text.lower():
                    ambush = not ambush
                    app.send_message(ids["helper"], "La ayuda a las ambush está activada" if ambush else "La ayuda a las ambush está desactivada")
                elif "/ordenes"==mensaje.text.lower():
                    ordenes = not ordenes
                    app.send_message(ids["helper"], "Las órdenes automáticas están activadas" if ordenes else "Las órdenes automáticas están desactivadas") 
                elif "/apuntar"==mensaje.text.lower():
                    apuntar = not apuntar
                    app.send_message(ids["helper"], "Las órdenes adelantadas están activadas" if apuntar else "Las órdenes adelantadas están desactivadas")        
                elif 'moon'==mensaje.text.lower() and sentinela:
                    tactics='/tactics_moonlight'
                    time.sleep(2)
                    app.send_message(ids["helper"], "Tactics actualizadas: "+tactics)  
                elif 'potato'==mensaje.text.lower() and sentinela:
                    tactics='/tactics_potato'
                    time.sleep(2)
                    app.send_message(ids["helper"], "Tactics actualizadas: "+tactics)
                elif 'eagle'==mensaje.text.lower() and sentinela:
                    tactics='/tactics_highnest'
                    time.sleep(2)
                    app.send_message(ids["helper"], "Tactics actualizadas: "+tactics)  
                elif 'deer'==mensaje.text.lower() and sentinela:
                    tactics='/tactics_deerhorn'
                    time.sleep(2)
                    app.send_message(ids["helper"], "Tactics actualizadas: "+tactics)
                elif 'shark'==mensaje.text.lower() and sentinela:
                    tactics='/tactics_sharkteeth'
                    time.sleep(2)
                    app.send_message(ids["helper"], "Tactics actualizadas: "+tactics)
                elif 'dragon'==mensaje.text.lower() and sentinela:
                    tactics='/tactics_dragonscale'
                    time.sleep(2)
                    app.send_message(ids["helper"], "Tactics actualizadas: "+tactics)
                elif 'wolf'==mensaje.text.lower() and sentinela:
                    tactics='/tactics_wolfpack'
                    time.sleep(2)
                    app.send_message(ids["helper"], "Tactics actualizadas: "+tactics)
                elif "/dados"==mensaje.text.lower():
                    dice = not dice
                    app.send_message(ids["helper"], "El loop de los dados se encuentra activado" if dice else "El loop de los dados se encuentra desactivado") 
                elif "/quest"==mensaje.text.lower():
                    ciclo_quest = not ciclo_quest
                    app.send_message(ids["helper"], "Está puesto el mandar quest rishiño" if ciclo_quest else "Ya te quite el mensaje de quest rishiño")
                elif "/taberna"==mensaje.text.lower():
                    taberna = not taberna
                    app.send_message(ids["helper"], "El loop de taberna está activado" if taberna else "El loop de taberna se encuentra desactivado")
                elif "/skill_adv"==mensaje.text.lower():
                    habilidad = not habilidad
                    app.send_message(ids["helper"], "La activación de las habilidades level 50+ de la clase están activadas" if habilidad else "La activación de las habilidades level 50+ de la clase están desactivadas")

                elif "/mascota"==mensaje.text.lower():
                    pet = not pet
                    app.send_message(ids["helper"], "You are now the proud owner of a cute pet" if pet else "You just kill your pet I hope you feel great about it")
                    if pet:
                        mascota()
                elif "/report"==mensaje.text.lower():
                    reporte()           
   

                elif "/caza"==mensaje.text.lower() and cazador:
                    caza = not caza
                    app.send_message(ids["helper"], "La caza de mobs se encuentra activada" if caza else "La caza de mobs se encuentra desactivada")
                
                elif "/cazar"==mensaje.text.lower():
                    cazador = not cazador
                    caza = cazador
                    app.send_message(ids["helper"], "Activadas las funciones de cazador" if cazador else "Desactivadas las funciones de cazador")

               # elif "/restart"==mensaje.text.lower():
                  #  app.send_message(ids["helper"], "Reiniciando el Shikamarus's bot")
                  #  app.restart()




                elif "Class info: /class" in mensaje.text:
                    if (re.search(".+?🏹.+?Class info: /class", mensaje.text)) or (re.search("🏹.+?Class info: /class", mensaje.text)) or (re.search("🏹+Class info: /class", mensaje.text)):
                        ranger = True
                    else:
                        ranger = False

                    if (re.search(".+?⚔.+?Class info: /class", mensaje.text)) or (re.search("⚔.+?Class info: /class", mensaje.text)) or (re.search("⚔+Class info: /class", mensaje.text)):
                        knight = True  
                    else:
                        knight = False                

                    if (re.search(".+?🛡.+?Class info: /class", mensaje.text)) or (re.search("🛡.+?Class info: /class", mensaje.text)) or (re.search("🛡+Class info: /class", mensaje.text)):
                        sentinela = True
                    else:
                        sentinela = False
                    
                    if (re.search(".+?⚗️.+?Class info: /class", mensaje.text)) or (re.search("⚗️.+?Class info: /class", mensaje.text)) or (re.search("⚗️+Class info: /class", mensaje.text)):
                        alch = True
                    else:
                        alch = False
                    
                    if (re.search(".+?📦.+?Class info: /class", mensaje.text)) or (re.search("📦.+?Class info: /class", mensaje.text)) or (re.search("📦+Class info: /class", mensaje.text)):
                        collector = True
                    else:
                        collector = False
                    
                    if (re.search(".+?⚒.+?Class info: /class", mensaje.text)) or (re.search("⚒.+?Class info: /class", mensaje.text)) or (re.search("⚒+Class info: /class", mensaje.text)):
                        Blacksmith = True
                    else:
                        Blacksmith = False
                    
                    time.sleep(timer)
                    app.send_message(ids["helper"], "Clase/es registrada: "+"\n"+("-Ranger"+"\n" if ranger else "")+("-Knight"+"\n" if knight else "")+("-Sentinel"+"\n" if sentinela else "")+("-Alchemist"+"\n" if alch else "")+("-Collector"+"\n" if collector else "")+("-Blacksmith"+"\n" if Blacksmith else ""))
                    
 
                                                
                




                    
                          
        """

        nonlocal FUNCTION

        """
        # Borrar aquellos que ids que no son utiles. 
        def chat_on():
            dialogs = [i.chat.id for i in app.iter_dialogs()]
            faltan = False
            for k, v in ids.items():
                if  v not in dialogs:
                    ids[k]=906100033
                    faltan = True
          
            if faltan:
                try:
                    app.send_message("@Basuramia_bot", "/start")
                    app.send_message(906100033,"mandaré aquí lo que deberia mandar a otros chats pero no pude."+
                                     "puedes moverlo a archivados, pero no lo borres por favor...")
                except:
                    log.warning("No se ha podido unir al bot de Basuramia_bot "+str(me.username))
                 
        chat_on()
        if ids["helper"] != 906100033: #No está en la basura...
               app.send_message(ids["helper"],"Bot reiniciado....!!! 😜😘. Perdí la cuenta de Shikamaru escríbanme a @GrayFang para tener sus contactos")                
               reporte()

        if ids["Waifu"] != 906100033:
               joda = randint(1, 3)
               time.sleep(joda)
               app.send_message(ids["Waifu"], "Back 🔙")
               time.sleep(joda)
               app.send_message(ids["Waifu"], "PLAY NOW! 🎟")
             #  if not waifu_notif:
                #   aux_fast_waifu = True
                 #  while aux_fast_waifu:
                   #    time.sleep(joda+5)
                   #    app.send_message(ids["Waifu"], "🎟")
              # else:
               time.sleep(joda)
               app.send_message(ids["Waifu"], "🎟")
               
               
      #  if ids["CW"] != 906100033: #No está en la basura..
         #      timer = randint(3, 7)
        #       time.sleep(timer+5)
         #      app.send_message(ids["CW"],"🏅Me")
          #     time.sleep(timer+5)
          #     app.send_message(ids["CW"],"/hero")

        @app.on_message(Filters.chat(list(ids.values())) & ~Filters.scheduled & Filters.media)
        def cliente(client, message):
            nonlocal api_session
            if message.chat.id!=906100033: #no es de Basuramia_bot
                try:
                    selector_CW(message)
                except Exception as e:
                    log.warning(str(me.username)+" ha sufrido un error:", exc_info=True)      

    def stop(self):
        app.stop()
