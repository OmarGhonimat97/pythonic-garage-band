from abc import abstractmethod


class Band:
  instances = []

  def __init__(self, name, members=[]):
    self.name = name
    self.members = members
    self.__class__.instances.append(self)

  def __repr__(self):
    return self.name

  def __str__(self):
    return self.name

  def play_solos(self):
    output = [member.play_solo() for member in self.members]
    return output
    # for member in self.members:
    #   output = member.play_solo()
    # return output

  @classmethod
  def to_list(cls):
    return cls.instances


class Musician:

  def __init__(self):
      self.name = ''
      self.instrument = ''

  def __repr__(self):
    pass

  def __str__(self):
    pass

  def play_solo(self):
    pass

  def get_instrument(self):
    pass


class Guitarist(Musician):
  def __init__(self, name):
      self.name = name
      self.instrument = 'guitar'

  def __repr__(self):
    return f"Guitarist instance. Name = {self.name}"

  def __str__(self):
    return f"My name is {self.name} and I play {self.instrument}"



  def play_solo(self):
    return 'face melting guitar solo'

  def get_instrument(self):
    return self.instrument


class Bassist(Musician):
  def __init__(self, name):
    self.name = name
    self.instrument = "bass"


  def __str__(self):
    return f"My name is {self.name} and I play {self.instrument}"


  def __repr__(self):
    return f"Bassist instance. Name = {self.name}"


  def get_instrument(self):
    return self.instrument


  def play_solo(self):
    return "bom bom buh bom"


class Drummer(Musician):
  def __init__(self, name):
    self.name = name
    self.instrument = "drums"


  def __str__(self):
    return f"My name is {self.name} and I play {self.instrument}"


  def __repr__(self):
    return f"Drummer instance. Name = {self.name}"


  def get_instrument(self):
    return self.instrument


  def play_solo(self):
    return "rattle boom crash"


