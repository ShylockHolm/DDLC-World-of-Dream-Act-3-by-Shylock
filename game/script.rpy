label start:

    $ anticheat = persistent.anticheat

    $ chapter = 0

    $ _dismiss_pause = config.developer

    $ s_name = "Sayori"
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"
    $ me_name = "Meiji"
    $ kot_name = "Kotonoha"
    $ mo_name = "Mori"
    $ koz_name = "Kozue"
    $ ya_name = "Yae"

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ in_sayori_kill = None
    $ allow_skipping = True
    $ config.allow_skipping = True

    #call dayminus1
    call day0 from _call_day0
    jump endgame

label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
