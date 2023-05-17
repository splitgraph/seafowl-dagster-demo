import pandas as pd
import requests
from dagster import (
    Config,
    Definitions,
    MetadataValue,
    Output,
    asset,
    job,
    op
)

from seafowl.dataframe import dataframe_to_seafowl
from seafowl import SeafowlConnectionParams
from seafowl.types import QualifiedTableName


@asset
def hackernews_top_story_ids():
    """Get top stories from the HackerNews top stories endpoint.

    API Docs: https://github.com/HackerNews/API#new-top-and-best-stories.
    """
    top_story_ids = requests.get(
        "https://hacker-news.firebaseio.com/v0/topstories.json"
    ).json()
    return top_story_ids[:10]


# asset dependencies can be inferred from parameter names
@asset
def hackernews_top_stories(hackernews_top_story_ids):
    """Get items based on story ids from the HackerNews items endpoint."""
    results = []
    for item_id in hackernews_top_story_ids:
        item = requests.get(
            f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json"
        ).json()
        results.append(item)

    df = pd.DataFrame(results)

    # recorded metadata can be customized
    metadata = {
        "num_records": len(df),
        "preview": MetadataValue.md(df[["title", "by", "url"]].to_markdown()),
    }

    return Output(value=df, metadata=metadata)


class ExportToSeafowlConfig(Config):
    url: str
    secret: str
    table: str

@op
def export_to_seafowl(
    context, config: ExportToSeafowlConfig, data: pd.DataFrame
) -> None:
    context.log.info("exporting to seafowl")
    context.log.info(f"CONFIG url {config.url}")
    context.log.info(f"CONFIG secret {config.secret}")
    context.log.info(f"CONFIG table {config.table}")

    conn = SeafowlConnectionParams(
        url=config.url,
        secret=config.secret,
        database=None)
    destination = QualifiedTableName(schema="public", table=config.table)
    dataframe_to_seafowl(data, conn, destination)
    

@job
def hn_stories_to_seafowl_pipeline():
    export_to_seafowl(hackernews_top_stories.to_source_asset())


defs = Definitions(
    jobs=[hn_stories_to_seafowl_pipeline],
    assets=[hackernews_top_story_ids, hackernews_top_stories]
)
