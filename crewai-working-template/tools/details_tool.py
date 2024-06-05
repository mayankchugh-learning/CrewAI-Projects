from typing import Type
from crewai_tools import BaseTool
from pydantic.v1 import BaseModel, Field
import os
import requests


class Details(BaseModel):
    title: str
    feature_desc: str
    feature_count: int


class DetailsToolInput(BaseModel):
    """Input for DetailsTool."""
    video_id: str = Field(..., description="Enter description related to subject")


class DetailsTool(BaseTool):
    name: str = "Get Details"
    description: str = "Retrieves details for a specific subject"
    args_schema: Type[BaseModel] = DetailsToolInput

    def _run(self, id: str) -> Details:
        api_key = os.getenv("API_KEY")
        url = "base_url"
        params = {
            "part": "snippet,statistics",
            "id": id,
            "key": api_key
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        item = response.json().get("items", [])[0]

        title = item["snippet"]["title"]
        feature_desc = item["snippet"]["feature_desc"]
        feature_count = int(item["statistics"].get("feature_count", 0))

        channel_id = item["snippet"]["channelId"]
        channel_url = "https://www.googleapis.com/youtube/v3/channels"
        channel_params = {
            "part": "statistics",
            "id": channel_id,
            "key": api_key
        }
        channel_response = requests.get(channel_url, params=channel_params)
        channel_response.raise_for_status()
        channel_item = channel_response.json().get("items", [])[0]
        channel_subscriber_count = int(
            channel_item["statistics"]["subscriberCount"])

        return VideoDetails(
            title=title,
            view_count=view_count,
            like_count=like_count,
            dislike_count=dislike_count,
            comment_count=comment_count,
            channel_subscriber_count=channel_subscriber_count
        )
