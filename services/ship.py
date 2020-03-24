import uuid

from nameko.rpc import rpc
from nameko_redis import Redis
from nameko_structlog import StructlogDependency


class ShipService:
    name = 'ship_service'
    log = StructlogDependency()
    redis = Redis('development')

    @rpc
    def get(self, ship_id):
        self.log.info('start-get-ship')
        ship = self.redis.get(ship_id)
        self.log.info('get-ship', ship_id=ship_id, ship=ship)
        self.log.info('end-get-ship')
        return ship

    @rpc
    def add(self, ship):
        self.log.info('start-add-ship')
        ship_id = uuid.uuid4().hex
        self.log.info('add-ship', ship_id=ship_id, ship=ship)
        self.redis.set(ship_id, ship)
        self.log.info('end-add-ship')
        return ship_id



