import math


print ("🫧 🪻 ♡︎ ~。.:* 🫧 ~ ♡︎ 🪻。.:* 🫧 ~ ♡︎ ~ 。.: 🪻 *🫧° ~ ⟡ ♡︎ ~  。 🪻 .:*🫧♡︎ ♡︎ 🫧 。.:* ~ ♡︎  ~     🪻     ♡︎ ~  🫧 ♡︎~ 。.:* 🪻 ~° ~ ♡︎ ⟡。.:* 🫧 🪻。.: 🫧 *~° ⟡ ♡︎ ~ 。 🪻 .:*🫧° ⟡ ♡︎ ♡︎ 🪻    🫧   ·  🪻 ♡︎~ 。.:* 🫧 ~° ⟡ ♡︎~ 🪻🫧 🪻 ♡︎ ~。.:* 🫧 ~ ♡︎ 🪻。.:* 🫧 ~ ♡︎ ~ 。.: 🪻 *🫧° ~ ⟡ ♡︎ ~  。 🪻 .:*🫧♡︎ ♡︎ 🫧 。.:* ~ ♡︎  ~     🪻     ♡︎ ~  🫧 ♡︎~ 。.:* 🪻 ~° ~ ♡︎ ⟡。.:* 🫧 🪻。.: 🫧 *~° ⟡ ♡︎ ~ 。 🪻 .:*🫧° ⟡ ♡︎ ♡︎ 🪻    🫧   ·  🪻 ♡︎~ 。.:* 🫧 ~° ⟡ ♡︎~ 🪻🫧 🪻 ♡︎ ~。.:* 🫧 ~ ♡︎ 🪻。.:* 🫧 ~ ♡︎ ~ 。.: 🪻 *🫧° ~ ⟡ ♡︎ ~  。 🪻 .:*🫧♡︎ ♡︎ 🫧 。.:* ~ ♡︎  ~     🪻     ♡︎ ~  🫧 ♡︎~ 。.:* 🪻 ~° ~ ♡︎ ⟡。.:* 🫧 🪻。.:H E L L O ! 🫧 *~° ⟡ ♡︎ ~ 。 🪻 .:*🫧° ⟡ ♡︎ ♡︎ 🪻    🫧   ·  🪻 ♡︎~ 。.:* 🫧 ~° ⟡ ♡︎~ 🪻🫧 🪻 ♡︎ ~。.:* 🫧 ~ ♡︎ 🪻。.:* 🫧 ~ ♡︎ ~ 。.: 🪻 *🫧° ~ ⟡  W E L C O M E ♡︎ ~  。 🪻 .:*🫧♡︎ ♡︎ 🫧 。.:* ~ ♡︎  ~     🪻     ♡︎ ~  🫧 ♡︎~ 。.:* 🪻 ~° ~ ♡︎ ⟡。.:* 🫧 🪻。.: 🫧 *~° U S E R !⟡ ♡︎ ~ 。 🪻 .:*🫧° ⟡ ♡︎ ♡︎ 🪻    🫧   ·  🪻 ♡︎~ 。.:* 🫧 ~° ⟡ ♡︎~ 🪻🫧 🪻 ♡︎ ~。.:* 🫧 ~ ♡︎ 🪻。.:* 🫧 ~ ♡︎ ~ 。.: 🪻 *🫧° ~ ⟡ ♡︎ ~  。 🪻 .:*🫧♡︎ ♡︎ 🫧 。.:* ~ ♡︎  ~     🪻     ♡︎ ~  🫧 ♡︎~ 。.:* 🪻 ~° ~ ♡︎ ⟡。.:* 🫧 🪻。.: 🫧 *~° ⟡ ♡︎ ~ 。 🪻 .:*🫧° ⟡ ♡︎ ♡︎ 🪻    🫧   ·  🪻 ♡︎~ 。.:* 🫧 ~° ⟡ ♡︎~ 🪻"
)
       
 
def is_prime(n):
  
  for i in range(2,n):
    if (n%i) == 0:
      return ("Not prime")
  return ("prime number")

number = int (input ("Enter a number: ")) 

print(is_prime(number)) 