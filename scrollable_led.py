import json

class ScrollableLED(object):

  __letter_width = 3 #each letter is 3 wide
  with open("character_map.json") as json_file:
    __letters = json.load(json_file) #load character map from external file

  def __init__(self, sentence):
    self.end_pos = 0
    self.buffer = {0:"", 1:"", 2:"", 3:"", 4:""}
    self.letter_map = {0:"", 1:"", 2:"", 3:"", 4:""}
    for letter in sentence.lower():
      lines = self.__letters[letter].split("\n") #Break letter in to vertical lines
      self.letter_map[0] += lines[0].ljust(self.__letter_width)
      self.letter_map[1] += lines[1].ljust(self.__letter_width)
      self.letter_map[2] += lines[2].ljust(self.__letter_width)
      self.letter_map[3] += lines[3].ljust(self.__letter_width)
      self.letter_map[4] += lines[4].ljust(self.__letter_width)
      self.letter_map[0] += " "
      self.letter_map[1] += " "
      self.letter_map[2] += " "
      self.letter_map[3] += " "
      self.letter_map[4] += " "
      self.end_pos += self.__letter_width + 1 #1 = space beteen letters

  def viewport_generator(self, width):
    scroll_pos = 0
    for index in range(scroll_pos, self.end_pos, 1):
      ''' Put more pixels into buffer '''
      self.buffer[0] += self.letter_map[0][scroll_pos]
      self.buffer[1] += self.letter_map[1][scroll_pos]
      self.buffer[2] += self.letter_map[2][scroll_pos]
      self.buffer[3] += self.letter_map[3][scroll_pos]
      self.buffer[4] += self.letter_map[4][scroll_pos]
      scroll_pos += 1
      yield self.get_viewport(width) #generator returns a viewport of given width

  def get_viewport(self, width):
    ''' Return a viewport of the given width into the current buffer '''
    viewport = {0:"", 1:"", 2:"", 3:"", 4:""}
    viewport[0] = self.buffer[0][-width:]
    viewport[1] = self.buffer[1][-width:]
    viewport[2] = self.buffer[2][-width:]
    viewport[3] = self.buffer[3][-width:]
    viewport[4] = self.buffer[4][-width:]
    return viewport
