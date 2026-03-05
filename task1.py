good = (r"""
Flicker: Hummillay Bubbillay Humillay Goobillay
           /|
        /\/ |/\
        \  ^   | /\  /\
  (\/\  / ^   /\/  )/^ )
   \  \/^ /\       ^  /
    )^       ^ \     (
   (   ^   ^      ^\  )
    \___\/____/______/
    [________________]
     |              |
     |     //\\     |
     |    <<()>>    |
     |     \\//     |
      \____________/
          |    |
          |    |
          |    |
          |    |
          |    |
          |    |
          |    |
""")

bad = (r"""
Doom: Bubbillay Hummillay Humillay Toubillay
           .`:;ij;f,;,
        .`;sk568G6itz,-",
      .\a\x68888888886r/,-'
    -._sV888P^98^"^9888k,-_"
   `.-\Q889"   "    `888/,-',
   .-_J88f           188KJ-_.
   ,-;388|    o o    |888[=-
   _".>88l           j88E:._"
    _"Z3886._ ,J.__.488R=;.
     .'/288888888888888S^._"
     '"j^7Z988888885R^L`-.
       ,'./jQV9TYVR\[\`".
          '|'|! |'|`. "
          ./ l  | \
        .'_ _.\ j, `._,.
       (_)_)._) (_.__,._)
""")

torch_lit = True
if torch_lit:
    outcome = good
else:
    outcome = bad
print(outcome)