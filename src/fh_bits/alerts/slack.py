import httpx2


def send_webhook(webhook_url: str, username: str, message: str):
    assert webhook_url and message
    httpx2.post(webhook_url, json={
        "text": message,
        "username": username or "fh-bits",
        "icon_emoji": ":robot_face:"
    })
