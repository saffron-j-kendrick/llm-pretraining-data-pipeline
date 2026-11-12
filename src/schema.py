from dataclasses import dataclass, field, asdict
from typing import Any

@dataclass
class Document:
    id : str
    text : str
    source : str
    url : str | None = None # in case source does not have a url
    metadata : dict[str, Any] = field(default_factory=dict)

def from_fineweb(row: dict):
    return asdict(Document( id = row["id"], text = row["text"], source = "fineweb", url = row.get("url"), 
                               metadata = {"language" : row.get("language"), "language_score" : row.get("language_score")}))

def from_wikipedia(row: dict):
    return asdict(Document( id = row["id"], text = row["text"], source = "wikipedia", url = row.get("url"),
                               metadata= {"title" : row.get("title")}))
    
