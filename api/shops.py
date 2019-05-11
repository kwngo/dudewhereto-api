from dudewhereto.base import db
from logging import getLogger

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('url')
parser.add_argument('description')
parser.add_argument('thumbnail')


class Shops(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', type=str)
        self.parser.add_argument('url')
        self.parser.add_argument('description')
        self.parser.add_argument('thumbnail')

    def post(self):
        args = self.parser.parse_args()
        name = args['name']
        url = args['url']
        description = args['description']
        thumbnail = args['thumbnail']

        try:
            shop = Shop(name=name, url=url, description=description, thumbnail=thumbnail)
            db.session.add(shop)
            db.session.commit()
            return {'shop': shop}
        except SQLAlchemyError as e:
            LOG.error(f'Shop: Shop could not be created: {e}')


