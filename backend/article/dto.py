from dataclasses import dataclass
from datetime import datetime

@dataclass
class CreateArticleDTO:
    url: str
    title: str | None
    content: str
    author: str
    published_at: datetime

