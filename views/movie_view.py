import tkinter as tk

class MovieView:
  def __init__(self, root):
    self.__root = root
    self._labels = {}
    self._inputs = {}
    self._buttons = {}
    self._frames = {}

    self._create()
    self._style()
    self._load()

  def _create(self):
    self._frames['List'] = tk.Frame(self.__root, border=0, bg="#1c2e4a")
    self._frames['Title'] = tk.Frame(self.__root, border=0, bg="#1c2e4a")
    self._frames['Year']= tk.Frame(self.__root, border=0, bg="#1c2e4a")
    self._frames['Star']= tk.Frame(self.__root, border=0, bg="#1c2e4a")
    
    self._labels['Title'] = tk.Label(self.__root, text='Titulo:', border=0, borderwidth=0, highlightthickness=0)
    self._labels['Year'] = tk.Label(self.__root, text='Ano:', border=0, borderwidth=0, highlightthickness=0)
    self._labels['Star'] = tk.Label(self.__root, text='Nota:', border=0, borderwidth=0, highlightthickness=0)

    self._inputs['Title'] = tk.Entry(self._frames['Title'], border=0, borderwidth=0, highlightthickness=0)
    self._inputs['Year'] = tk.Entry(self._frames['Year'], border=0, borderwidth=0, highlightthickness=0)
    self._inputs['Star'] = tk.Entry(self._frames['Star'], border=0, borderwidth=0, highlightthickness=0)

    self._buttons['Insert'] = tk.Button(self.__root, text='Inserir Item', border=0, borderwidth=0, highlightthickness=0, cursor="hand1")
    self._buttons['Edit'] = tk.Button(self.__root, text='Editar Item', border=0, borderwidth=0, highlightthickness=0, cursor="hand1")
    self._buttons['Delete'] = tk.Button(self.__root, text='Deletar Item', border=0, borderwidth=0, highlightthickness=0, cursor="hand1")
  
    self._list = tk.Listbox(self._frames['List'], width=50, border=0, borderwidth=0, highlightthickness=0, activestyle='none')
    
  def _load(self):
    #tk.Scrollbar(self._list)

    self._labels['Title'].grid(row=0, column=0, sticky=tk.W+tk.S, pady=(5, 0), padx=(10, 0))
    self._labels['Year'].grid(row=1, column=0, sticky=tk.W+tk.S, pady=(5, 0), padx=(10, 0))
    self._labels['Star'].grid(row=2, column=0, sticky=tk.W+tk.S, pady=(5, 0), padx=(10, 0))

    self._frames['Title'].grid(row=0, column=1, sticky=tk.E+tk.W, pady=(5, 0), padx=(0, 10))
    self._frames['Year'].grid(row=1, column=1, sticky=tk.E+tk.W, pady=(5, 0), padx=(0, 10))
    self._frames['Star'].grid(row=2, column=1, sticky=tk.E+tk.W, pady=(5, 0), padx=(0, 10))
    self._frames['List'].grid(row=3, column=0, columnspan=2, padx=(10, 10), pady=(10, 10))

    self._inputs['Title'].grid(row=0, column=0, pady=(2, 2), padx=(5, 0))
    self._inputs['Year'].grid(row=0, column=0, pady=(2, 2), padx=(5, 0))
    self._inputs['Star'].grid(row=0, column=0, pady=(2, 2), padx=(5, 0))

    self._buttons['Insert'].grid(row=4, column=0, sticky=tk.E+tk.W, padx=(10, 5))
    self._buttons['Edit'].grid(row=4, column=1, sticky=tk.E+tk.W, padx=(5, 10))
    self._buttons['Delete'].grid(row=5, column=0, sticky=tk.E+tk.W, columnspan=2, pady=(5, 5), padx=(10, 10))
    self._list.grid(row=0, column=0, columnspan=2, padx=(2, 2), pady=(2, 2))

    author = tk.Label(self.__root, text='Author: Ernane Ferreira', fg="#ccc", bg="#152238")
    author.config(font=("sans-serif", 9))
    author.grid(row=6, column=0, columnspan=2, rowspan=2,pady=(5,10))

  def _style(self):    
    bg_dark = "#152238"
    bg_clean = "#1c2e4a"
    bg_hover = "#344b72"
    white = "#fff"

    self.__root['background'] = bg_dark 

    self._list['foreground'] = white
    self._list['background'] = bg_clean
    self._list['selectforeground'] = white
    self._list['selectbackground'] = bg_hover
    
    self._labels['Year']['foreground'] = white
    self._labels['Title']['foreground'] = white
    self._labels['Title']['background'] = bg_dark 
    self._labels['Year']['background'] = bg_dark 
    self._labels['Star']['foreground'] = white
    self._labels['Star']['background'] = bg_dark 

    self._inputs['Title']['foreground'] = white
    self._inputs['Title']['background'] = bg_clean
    self._inputs['Year']['foreground'] = white
    self._inputs['Year']['background'] = bg_clean
    self._inputs['Star']['foreground'] = white
    self._inputs['Star']['background'] = bg_clean

    self._buttons['Insert']['background'] = bg_clean
    self._buttons['Edit']['background'] = bg_clean
    self._buttons['Delete']['background'] = bg_clean
    self._buttons['Insert']['foreground'], self._buttons['Insert']['activeforeground'] = [white, white]
    self._buttons['Edit']['foreground'], self._buttons['Edit']['activeforeground'] = [white, white]
    self._buttons['Delete']['foreground'],self._buttons['Delete']['activeforeground'] = [white, white]

    self._buttons['Insert']['activebackground'] = bg_hover
    self._buttons['Edit']['activebackground'] = bg_hover
    self._buttons['Delete']['activebackground'] = bg_hover

  @property
  def list(self):
    return self._list

# Testes da view
if __name__ == "__main__":
  root = tk.Tk()
  root.title('Teste View')
  c = MovieView(root)
  tk.mainloop()