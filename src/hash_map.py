from linked_list import LinkedList
from node import Node

class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [LinkedList() for element in range(self.array_size)]

  def hash(self, key):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code

  def compress(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compress(self.hash(key))
    list_at_array = self.array[array_index]
    #update value if key already exists
    for item in list_at_array:
      if item[0] == key:
        item[1] = value
        return
    #if the key does not exist, add a new node to the linked list:  
    payload = Node([key, value])
    list_at_array.insert(payload)

  def retrieve(self, key):
    array_index = self.compress(self.hash(key))
    payload = self.array[array_index]
    list_at_index = self.array[array_index]
    for item in list_at_index:
      if item[0] == key:
        return item[1]
    return None #if the key does not exist in the hash map