os: mac
-
moom:
  key(ctrl-shift-f13)
moom original:
  key(ctrl-shift-f13)
  sleep(100ms)
  key(enter)
  key(escape)

moom center:
  key(ctrl-shift-f13)
  sleep(100ms)
  insert('c')
  key(escape)

moom max:
  key(ctrl-shift-f13)
  sleep(100ms)
  insert('m')
  key(escape)

moom <number_small>:
  key(ctrl-shift-f13)
  sleep(100ms)
  insert(number_small)
  key(escape)
