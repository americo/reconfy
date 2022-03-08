from discord_webhook import DiscordWebhook


def discord(webhook_url, content):
    webhook = DiscordWebhook(url=webhook_url, content=content)
    response = webhook.execute()
    return response
