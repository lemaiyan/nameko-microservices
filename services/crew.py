import uuid

from nameko.rpc import rpc
from nameko_redis import Redis
from nameko_structlog import StructlogDependency


class CrewService:
    name = 'crew_service'
    log = StructlogDependency()
    redis = Redis('development')

    @rpc
    def get(self, crew_id):
        return self.redis.hgetall(crew_id)

    @rpc
    def add(self, ship_id, name, designation, crew_race):
        crew_id = uuid.uuid4().hex
        crew = {
            "ship_id": ship_id,
            "name": name,
            "designation": designation,
            "race": crew_race
        }
        self.log.info("crew-info", crew=crew)
        self.redis.hmset(crew_id, crew)
        return crew_id
