from parcer.celery import app
from utils.parcer import get_link
from apps.src.models import Base


@app.task
def parsing_base(title):
    result = get_link(
        title=title)
    if result is not None:
        for value in result.itertuples():
            Base.objects.get_or_create(
                date=value[1],
                open=value[2],
                high=value[3],
                low=value[4],
                close=value[5],
                adj_close=value[6],
                volume=value[7]
            )
    return 'data parsing and write to database'
