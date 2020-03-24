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
        self.log.info('start-get-crew')
        crew = self.redis.hgetall(crew_id)
        self.log.info('get-crew', crew_id=crew_id, crew=crew)
        self.log.info('end-get-crew')
        return crew

    @rpc
    def add(self, ship_id, name, designation, crew_race):
        self.log.info('start-add-crew')
        crew_id = uuid.uuid4().hex
        crew = {
            "ship_id": ship_id,
            "name": name,
            "designation": designation,
            "race": crew_race
        }
        self.log.info("add-crew", crew=crew, crew_id=crew_id)
        self.redis.hmset(crew_id, crew)
        self.log.info('end-add-crew')
        return crew_id
