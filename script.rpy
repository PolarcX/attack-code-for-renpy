define s = Character('stickman' , Colour = "#fff000")

label block:
    s"you blocked the mosnters attack"
    jump battle1
    
label start:
    $ monster_hp = 200
    $ s_hp = 100
    $ s_mp = 30

label battle1:
    s "Monsters HP = [monster_hp]"
    s "stickman HP = [s_hp]"
    s "stickman MP = [s_mp]"
    menu:
        "Attack":
            $ monster_hp -= 10
            
        "Cast Fireball":
            if s_mp > 0:
                s "cast fireball!"
                $ monster_hp -= 30
                $ s_mp -= 10
            if s_mp <= 0:
                s "You do not have mana left"
                jump continue
            
        "Heal":
            if s_mp > 0:
                s "Heal!"
                $ s_hp += 30
            if s_mp <= 0:
                s " You do not have mana left"
                jump continue
            
        "Block":
            jump block
            
            if monster_hp > 0 :
                jump continue
            else:
                jump win
                
    
label continue:
    
    "The mosnter attacks you"
    $ s_hp -= 10
    
    if s_hp > 0 :
        jump battle1
    else:
        jump lose
        
label win:
    "you win"

label lose:
    "you lose"
    
    
    
  
        
        
        