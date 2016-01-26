from .models import Alligator


class AnimalServiceClient(object):
    base_uri = 'animal-service.com'

    def find_alligator_by_name(self, name):
        response = self.client.get(
            '/alligators/{0}' % name,
            headers={
                'Accept': 'application/json'
            }
        )

        if response.ok:
            return Alligator(**response.json())
