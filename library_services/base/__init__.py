from library_services import lm
from library_services.models import User


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


from .index import main
from .auth import auth
from .clients import user
from .book import book
from .comment import comment
from .log import log
