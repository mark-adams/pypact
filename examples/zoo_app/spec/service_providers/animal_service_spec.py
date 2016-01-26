from pypact import Specification, request, response, given


class AnimalServiceClientSpec(Specification):
    consumer = 'Zoo App'
    provider = 'Animal Service'

    @request(
        method='GET',
        path='/alligators/Mary',
        headers={
            'Accept': 'application/json'
        }
    )
    @given('there is an alligator named Mary')
    def when_an_alligator_by_the_given_name_exists(self):
        return response(
            status=200,
            headers={
                'Content-Type': 'application/json;charset=utf-8'
            },
            body={
                'name': 'Mary'
            }
        )

    @request(
        method='GET',
        path='/alligators/Mary',
        headers={
            'Accept': 'application/json'
        }
    )
    @given('there is not an alligator named Mary')
    def when_an_alligator_by_the_given_name_does_not_exist(self):
        return response(
            status=404
        )

    @request(
        method='GET',
        path='/alligators/Mary',
        headers={
            'Accept': 'application/json'
        }
    )
    @given('an error occurs receiving the alligator')
    def when_an_error_occurs_retrieving_the_alligator(self):
        return response(
            status=500,
            headers={
                'Content-Type': 'application/json;charset=utf-8'
            },
            body={
                'error': 'Argh!!!'
            }
        )
