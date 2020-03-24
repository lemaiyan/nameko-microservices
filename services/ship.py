import uuid

from nameko.rpc import rpc
from nameko_redis import Redis


class ShipService:
    name = 'ship_service'

    redis = Redis('development')

    @rpc
    def ship(self, ship_id):
        return self.redis.get(ship_id)

    @rpc
    def add(self, ship):
        ship_id = uuid.uuid4().hex
        self.redis.set(ship_id, ship)
        return ship_id



