class database:
  def __init__(self):
    self._name_archive = f"{__file__.replace('database.py','')}db.txt"
    self._db = None
    self._items = self.loadDB()

  def loadDB(self):
    try:
      self._db = open(self._name_archive, "r+")
      list = []
      for line in self._db:
          list.append(line.strip())
      return list
    except Exception as  error:
      print("Error: ", error)
    finally:
      self._db.close()

  def deleteItem(self, item):
    with open(self._name_archive, "r") as f:
      lines = f.readlines()
    with open(self._name_archive, "w") as f:
        for line in lines:
            if line.strip("\n") != item:
                f.write(line)

  def insertItem(self, new_item):
    self._items.append(new_item)
    try:
      self._db = open(self._name_archive, "a")
      self._db.write(new_item+"\n")
    except Exception as  error:
      print("Error: ", error)
    finally:
      self._db.close()

  @property
  def items(self):
    return self._items

  @property
  def data(self):
    lines = []
    with open(self._name_archive, "r") as f:
      lines = f.readlines()
    print("\n.::Dados do 'Banco de Dados'::.\n\n", ' '.join(lines).strip())
    