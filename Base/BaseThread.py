import threading
class BThread(threading.Thread):
  def __init__(self, func):
      threading.Thread.__init__(self)
      self.func = func
      #print(type(self.func))
  def run(self):
      self.func