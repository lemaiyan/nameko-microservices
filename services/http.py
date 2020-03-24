import json

from nameko.rpc import RpcProxy
from nameko.web.handlers import http
from nameko_structlog import StructlogDependency


class StarTrekHTTPService:
    log = StructlogDependency()
    name = 'star_trek_service'
    ship_rpc = RpcProxy('ship_service')
    crew_rpc = RpcProxy('crew_service')

    @http('GET', '/ship/<string:ship_id>')
    def get_ship(self, request, ship_id):
        ship = self.ship_rpc.get(ship_id)
        return json.dumps(dict(ship=ship))


    @http('POST', '/ship')
    def create_ship(self, request):
        data = json.loads(request.get_data(as_text=True))
        ship_id = self.ship_rpc.add(data['ship'])
        return json.dumps(dict(ship_id=ship_id))

    @http('GET', '/crew/<string:crew_id>')
    def get_crew(self, request, crew_id):
        crew = self.crew_rpc.get(crew_id)
        return json.dumps(dict(crew=crew))

    @http('POST', '/crew')
    def add_crew(self, request):
        data = json.loads(request.get_data(as_text=True))
        self.log.info("payload", data=data)
        crew_id = self.crew_rpc.add(data['ship_id'], data['name'],
                                    data['designation'], data['race'])
        return json.dumps(dict(crew_id=crew_id))


