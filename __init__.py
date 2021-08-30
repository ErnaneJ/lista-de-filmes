from controllers.movie_controller import *
from models.movie_model import *
from views.movie_view import *

if __name__ == "__main__":
  controller = MovieController()
  model = MovieModel()
  view = MovieView(controller.root)
  
  controller.initialize(model, view)
  controller.execute()
  print(__file__)