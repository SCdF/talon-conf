from talon import Context, Module, ui, actions, noise

import pprint

mod = Module()

@mod.action_class
class Actions:
  def window_list():
    """asdf"""
    truth = []
    for app in filter(lambda x : x.active_window, ui.apps(background=False)):
      truth.append(app.active_window)
    pprint.pprint(truth)
  def screens():
    """asdfasdf"""
    print(ui.screens())

def on_pop(active):
    actions.speech.enable()
noise.register("pop", on_pop)
