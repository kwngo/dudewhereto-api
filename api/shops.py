from sizzle.base import db
from logging import getLogger

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('url')
parser.add_argument('description')
parser.add_argument('thumbnail')


class Posts(Resource):
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
            post = Post(name=name, url=url, description=description, thumbnail=thumbnail)
            db.session.add(post)
            db.session.commit()
            return {'post': post}
        except SQLAlchemyError as e:
            LOG.error(f'Post: Post could not be created: {e}')


