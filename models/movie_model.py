from tkinter import Tk, Listbox, StringVar
from db.database import *

class MovieModel:
  def __init__(self):
    self._database = database()
    self._listVar = StringVar(value=self._database.items)
    self._list = Listbox(listvariable = self._listVar)

  def setListBox(self, view):
    view._list['listvariable'] = self._listVar

  def delete(self, index):
    self._database.deleteItem(self._list.get(index))
    self._list.delete(index)
    return True

  def insert(self, new_movie):
    new_movie = f"{new_movie['title']} ({new_movie['year']}) - {new_movie['star']} ✰"
    self._list.insert(0,new_movie)
    self._database.insertItem(new_movie)
    return True

  @property
  def list(self):
    return '\n '.join([self._list.get(idx) for idx in range(self._list.size())])

  @property
  def data(self):
    self._database.data

# Teste Model
if __name__ == '__main__':
  root = Tk()
  m = MovieModel()
  # Inserir
  print(" -> Inserindo: ",m.insert({'title': 'titulo de teste 2', 'year': '2002', 'star':'9.7'}))
  print(" -> Inserindo: ",m.insert({'title': 'titulo que sera deletado', 'year': '2001', 'star':'8.7'}))
  # Verificando bd
  m.data
  # Verificando listagem
  print(" -> Lista: \n",m.list)
  # delete
  print(" -> Deletando: ",m.delete(0))
  # Verificando Delete
  print(" -> Lista: \n",m.list)
  # Verificando bd
  m.data