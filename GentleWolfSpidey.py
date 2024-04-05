# https://www.reddit.com/r/Python/comments/5h2r6f/a_little_silliness_for_python_windows_users_the/
import winsound, random
from time import sleep

notes = {'C':0, 'D':2, 'E':4, 'F':5, 'G':7, 'Ab':8, 'A':9, 'Bb':10, 'B':11, 'C2':12, 'D2':14}

# 200 BPM, so a quarter is 300ms.
# https://www.musicnotes.com/sheetmusic/mtd.asp?ppn=MN0244135&ca=0&cmpid=art_betacustic
# https://www.youtube.com/watch?v=EyN6u4cG4tg
spideySong = "D:300 F:150 A:450 SILENCE:300 Ab:300 F:150 D:450 SILENCE:300 D:300 F:150 A:150 SILENCE:150 Bb:150 A:300 \
Ab:300 F:150 D:450 SILENCE:300 G:300 Bb:150 D2:450 SILENCE:300 C2:300 Bb:150 G:450 SILENCE:300 D:300 F:150 A:450 SILENCE:300 \
Ab:300 F:150 D:450 Bb:300 A:1200 Ab:150 G:300 F:150 G:300 F:300 D:600 D:600 D:600 D:600"

# https://attractmorematches.com/spider-man-pick-up-lines/
spideyPickups = ["If we were in the Spider-Verse, I’d pick your universe every time.", "Do you have spidey-sense? Because every time I’m near, you make my heart tingle.",\
                 "Are you Spider-Man? Because you’ve just swept me off my feet.", "I’m no Doctor Octopus, but I’ve got arms wide open for you.",\
                 "You must be made of spider silk because you’re stronger than you look.", "I’d let my identity be revealed if it meant winning your heart.",\
                 "Is your name Peter Parker? Because you’ve got me caught in your web.", "Are you from the Spider-Verse? Because every time I see you, my world flips upside down.",\
                 "I must be a Green Goblin, because I’m green with envy for anyone who gets your attention.", "Do you shoot webs? Because I’m totally entangled in your charm.",\
                 "If I were Spider-Man, would you be my Mary Jane?", "Do you have the Daily Bugle? Because you’ve got my front page headline.",\
                 "Are you a member of the Sinister Six? Because you’re dangerously attractive.", "I’m not Spider-Man, but I can still do some amazing things with my hands.",\
                 "Are you Electro? Because you’ve just electrified my heart.", "I may not be Spider-Man, but I can still make your heart soar through the skies of New York.",\
                 "Are you the Green Goblin? Because you’ve thrown a bomb into my love life.", "Do you have a symbiote? Because I feel a powerful bond between us.",\
                 "Are you a super-villain? Because you’ve just captured my heart.", "If I were Spider-Man, I’d save the last dance for you.",\
                 "Are you the Lizard? Because you’ve just regenerated my interest in love.", "I must be Sandman, because I can’t solidify my dreams without you.",\
                 "Do you have spider-powers? Because every time you’re near, I feel like I’m on top of the world.", "I may not climb walls, but I’d climb mountains for you.",\
                 "Do you have Black Cat’s luck? Because I feel fortunate to have met you.", "I may not be Spider-Man, but I can still take you to dizzying heights.",\
                 "Are you Venom? Because you’ve bonded with my heart.", "Is your name Gwen Stacy? Because you’ve got me falling for you.",\
                 "If I had Spider-Man’s powers, I’d spend all my time rescuing you.", "I’m no Vulture, but I’m swooping in to win your heart.",\
                 "If love were a web, I’d be caught in yours.", "You must be Aunt May, because you’ve got that caring heart I’ve been looking for.",\
                 "Is your heart a Spider-Tracer? Because it’s leading me right to you.", "I’m no Mysterio, but our future together looks magical.",\
                 "I’m not Spider-Man, but I’d swing by and pick you up anyway.", "Do you have super strength? Because you just lifted my spirits.",\
                 "Are you a spider bite? Because you’ve given me extraordinary feelings.", "If we were in the Spider-Verse, I’d cross dimensions just to find you.",\
                 "Are you Spider-Gwen? Because you’ve just swung into my heart.", "If you were a Spider-Man villain, you’d be the Charming Man, because you’ve bewitched my heart.",\
                 "Do you have Spidey senses? Because you’ve detected your way straight to my heart.", "Are we in the Spider-Verse? Because I feel like I’ve just met my perfect match in another dimension.",\
                 "I may not be Spider-Man, but I promise to always be your friendly neighborhood admirer.", "You’re like the Mary Jane to my Peter Parker.",\
                 "If being into you was a superpower, I’d be the strongest hero in the world.", "I’m not the Rhino, but I’d charge through any obstacle to get to your heart.",\
                 "Do you work for Oscorp? Because you’ve invented a new way to captivate my heart.", "Are you a spider bite? Because you give me powers I never knew I had.",\
                 "Is your name Miles Morales? Because you’ve just brought a new universe into my life.", "I may not climb walls, but I’m falling over myself for you.",\
                 "Are you wearing a Spider-Man suit? Because you fit perfectly in my universe.", "You must be the Kingpin, because you’ve taken over my thoughts and heart.",\
                 "You’re like Spider-Man’s web shooters – always by my side and ready to save the day.", "Are you related to Spider-Man? Because you just made my spidey-senses tingle.",\
                 "If I were a web-slinger, you’d be the reason I come home every night.", "You must be a superhero, because being with you feels like flying over New York City.",\
                 "Just like Peter Parker hides his identity, I’ve been hiding my feelings for you.", "You’re like a Spider-Man action figure – perfectly sculpted and highly desired.",\
                 "I may not have a spider suit, but I have a heart ready to save you every day.", "I’m not the Hobgoblin, but I’m throwing all my love your way.",\
                 "Do you have spider agility? Because you’ve jumped into my heart with ease.", "Are you the J. Jonah Jameson to my photos? Because you critique my heart in the best way.",\
                 "You must be a web cartridge, because you’re essential to my Spider-Man life.", "Is your kiss like Spider-Man’s? Because I’m ready to hang upside down for it.",\
                 "You’re like the Venom to my Spider-Man – impossible to separate.", "Are you a spider? Because you’ve woven a web around my heart.",\
                 "I’d climb the tallest skyscraper just to save a moment with you.", "I’m no Flash Thompson, but I’d fight for your attention.",\
                 "If I were a Spider-Man villain, I’d be ‘The Charmer’ because I can’t resist your allure.", "You must be made of spider silk because your touch is stronger than steel.",\
                 "You’re like Peter Parker’s camera – always capturing the best in me."]

# https://www.asciiart.eu/comics/spiderman
print(r"If Spiderman was bitten by a spider to become Spiderman, can you bite me so I can be your man?")
print(r'''

                                                            ....                                                             ...           
                                                      .."":"    ":".                                                  .""""": : :              
                                                    ."    :      :  :                                             ..."4  :  : : :          
                                                  ..      .:....":"" :                                           :---.$  :  : : ".         
                                                 :  : ..." :     :    :                                          :--..$..:$$$": : :        
                                                :   .".     :    :     :                                         :---.:  :  : : : "        
                                               :  ."  ".   .:.""":""..":                                         ".--.:  :  : : :".        
                                               :.".     :."  :   :   : d:                                        : --.$..:.."": :  :       
                                               :   ". ." :   :...:  ."d$:                                         "&$$$  :  : : : ."       
                                               :  ." ".  .:"" :  :"":d$$":                                         :: :  :  : : ::         
                                                :p,.   ":" ". :  : d$$P  ;                                        : : :..:.$$.: :".        
                                                :$$$$p."".  ":-:":d$$P   :                                    .....": :  :  :  ": :        
                                                :$$"$$$$$p:--:-:-:$$P   :                                   d$$$$"  : "..:  : : :"         
                                                "$:   "c$$$$p:.:.$$:   d:   ...              ...d&&&&$$D. d$$$$$ :."".:  """$"  :          
                                                 :$p     c$$$: : $$$D d$:""":  """..     .d&&&&&&&&$$$$$$$&$$$" ." :."$. "..": :           
               ..                                 :$p     :$$:.-:d$$$$$$:   :   :  :"".d&&&&&&&&&&&&&$$$$$&&$$." : :  $$D :  ::            
            . : :":"..                            ".$$..$$$$P: ..:""$$$$... :   :  :  d&&$&&&&&&&&&$$$$$$$$$$$ : ." ".. $$$$:"             
          .".": : : : :                            :$$$$$$P"":"  : ... :   ------...:&&$$$&&$$$&&$$$$$$$$$$$$$ :" ". :".:$ :               
          :.'-.:: : :."                            .:$$$$P.  :."":"   ":.  :    :  d$$$$$$$$$$$$$$$$$$$$$$$$$$"".  ."".d$".:               
        .".'-..""".:"                           .." :"". : "":    :."".. --..   : d$$$$$$$$$$$$$$$$$$$$$$$$$$$.  ":   d$".."               
        :.'-.."-.  :..                       .:".: .".. :.   :  ...:  " -.   --..d$$$$$$$$$$$$$$$$$$$$$$$$&$$$$$.: """$".."                
      .".'-..".  -.". "..                  ." :. ."."- $: "":.""   :."    "..   d$$$$$$$$$$$$$$$$$&&$$$$$&&$$$$$$$..  $ ."                 
     ."._-..".'-..".'-." ":              .":."..."-:-."$$$. :      ::        ".d$$$$$&&$$$$$$$$$&&&$$$$$&&$$$$$$$$$$"  ."                  
     :.  -.  '-..".'-.:".:             .": : .":"-:" :  $$$$$......" ". .    .$$$$$$$&&&&$$$$$&&&$$$$$$$&$$$$$$$$$$$.""                    
     ".:..'-.  .".'-..". ".          .:  ." :-."  $-.:  $$$$$$$$$$$".  : ".."d$$$$$$$$$$&&&$$$$$$$$$$$$$p"'  """""                         
         :".'-.'-.-..". :$$        ." :.":."."$$$$  :"-.:  $$$$$$$$ :  :  ...$$&&$$$$"  ""c$$$$$$$$$$p"                                              
         ". :.'-.'-.'-."$$P      .": .:  :-:"   :-. :  :--..:$$$  :  :  :- d$$$$$$P"                                                       
           " :$. $.'-. $$$  ..d$$$D."  :".:$$$ :"  -"-.:    :   :.:  :.-: .$$$$$$"                                                         
             :"$$$$". $$$: $$$$$$$$-.-:  :$$$ :"--.:  $$$$$$$$  :  :.-:  :d$$$$"                                                           
            .":$$$$$$$$$$$$$$$$$$$$$D:-.-:   ."   :   :    :  $ :-.":    :$$$$"                                                            
           .":  :c$$$$$p c$$$$$$&&&$$D  :--.:"  $$$.-."   :     :   :-:--:$$$P                                                             
          ..-:.:   :  :   &&&&&&&&$$$$-."   : $$$    :--..:..---:.--: :  $$$$                                                              
         :  :._:--.:-.:.-c&&&&&&&$$$$$D:-..:$$  :   ."  : .  :  $$  ."..-$$$P                                                              
        :.--:  :.  :  :  $$$$$$$$$$$$$&.   $$.-:"   :--.:$   :--$$--$:  $$$$                                                               
        :   :..: --:.-:.-$$$$$$$$$$$$$&&&.$   :.   :"  : ". :  $$$"$ :--$$$$                                                               
         :--   :-.:...:.c$$$$$$$$$$$$$$&&&.   : -..:   :$  """$$$$$$$ .d$$$$                                                               
          ::---:--: .c$$$$$$$$$$$$$$$$$$$&&. :"   :--.:  """$ $$$ : .d$$&$$"                                                               
          ":--.:.- $$$$$$$&&$$$$$$$$$$$$$&&&.:.--.:   :--: $$$$$$$" $$$&$$"                                                                
            : :  : $$$$&&&&$$".$$$$$$$$$$$&&&:   :..--. / $: $$$ :$_$$$&$"                                                                 
            :-_.--.$$&&&$$$$" $$$$$$$$$$$$&&&:   :     : $ :  $ :- d$$&&p                                                                  
            :._: : $$&$$""    $$$$$$$$$&$$$&&:--.:.--. :   : : :__.$&&$$'                                                                  
            ".:---.$$$"       $$$$$$$$$&&&$$&&$  :    -:.-._:--: .d&$$p                                                                    
              ":.:.:"         $$$$$$$$$$$&&&&&&  :     :    :  : d&$p                                                                      
                              $$$$$$$$&&$$$&&&&  :.--..:   :  :-_&$"                                                                       
                              &&$$$$$$$&&$$&&&& :      :--.: :   :                                                                         
                              c&$$$&$$$$&&$$&&&.:.---. :   :-:--:                                                                          
                              "&&$$&&$$$&&&&&&&&:     :--.: :   :                                                                          
                               &&$$$&&$&&&&&&&&&:.---.:  :..:.."                                                                           
                               c&&$$&&$$$&&&&&&&$    :---: : .:                                                                            
                                "c$$$$$$$$$$$$$$$..--:...:-:- :                                                                            
                                 "$$$$$$$$$$$$$&&    :  :  : : :                                                                           
                                  :. :""$$$$$$&&&.--.:.-:-.:.:...                                                                          
                                  : -:-.:   :   :   :   :  :-::&&                                                                          
                                  :  :   :-.:.-.:.-.:.-.:.-: .&&&.                                                                         
                                   :.:.. :  :   :   :   :  :$$$&&&                                                                         
                                  d$$$$$$$$$$...;.  :   :.$$$$$$&&,                                                                        
                                 .$$$$$$$$$$&&&&&&&&&&&&&&&$$$$$$$$.                                                                       
                                 d$$$$$$$$$$$$&&&&&&&&&&&$$$$$$$$$$$Dp,.                                                                   
                                 $$&$$$&$$$$$&&&&&&&&&$$$$$$$$$&$$$$$$$$D,.                                                                
                                 $$&&$$&&$$$$$&&&&&&&$$$$$$$$$$&&&&&&&$$$$$$.                                                              
                                 $&&$$&&&&$$$$$$&&&&$$$$&&$$$$$&&&&&&&&&$$$$&&.                                                            
                                 &&&$&&&&&&&$$$$&&&&&&&&&&$$$$$&&&&&&&&&&&&$&&&&.                                                          
                                .$$$$&&&&&&&&&$$&&&&&&&&&$$$$&&&&&&&&&&&&&&&&&&&&&.                                                        
                                d$$$$&&&&&&&&&&$$$$$&&$&&$$$$$$&&&&&&&&&&&&&&&&&&&&&.                                                      
                               .$$$$$&&&&&&&&&&$$$$$$$$&&$$$$$$$$$$$$$$$&&&&&&&&$$&&&&.                                                    
                               d$&&$&&&&&&&&&&&$$$$$$$$$&&&&&&&&&&&&&&&&&&&&&&&&&&$$&&$$.                                                  
                              d$$&&$&&&&&&&&&&$$$$$$$$$&&&&$$$&&&&$$$$$$&&&&&&&&&&&&&&&$$.                                                 
                              $$$&&$&&&&&&&&&&$$$$$$$$$&$$$$$$$$$$$$$$$$$$$&&&&&$$&&&&&&$$.                                                
                             .$$$&&$$&&&&&&&&&$$$$&$$$&&$$$$&&$$$$$&&&&&&&&&&&&&$$$$$$$&&$$.                                               
                             d$$$&&$$&&&&&&&&$$$$$&&$y"' '"cC$$$$$$$$$&&$$$$$&&&&&&&$$$$&&&&.                                              
                            .$$$$&&$$&&&&&&&&$$$$&&&D        "c$$$$$$$$$&&&&$$$$&&&&&&&&&&&&&&.                                            
                            d$$$$&&$&&&&&&&&&$$$$&&&`          '"c$$$$$$$$$&&$$$$$&&&&&&$$&&$$$$.                                          
                            $$$$$$&$&&&&&&&&&&$$&&&"              '"c&&&&&&$$$$$$$$&&&$$$$$&&&&$$$.                                        
                            $$&&$$$&&&&&&&&$&&$&&&"                  '"c&&&&&&$$$$&&$$$$$$$&&&$$$$$                                        
                           .$$&&$$&&&&&&&&&&$&&&$D                       '"c&&&&&&$$$$$$$$$$&$$$$$$:                                       
                           d$$&&$$&&&&&&&&&&$$$&&"                            '"cC&&&&&&&&&&&&$$$$$D                                       
                           $$$&&$$$&&&&&&&&&$$&D"                                 "c&$$$$$$$$$&$$$$&.                                      
                           $$$&&$$$&&&&&&&&$$$&'                                    "c&$&&&&&&&&$$$&&&.                                    
                           $$$$$$$$&&&&&&&$$$$$                                      :$$$&&&&&&&&$$$&&&&.                                  
                           $$$$$&$$&&&&&&$$$$$"                                      '$$$$&&&&&&&&&&$$&&&.                                 
                           $$$$&&$$&&&&&$$$$$$                                        $$$$$&&&&&&&&&&$$$&&.                                
                           c$$&&&&$$&&&$$$$$$$                                        $$$$$&&&&&&&&&&&$$$&&.                               
                            $$$&&&$$&&&$$&&$$$                                        Y$$$$&&&&&&&&&&&$$$&&&                               
                            $$$&&&&$&&$$&&$$$$                                         $$$$&&&&&&&&&&&&$$$&&                               
                          .d$$&&&&$$&&&&&$$$$"                                         Y$$&&&&&&&&&&&&&$$$$$                               
                          $$$$&&&&$$&&&&&$$$"                                           "$$$$&$$$$$$$$$$$$$$D                              
                        .d$$$$$&$$$&$$$&$$$"                                             "$$$$&$$$$$$$$$$$$ :                              
                       .$$$$$$$$$$&$$$$$$$"                                                "$$$$$$$$$$$$$&" ;                              
                  ..d$$$&$$$$$$$$$$$$$$$$"                                                   "&&&&$$$$$&-:. :                              
               .d$$$$$&&&$&$$$$$$$$$$$&&"                                                       Y. : . :-:  :                              
              .$$$$&&&$$$$&$$$$$$$$&&&$"                                                         :  : .:.:.:                               
            .d$$$&&$$$$$$$&$$$$$$$&$$$"                                                          :  :- :_:_:                                
          .d$$$&&$$$$$$$$$&$$$$$&&$$$"                                                            : :.-:   :                                
         d$$$$&$$$$$$$$&&&$$$$$&&&$"'                                                             : : . :.":                                
        d$$$$&$$$$$$$&&$$$$$$$$$&$"                                                                ::"_": ::                                
       d$$$$&$$$$$$&&&$$$$$$$$$$$"                                                                 ::. ::-::_                                
       $$$$&$$$$$$&&$$$$$$$$$$$$"                                                                 .": . :.:  -.._                          
       $$$$$$$$$$&&$$$$$$$$$$&$"                                                                 ." :'_": _: .:  -..._                     
       $$$$$$$$$$&$$$$$$$$$&&&$                                                                  :  :. .:. .-  _: :   "..                  
       c$$$$$$$$&$$$$$$$$&&$$$"                                                                 ."  :   :   : . --.    . ".                
        $$$$$$$&&$$$$$$&&$$$"'                                                                  :---:.-.:.--:"     ".."    ".              
        ;  "$$$&&$$$$$&&$"'                                                                     ".  :   :    :  .---":   .." ".            
        :  .:  """$$$$"'                                                                          --"---"-:--.:"    ..:--  .. :            
         :- :.-.:.--:"                                                                                     ".  : .--   : .-.."             
         :  :.-: . :                                                                                         '".:........""                
         :.-:  :- :                                                                                                                        
         : :.-:  :                                                                                                                         
         :.:.-:.-:                                                                                                                         
        ." :  :  :                                                                                                                         
       .".-:.-:-.:                                                                                                                         
       :   :  :  :                                                                                                                         
        :.-:--:-..:                                                                                                                        
       :  :  :    :                                   
      :.-.:.-:.-."                                    
     ."  :   : :"                                     
     :.-.:.-:.-:                                                                                                                           
   .'   :   :   :                                 
 .'..--::.-.:.-.:                                 
:  :   :   :    :                                 
: :    :   :    :                                                                                                                          
 ::.-.:.--.:.-.:                                                                                                                           
 `:   :   :  .'                                                                                                                            
  :.-:.--.:.'                                                                                                                              
   `.:   .'                                                                                                                                
     "--"    [WILU]
''')

def play_note(note, duration=500):
    winsound.Beep(int(256*(2**(notes[note]/12))), duration)

while True:
    print(random.choice(spideyPickups))
    for note in spideySong.split():
        note, duration = note.split(':')
        if note == "SILENCE":
            sleep(int(duration)/1000)
            continue
        play_note(note, int(duration))
