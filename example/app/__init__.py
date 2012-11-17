from pyramid.config import Configurator
from pyramid.view import view_config
from rebecca.form.views import FormView, AddFormView, DisplayView, EditFormView
from rebecca.form.utils import MatchDictFinder
import formalchemy as fa
import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.ext.declarative import declarative_base
from zope.sqlalchemy import ZopeTransactionExtension

Base = declarative_base()
DBSession = orm.scoped_session(orm.sessionmaker(extension=ZopeTransactionExtension()))

class Item(Base):
    __tablename__ = 'items'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.Unicode(255), nullable=False)
    value = sa.Column(sa.Integer, nullable=False)

    def __unicode__(self):
        return u"Item id={id}, name={name}, value={value}".format(id=self.id, name=self.name, value=self.value)


class Login(object):
    name = fa.Field().set(required=True)
    password = fa.Field().password().set(required=True)


@view_config(route_name="login", renderer="login.pt")
class LoginForm(FormView):
    __x_model__ = Login

@view_config(route_name='add_item', renderer="form.pt")
class AddItemView(AddFormView):
    __x_model__ = Item
    __x_session__ = DBSession



item_finder = MatchDictFinder(Item, DBSession, [(Item.id, 'item_id')])

@view_config(route_name='edit_item', renderer="form.pt")
class EditItemView(EditFormView):
    __x_factory__ = item_finder

@view_config(route_name='show_item', renderer="form.pt")
class DisplayItemView(DisplayView):
    __x_factory__ = item_finder

def main(global_conf, **settings):
    from pyramid.session import UnencryptedCookieSessionFactoryConfig

    engine = sa.engine_from_config(settings)
    DBSession.remove()
    DBSession.configure(bind=engine)
    Base.metadata.create_all(bind=DBSession.bind)
    config = Configurator(settings=settings)
    config.set_session_factory(UnencryptedCookieSessionFactoryConfig("secret"))
    config.include('pyramid_tm')
    config.include('rebecca.form')
    config.add_route('login', 'login')
    config.add_route('add_item', 'items/add')
    config.add_route('show_item', 'items/{item_id}')
    config.add_route('edit_item', 'items/{item_id}/edit')
    config.scan(".")

    return config.make_wsgi_app()
