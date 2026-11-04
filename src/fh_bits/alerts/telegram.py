import httpx2


def send(bot_token: str, chat_id: str, msg: str) -> None:
    assert bot_token and chat_id
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    httpx2.post(url, params={"chat_id": chat_id, "text": msg, "parse_mode": "Markdown"})
