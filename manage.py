import os
import pytest
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import config as app_config
from api import create_app


manager = Manager(create_app(app_config))
manager.add_command('db', MigrateCommand)

@manager.command
def test():
    """Runs the tests."""
    pytest.main(["-s", "tests"])


if __name__ == '__main__':
    manager.run()
