settings():
    # minimum silence time (in seconds) before speech is cut off, default 0.3
    speech.timeout = 0.3

again: core.repeat_command(1)
more: core.repeat_command(1)

clap: key(enter)
# north: key(up)
# south: key(down)
# west: key(left)
# east: key(right)

toggle toggle: key(alt-ctrl-shift-t)

# silly stuff
just windows please: user.window_list()

dump screens: user.screens()
