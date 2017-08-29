import requests
import os
from cars.models import BuildMedia

youtube_api_key = os.environ["YOUTUBE_API_KEY"]

def instagram_embed_retrieve(instagram_media_id):
    ig_url = "https://instagram.com/p/" + instagram_media_id
    api_response = requests.get("https://api.instagram.com/oembed?url=" + ig_url)
    json = api_response.json()

    return BuildMedia(
        media_type=BuildMedia.BuildMediaType.INSTAGRAM_PHOTO.value,
        remote_url=ig_url,
        external_id=instagram_media_id,
        preview_image_url=json["thumbnail_url"]
    )


def youtube_embed_retrieve(youtube_media_id):
    api_response = requests.get("https://www.googleapis.com/youtube/v3/videos?id=%s&key=%s&part=snippet" % (youtube_media_id, youtube_api_key))
    json = api_response.json()
    items = json["items"]
    if len(items) == 0:
        return None

    return BuildMedia(
        media_type=BuildMedia.BuildMediaType.YOUTUBE_VIDEO.value,
        remote_url="https://www.youtube.com/watch?v=" + youtube_media_id,
        external_id=youtube_media_id,
        preview_image_url=items[0]["snippet"]["thumbnails"]["medium"]["url"]
    )
