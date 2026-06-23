#This is a copy of definitions.rpy from DDLC.
#Use this as a starting point if you would like to override with your own.

#Explanation for Definitions
#This section defines stuff for the game: sprite poses for the girls, music, and backgrounds
#If you plan on adding new content, pop them over down there and mimic the appropriate lines!
define persistent.demo = False
define persistent.steam = False
define config.developer = True #Change this flag to True to enable dev tools

## Android Gestures (provided by Tulkas)
## These gestures allow players to access different settings using the touch screen.
# Swipe Up - Saves
# Swipe Down - Hide Dialogue Box
# Swipe Left - History
# Swipe Right - Skip Dialogue
define config.gestures = { "n" : 'game_menu', "s" : "hide_windows", "e" : 'toggle_skip', "w" : "history" }
    
init python:
    # Creates a keymap for the history screen
    if renpy.android:
        config.underlay.append(renpy.Keymap(history = ShowMenu("history"))) 

## Music
# This section declares the music available to be played in the mod.
# Syntax:
#   audio. - This tells Ren'Py this is a audio variable.
#   t1 - This tells Ren'Py the label of the music/sound file being declared.
#   <loop 22.073> - This tells Ren'Py to loop the music/sound to this position when the song completes.
#   "bgm/1.ogg" - This tells Ren'Py the path of the music/sound file to use.
# Example: 
#   define audio.t2 = "bgm/2.ogg"
define audio.t1 = "<loop 22.073>bgm/1.ogg"  #Main theme (title)


define audio.t2 = "<loop 4.499>bgm/2.ogg"   #Sayori theme
define audio.t2g = "bgm/2g.ogg"
define audio.t2g2 = "<from 4.499 loop 4.499>bgm/2.ogg"
define audio.t2g3 = "<loop 4.492>bgm/2g2.ogg"
define audio.t3 = "<loop 4.618>bgm/3.ogg"   #Main theme (in-game)
define audio.t3g = "<to 15.255>bgm/3g.ogg"
define audio.t3g2 = "<from 15.255 loop 4.618>bgm/3.ogg"
define audio.t3g3 = "<loop 4.618>bgm/3g2.ogg"
define audio.t3m = "<loop 4.618>bgm/3.ogg"
define audio.t4 = "<loop 19.451>bgm/4.ogg"  #Poem minigame
define audio.t4g = "<loop 1.000>bgm/4g.ogg"
define audio.t5 = "<loop 4.444>bgm/5.ogg"   #Sharing poems...... 'Okay Everyone~!'
#Hey Mod team, our themes aren't defined here in the original script.
#Did some reading around and there was this + "_character" reference elsewhere.
#Anyhow, I'll try 'defining' them and see if it works!

define audio.tmonika = "<loop 4.444>bgm/5_monika.ogg" #I'm the only one with pianos x3
define audio.tsayori = "<loop 4.444>bgm/5_sayori.ogg" #Hxppy Thoughts with Ukelele & Snapping~!
define audio.tnatsuki = "<loop 4.444>bgm/5_natsuki.ogg" #Was it always cute on purpose?
define audio.tyuri = "<loop 4.444>bgm/5_yuri.ogg" #Fancy harps and instruments!

#Yeah, Monika... that should be good.
#So, take it from her and if you want to define music, make sure it exists in the appropriate folder
#Define its "audio.name" and see how it goes! (this should always be .ogg too, I think)

define audio.t5b = "<loop 4.444>bgm/5.ogg"
define audio.t5c = "<loop 4.444>bgm/5.ogg"
define audio.t6 = "<loop 10.893>bgm/6.ogg"  #Yuri/Natsuki theme
define audio.t6g = "<loop 10.893>bgm/6g.ogg"
define audio.t6r = "<to 39.817 loop 0>bgm/6r.ogg"
define audio.t6s = "<loop 43.572>bgm/6s.ogg"
define audio.t7 = "<loop 2.291>bgm/7.ogg"   #Causing trouble
define audio.t7a = "<loop 4.316 to 12.453>bgm/7.ogg"
define audio.t7g = "<loop 31.880>bgm/7g.ogg"
define audio.t8 = "<loop 9.938>bgm/8.ogg"   #Trouble resolved
define audio.t9 = "<loop 3.172>bgm/9.ogg"   #Emotional
define audio.t9g = "<loop 1.532>bgm/9g.ogg" #207% speed
define audio.t10 = "<loop 5.861>bgm/10.ogg"   #Confession
define audio.t10y = "<loop 0>bgm/10-yuri.ogg"
define audio.td = "<loop 36.782>bgm/d.ogg"


define audio.m1 = "<loop 0>bgm/m1.ogg" #Monika and her spaceroom music
define audio.mend = "<loop 6.424>bgm/monika-end.ogg" #Monika music post-deletion

define audio.ghostmenu = "<loop 0>bgm/ghostmenu.ogg"
define audio.g1 = "<loop 0>bgm/g1.ogg"
define audio.g2 = "<loop 0>bgm/g2.ogg"
define audio.hb = "<loop 0>bgm/heartbeat.ogg"

define audio.closet_open = "sfx/closet-open.ogg"
define audio.closet_close = "sfx/closet-close.ogg"
define audio.page_turn = "sfx/pageflip.ogg"
define audio.fall = "sfx/fall.ogg"
define audio.s_kill_glitch1 = "sfx/s_kill_glitch1.ogg"
define audio.fall2 = "sfx/fall2.ogg"
define audio.giggle = "sfx/giggle.ogg"
define audio.glitch1 = "sfx/glitch1.ogg"
define audio.glitch2 = "sfx/glitch2.ogg"
define audio.glitch3 = "sfx/glitch3.ogg"
define audio.gnid = "sfx/gnid.ogg"
define audio.interference = "sfx/interference.ogg"
define audio.monikapound = "sfx/monikapound.ogg"
define audio.mscare = "sfx/mscare.ogg"
define audio.run = "sfx/run.ogg"
define audio.slap = "sfx/slap.ogg"
define audio.smack = "sfx/smack.ogg"
define audio.stab = "sfx/stab.ogg"
define audio.yuri_kill = "sfx/yuri-kill.ogg"
define audio.crack = "sfx/crack.ogg"
define audio.eyes = "sfx/eyes.ogg"  

define audio.mori = "<loop 0>mod_assets/audio/anonymous.mp3"
define audio.happy = "<loop0>mod_assets/audio/happy.mp3"
define audio.sad = "<loop0>mod_assets/audio/sad.mp3"
define audio.hope = "<loop0>mod_assets/audio/I_dont_want_to_lose_hope.mp3"

## Backgrounds
# This section declares the backgrounds available to be shown in the mod.
# To define a new color background, declare a new image statement like in this example:
#     image blue = "X" where X is your color hex i.e. '#158353'
# To define a new background, declare a new image statement like this instead:
#     image bg bathroom = "mod_assets/bathroom.png" 
image black = "#000000"
image dark = "#000000e4"
image darkred = "#110000c8"
image white = "#ffffff"
image splash = "bg/splash.png"
image end:
    truecenter
    "gui/end.png"

image bg residential_day = "bg/residential.png" # Start of DDLC BG
image bg class_day = "bg/class.png" # The classroom BG
image bg corridor = "bg/corridor.png" # The hallway BG
image bg club_day = "bg/club.png" # The club BG
image bg club_day2: # Glitched Club BG
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg/club-skill.png"

image bg closet = "bg/closet.png" # The closet BG
image bg bedroom = "bg/bedroom.png" # MC's Room BG
image bg sayori_bedroom = "bg/sayori_bedroom.png" # Sayori's Room BG
image bg house = "bg/house.png" # Sayori's House BG
image bg kitchen = "bg/kitchen.png" # MC's Kitchen BG

image bg notebook = "bg/notebook.png" # Poem Game Notebook Scene
image bg notebook-glitch = "bg/notebook-glitch.png" # Glitched Poem Game BG

# This image shows a glitched screen during Act 2 poem sharing with Yuri.
image bg glitch = LiveTile("bg/glitch.jpg")

# This image transform shows a glitched scene effect
# during Act 3 when we delete Monika.
image glitch_color:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.7
        linear 0.45 alpha 0

# This image transform shows another glitched scene effect
# during Act 3 when we delete Monika.
image glitch_color2:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.7
        linear 0.45 alpha 0


#"mod_assets/bg/.png"
image bg club_ruined = "mod_assets/bg/club_ruined.png"
image bg infi_hall:
    "mod_assets/bg/god.png"
    zoom 0.7
image bg infi_hall_clear:
    "mod_assets/bg/what.png"
    zoom 0.7
image bg hallway_glitch:
    "mod_assets/bg/hallway_glitch.jpg"
    zoom 0.85
image bg class_exit = "mod_assets/bg/class_exit.png"
image bg unknown = "mod_assets/bg/unknown.png"
image bg spaceroom_dark = "mod_assets/bg/monika_room5.png"
image bg spaceroom = "mod_assets/bg/monika_room6.png"
image bg house_fog:
    "mod_assets/bg/unknown_house.jpg"
    zoom 1.3
image bg livingroom = "mod_assets/bg/MC_Living_room_rain2.png"
image bg room_destroyed = "mod_assets/bg/room_destroyed.png"
image bg book = "mod_assets/bg/PotraitofMarkov.png"
image bg aiko_room = "mod_assets/bg/Aiko-Room.png"
image bg space_bedroom = "mod_assets/bg/sc1.png"
image bg space_kitchen = "mod_assets/bg/sckitchen.png"
image bg mc_bedroom = "mod_assets/bg/bedroom6.png"


###### Character Variables ######
# These configure the shortcuts for writing dialog for each character.
define narrator = Character(ctc="ctc", ctc_position="fixed", window_background=Image("mod_assets/gui/player.png", xalign=0.5, yalign=1.0))

define s = DynamicCharacter('s_name', image='Sayori', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_background=Image("mod_assets/gui/sayori.png", xalign=0.5, yalign=1.0), who_style='say_label_sayori')
define m = DynamicCharacter('m_name', image='Monika', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_background=Image("mod_assets/gui/monika.png", xalign=0.5, yalign=1.0), who_style='say_label_monika')
define n = DynamicCharacter('n_name', image='Natsuki', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_background=Image("mod_assets/gui/natsuki.png", xalign=0.5, yalign=1.0), who_style='say_label_natsuki')
define y = DynamicCharacter('y_name', image='Yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_background=Image("mod_assets/gui/yuri.png", xalign=0.5, yalign=1.0), who_style='say_label_yuri')
define me = DynamicCharacter('me_name', image='meiji', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_background=Image("mod_assets/gui/meiji.png", xalign=0.5, yalign=1.0), who_style='say_label_mc')

define mc = DynamicCharacter('player', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_background=Image("mod_assets/gui/player.png", xalign=0.5, yalign=1.0), who_style='say_label_mc')
define mo = DynamicCharacter('mo_name', image='mori', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_background=Image("mod_assets/gui/mori.png", xalign=0.5, yalign=1.0), who_style='say_label_mori')
define kot = DynamicCharacter('kot_name', image='kotonoha', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_background=Image("mod_assets/gui/kotonoha.png", xalign=0.5, yalign=1.0), who_style='say_label_kotonoha')
define koz = DynamicCharacter('koz_name', image='kozue', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_background=Image("mod_assets/gui/kozue.png", xalign=0.5, yalign=1.0), who_style='say_label_kozue')
define ya = DynamicCharacter('ya_name', image='yae', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_background=Image("mod_assets/gui/yae.png", xalign=0.5, yalign=1.0), who_style='say_label_yae')

define pl = DynamicCharacter('pl_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_background=Image("mod_assets/gui/playji.png", xalign=0.5, yalign=1.0), who_style='say_label_mc')

define ny = Character('Nat & Yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_background=Image("mod_assets/gui/player.png", xalign=0.5, yalign=1.0), who_style='say_label_mc')
define u = Character(_('?????'), what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="nestled", who_style='say_label_mc', window_background=Image("mod_assets/gui/player.png", xalign=0.5, yalign=1.0))
define ev = Character(_('Everyone'), what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="nestled", who_style='say_label_mc', window_background=Image("mod_assets/gui/player.png", xalign=0.5, yalign=1.0))

define _dismiss_pause = config.developer

###### Persistent Variables ######
# These values are automatically loaded/saved on game start and exit.
# These exist across all saves

default persistent.playername = ""
default player = persistent.playername
default persistent.playthrough = 0
default persistent.yuri_kill = 0
default persistent.seen_eyes = None
default persistent.seen_sticker = None
default persistent.ghost_menu = None
default persistent.seen_ghost_menu = None
default seen_eyes_this_chapter = False
default persistent.anticheat = 0
default persistent.clear = [False, False, False, False, False, False, False, False, False, False]
default persistent.special_poems = None
default persistent.clearall = None
default persistent.menu_bg_m = None
default persistent.first_load = None

###### Other global variables ######
# It's good practice to define global variables here, just so you know what you can call later

default in_sayori_kill = None
default in_yuri_kill = None
default anticheat = 0
define config.mouse = None
default allow_skipping = True
default basedir = config.basedir
default chapter = 0
default currentpos = 0
default faint_effect = None

default s_name = "Sayori"
default m_name = "Monika"
default n_name = "Natsuki"
default y_name = "Yuri"
default me_name = "Meji"
default mo_name = "Mori"
default kot_name = "Kotonoha"
default koz_name = "Kozue"
default ya_name = "Yae"

default pl_name = "?pl̸%a̴y̸j̵i̸"

# Instantiating variables for poem appeal. This is how much each character likes the poem for each day.
# -1 = Dislike, 0 = Neutral, 1 = Like
default n_poemappeal = [0, 0, 0]
default s_poemappeal = [0, 0, 0]
default y_poemappeal = [0, 0, 0]
default m_poemappeal = [0, 0, 0]

# The last winner of the poem minigame.
default poemwinner = ['sayori', 'sayori', 'sayori']

# Keeping track of who read your poem when you're showing it to each of the girls.
default s_readpoem = False
default n_readpoem = False
default y_readpoem = False
default m_readpoem = False

# Used in poemresponse_start because it's easier than checking true/false on everyone's read state.
default poemsread = 0

# The main appeal points. Whoever likes your poem the most gets an appeal point for that chapter.
# Appeal points are used to keep track of which exclusive scene to show each chapter.
default n_appeal = 0
default s_appeal = 0
default y_appeal = 0
default m_appeal = 0

# We keep track of whether we watched Natsuki's and sayori's second exclusive scenes
# to decide whether to play them in chapter 3.
default n_exclusivewatched = False
default y_exclusivewatched = False

# Yuri runs away after the first exclusive scene of playthrough 2.
default y_gave = False
default y_ranaway = False

# We choose who to side with in chapter 1.
default ch1_choice = "sayori"

# If we choose to help Sayori in ch3, some of the dialogue changes.
default help_sayori = None
default help_monika = None

# We choose who to spend time with in chapter 4.
default ch4_scene = "yuri"
default ch4_name = "Yuri"
default sayori_confess = True

# We read Natsuki's confession poem in chapter 23.
default natsuki_23 = None

init python:
    renpy.music.register_channel("ambient","sfx",True,tight=True) #This creates a new sound channel called "ambient" with looping enable

define audio.rain = "<loop 0.0>/mod_assets/rain/sfx/rain.ogg" #the sound file that will be player when it's raining
define audio.rainindoors = "<loop 0.0>/mod_assets/rain/sfx/rain2.ogg" #a quieter version of the sound, if you want to use it while indoors use "play ambient rainindoors" isntead of "play ambient rain"

label rain: #use "call rain" to start the rain with a 5 seconds fade
    show rain zorder 5 with Dissolve(5.0)
    return

label instant_rain: #use "call instant_rain" to start the rain immediately
    show rain zorder 5
    return

label rain_stop: #use call rain_stop to stop the rain with a 5 seconds fade
    hide rain with Dissolve(5.0)
    return

label instant_rain_stop: #use call instant_rain_stop to stop the rain immediately
    hide rain
    return