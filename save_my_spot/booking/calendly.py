import calendly

client = calendly.Client(api_key='VOTRE_CLÉ_API')

def get_calendar_url(event_type):
    event_type = client.event_type.retrieve(slug=event_type)
    return event_type['scheduling_url']
