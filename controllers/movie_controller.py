import tkinter as tk
import tkinter.messagebox as messagebox
from helpers.helper import *

class MovieController(Helper):
  def __init__(self):
    self._root = tk.Tk()
    self._root.title('Listagem de Filmes')
    
    super().__init__(self._root)
    
    self._model = None
    self._view = None
    self._temp_index = None

  def initialize(self, model, view):
    self._model = model
    self._view = view
    self._setsUp()

  def execute(self):
    self._root.mainloop()

  @property
  def root(self):
    return self._root

  def _setsUp(self):
    self._model.setListBox(self._view)
    self._view._buttons['Insert']['command'] = lambda: self._processInsertion()
    self._view._buttons['Edit']['command'] = lambda: self._processEditing()
    self._view._buttons['Delete']['command'] = lambda: self._processDeletion()
  
  def _processEditing(self):
    try:
      self._temp_index = self._view._list.curselection()[0]
      values = self._format(self._view._list.get(self._temp_index))
      self._loadValuesInInputs(values)
      self._switchToEditState()
    except Exception:
      messagebox.showerror(title="Ops, algo deu errado :/",message="Você precisa selecionar um item antes de tentar editar.") 

  def _processInsertion(self):
    if self.requiredInputs(self._view._inputs) and self.checkYear(self._view._inputs['Year'].get()) and self.checkStar(self._view._inputs['Star'].get()):
      msg = "Item inserido com sucesso!"
      
      if(self._view._buttons['Edit']['text'] == "Salvar"): 
        self._processDeletion()
        self._switchToDefaultState()
        msg = "Item salvo com sucesso!"

      self._model.insert(self._valuesOfInputs())
      self.flashNotice(msg)
      self._clearInputs()
      self._temp_index = None

  def _processDeletion(self):
    try:
      msgBox = True
      item = self._temp_index
      if self._view._list.curselection():
       item = self._view._list.curselection()[0]
      if(self._view._buttons['Edit']['text'] != "Salvar" and self._view._list.curselection()):
        msgBox = messagebox.askokcancel(title = "Confirme se deseja deletar" , message = "Você tem certeza de que deseja deletar este item?") 
      if msgBox:
        self._model.delete(item)
        self.flashNotice("Item deletado com sucesso!")
    except Exception:
      messagebox.showerror(title="Ops, algo deu errado :/",message="Você precisa selecionar um item antes de tentar deletar.") 
  
  def _loadValuesInInputs(self, values):
    self._view._inputs['Title'].insert(0,values['title']) 
    self._view._inputs['Year'].insert(0,values['year']) 
    self._view._inputs['Star'].insert(0,values['star'])
    
  def _switchToEditState(self):
    self._view._buttons['Edit']['text'] = "Salvar"
    self._view._buttons['Edit']['command'] = lambda: self._processInsertion()

    self._view._buttons['Insert']['state'] = tk.DISABLED
    self._view._buttons['Delete']['state'] = tk.DISABLED
  
  def _switchToDefaultState(self):
    self._view._buttons['Edit']['text'] = "Editar Item"
    self._view._buttons['Edit']['command'] = lambda: self._processEditing()
    self._view._buttons['Insert']['state'] = tk.NORMAL
    self._view._buttons['Delete']['state'] = tk.NORMAL

  def _clearInputs(self):
    self._view._inputs['Title'].delete(0,'end')
    self._view._inputs['Year'].delete(0,'end')
    self._view._inputs['Star'].delete(0,'end')

  def _valuesOfInputs(self):
    return ({
      'title': str(self._view._inputs['Title'].get()), 
      'year': int(str(self._view._inputs['Year'].get())), 
      'star': float(str(self._view._inputs['Star'].get()))
      })