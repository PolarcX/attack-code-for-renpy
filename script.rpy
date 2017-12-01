define s = Character('stickman' , Colour = "#fff000")

label block:
    s"you blocked the mosnters attack"
    jump battle1
label lose:
    "you lose"
    
label start:
    play music "BGM1.mp3"
    $ monster_hp = 200
    $ s_hp = 100
    $ s_mp = 300

label battle1:
    s "Monsters HP = [monster_hp]"
    s "stickman HP = [s_hp]"
    s "stickman MP = [s_mp]"
    menu:
        "Attack":
            $ atk = renpy.random.randint(1,100)
            if atk < 85:
                play sound "slash.mp3"
                s " you attack the monster"
                $ monster_hp -= 10
            else:
                play sound "crit.mp3"
                s " You Critted"
                $ monster_hp -= 25
         
        "Cast Fireball":
            if s_mp > 0:
                play sound "flame.mp3"
                s "cast fireball!"
                $ monster_hp -= 30
                $ s_mp -= 10
            if s_mp <= 0:
                s "You do not have mana left"
                jump continue
            
        "Heal":
            if s_mp > 0:
                play sound "heal.mp3"
                s "Heal!"
                $ s_hp += 30
            if s_mp <= 0:
                s " You do not have mana left"
                jump continue
            
        "Block":
            play sound "block.mp3"
            jump block
            
            
    if monster_hp > 0:
        jump continue
    else:
        jump win
                
    
label continue:
    
    play sound "monsterattack1.mp3"
    "The mosnter attacks you"
    $ s_hp -= 10
    
    if s_hp > 0 :
        jump battle1
    else:
        jump lose
        
label win:
    stop music
    play sound "victory.wav"
    "you win"
    stop sound
    
    
    
    
  
        
        
        