from lagom import Container

# configure django this line has to be before importing Repositories
from app.infrastructure.db import configure  # noqa

# configure Dependency injection
container = Container()
