import pytest
from services.http import StarTrekHTTPService


@pytest.fixture
def web_session(container_factory, web_config, web_session):
    web_config["AMQP_URI"] = "amqp://guest:guest@rabbitmq:5672/"
    container = container_factory(StarTrekHTTPService, web_config)
    container.start()
    return web_session
