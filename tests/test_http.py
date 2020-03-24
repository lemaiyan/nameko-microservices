import json
import uuid
class TestHttp:

    @staticmethod
    def test_ship(web_session):
        result = web_session.post('/ship', data=json.dumps(dict(ship="USSR Discovery"))).text
        ship_id = json.loads(result)['ship_id']
        result = web_session.get(f'/ship/{ship_id}')
        assert result.text == '{"ship": "USSR Discovery"}'

    @staticmethod
    def test_crew(web_session):
        ship_id = str(uuid.uuid4().hex)
        payload = dict(ship_id=ship_id,
                       name="Christopher Pike",
                       designation="Captain",
                       race="Human")

        result = web_session.post('/crew', data=json.dumps(payload)).text
        crew_id = json.loads(result)['crew_id']
        result = web_session.get(f'/crew/{crew_id}')
        assert result.text == json.dumps(dict(crew=payload))


