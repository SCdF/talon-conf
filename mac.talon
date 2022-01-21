os: mac
mode: all
-
talon mac: speech.enable()
talon windows: speech.disable()

spotlight <phrase>:
  key(super-space)
  sleep(100ms)
  insert(phrase)

(focus|folk) switch: key(super-tab)

quick note: key(fn-q)

settings():
  user.mouse_continuous_scroll_amount = -80
