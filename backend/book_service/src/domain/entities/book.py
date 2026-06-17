from dataclasses import dataclass
from datetime import datetime


@dataclass
class Book:
    series_id: int
    publisher_id: int
    type: list[str | None]
    title_ru: str
    title_orig: str
    isbn: str
    volume_number: str
    price: float
    stock: int | None
    pages: int
    weight_g: int
    dimensions: str
    cover_type: str
    publishing_year: int
    age_rating: str
    description: str
    created_at: datetime
