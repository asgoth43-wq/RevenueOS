from dataclasses import dataclass
from urllib.parse import urlencode, urlparse, parse_qsl, urlunparse

@dataclass(frozen=True)
class MarketplaceListing:
    marketplace: str
    title: str
    description: str
    price: str
    tags: list[str]
    destination_url: str

def build_listing(draft, marketplace: str, destination_url: str) -> MarketplaceListing:
    marketplace = marketplace.strip().lower()
    if not marketplace:
        raise ValueError("marketplace is required")
    if not destination_url.startswith(("https://", "http://")):
        raise ValueError("destination_url must be an http(s) URL")
    title = draft.title
    description = draft.description
    if marketplace == "etsy":
        title = title[:140]
    elif marketplace == "gumroad":
        title = title[:100]
    return MarketplaceListing(
        marketplace=marketplace,
        title=title,
        description=description,
        price=str(draft.suggested_price),
        tags=draft.tags[:13],
        destination_url=destination_url,
    )

def add_tracking(url: str, source: str, campaign: str) -> str:
    parsed = urlparse(url)
    query = dict(parse_qsl(parsed.query))
    query.update({"utm_source": source, "utm_medium": "marketplace", "utm_campaign": campaign})
    return urlunparse(parsed._replace(query=urlencode(query)))
