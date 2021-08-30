import tkinter as tk
class Helper:
  def __init__(self, root):
    self._root = root

  def clearInputs(self):
    self._inputTitle.delete(0,'end')
    self._inputYear.delete(0,'end')
    self._inputStar.delete(0,'end')

  def flashNotice(self, msg):
    msg = tk.Label(self._root, text=msg)
    msg.grid(row=0, column=0, columnspan=2)

    msg['foreground'] = "white"
    msg['background'] = "#1c2e4a"

    self._root.after(1500, msg.destroy)

  def verifySelection(self):
    if (not self._list.curselection() == ()):
      return True
    else:
      self.flashNotice('⚠️ Nenhum item da lista foi selecionado.')
      return False
    
  def requiredInputs(self, inputs):
    if(inputs['Title'].get() and inputs['Year'].get() and inputs['Star'].get()):
      return True
    else:
      self.flashNotice('⚠️ Por favor, preencha todos os campos.')
      return False

  def checkYear(self, year):
    try:
      if len(year) >= 4 and int(year) >= 1500 and int(year) <= 2021:
        return True
      else:
        self.flashNotice('⚠️ Ano digitado não é válido.')
        return False 
    except Exception as error:
      self.flashNotice('⚠️ O valor do ano deve ser válido.')
      print("Erro: ", error)

  def checkStar(self, star):
    try:
      if float(star) >= 0.0 and float(star) <= 10.0:
        return True
      else:
        self.flashNotice('⚠️ A nota deve estar contida no intervalo de 0 à 10.')
        return False 
    except Exception as  error:
      self.flashNotice('⚠️ A nota deve ser um numero.')
      print("Erro: ", error)# Código de teste para o Model

  def _format(self, string):
    title = string.split('(')[0].strip()
    string = string.replace(title, "").replace('(', "")
    year = string.split(')')[0].strip()
    string = string.replace(year, "")
    star = string.split('-')[1].replace(" ✰","").strip()

    return ({'title': title, 'year': year, 'star':star})