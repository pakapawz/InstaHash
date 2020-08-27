from api_setup import get_credentials, make_api_call
from validations import has_caption, has_data


def get_hashtag_info(params):
    endpoint_params = dict()
    endpoint_params['user_id'] = params['instagram_user_id']
    endpoint_params['q'] = params['hashtag_name']
    endpoint_params['fields'] = 'id,name'
    endpoint_params['access_token'] = params['access_token']

    url = params['endpoint_base'] + 'ig_hashtag_search'

    return make_api_call(url, endpoint_params, params['debug'])


def get_hashtag_media(params):
    endpoint_params = dict()
    endpoint_params['user_id'] = params['instagram_user_id']
    endpoint_params['fields'] = 'id,children,caption,comment_count,like_count,media_type,media_url,permalink'
    endpoint_params['access_token'] = params['access_token']

    url = params['endpoint_base'] + params['hashtag_id'] + '/' + params['type']

    return make_api_call(url, endpoint_params, params['debug'])


def get_top_post_hashtags(hashtag):
    file_captions = open('file_captions', 'w')

    params = get_credentials()
    params['hashtag_name'] = hashtag
    hashtag_info_response = get_hashtag_info(params)

    if not has_data(hashtag_info_response['json_data']):
        file_captions.write('#cannot_retrieve_hashtag')
        file_captions.close()
        return

    params['hashtag_id'] = hashtag_info_response['json_data']['data'][0]['id']
    params['type'] = 'top_media'
    hashtag_top_media_response = get_hashtag_media(params)

    for post in hashtag_top_media_response['json_data']['data']:
        # post usually has [permalink'], [caption], and [media_type]
        if has_caption(post):
            caption = post['caption'].encode('ascii', 'ignore').decode() + '\n'
            file_captions.write(caption)
    file_captions.close()
