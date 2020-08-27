import requests
import json


def get_credentials():
    # credential setup before make api call
    credentials = dict()
    credentials['access_token'] = 'EAADVGub5jW4BAFBWReNitoecZCnnS1eZAtWSb9XKlHrMxT4AXDq5TExoSTuXD6FlosVYZBnR1N9UJEwCiWhrF36jRcmWB6mZAaX42ZA0gCXJFVfi8a6iua5JHuHLAN7ovlz3iKJfpA1vygqYvCTaU1XOMp8DAD1hjdrXmnVibsAZDZD'
    credentials['client_id'] = '234311520980334'
    credentials['client_secret'] = '63402bf1ba4dddb7b05b77a6a2744e66'
    credentials['graph_domain'] = 'https://graph.facebook.com/'
    credentials['graph_version'] = 'v8.0'
    credentials['endpoint_base'] = credentials['graph_domain'] + credentials['graph_version'] + '/'
    credentials['debug'] = 'no'
    credentials['page_id'] = '100734765089209'
    credentials['instagram_user_id'] = '17841400654592306'  # developer's IG userid
    credentials['ig_username'] = 'antoniusricky79'  # developer's IG username
    return credentials


def make_api_call(url, endpoint_params, debug='no'):
    # hit the api endpoint
    data = requests.get(url, endpoint_params)

    # container for hit result
    response = dict()

    # main content of response
    response['url'] = url
    response['endpoint_params'] = endpoint_params
    response['json_data'] = json.loads(data.content)

    # pretty print for cli
    response['endpoint_params_pretty'] = json.dumps(endpoint_params, indent=4)
    response['json_data_pretty'] = json.dumps(response['json_data'], indent=4)

    # only for debugging
    if debug == 'yes':
        print_api_call_response(response)

    return response


def print_api_call_response(response):
    # only for debugging
    print('===== DEBUG MODE =====\n')
    print('URL: ')
    print(response['url'] + '\n')
    print('Endpoint Params: ')
    print(response['endpoint_params_pretty'] + '\n')
    print('Response: ')
    print(response['json_data_pretty'] + '\n')
    print('======================\n')
