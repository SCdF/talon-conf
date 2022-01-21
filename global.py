from talon import Context, Module, ui, actions, noise

import pprint

mod = Module()

# pop_to_wake = True
# def on_pop(active):
#   if (pop_to_wake and not actions.speech.enabled()):
#     actions.speech.enable()
# noise.register("pop", on_pop)

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

  # def disable_pop_to_wake():
  #   """123"""
  #   global pop_to_wake
  #   print("disabling pop to wake?")
  #   pop_to_wake = False

  # def enable_pop_to_wake():
  #   """456"""
    # global pop_to_wake
    # print("enabling pop to wake?")
    # pop_to_wake = True
