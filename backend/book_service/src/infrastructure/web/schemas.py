from pydantic import BaseModel, Field


class BookCreateDTO(BaseModel):
    series_id: int
    publisher_id: int
    type: list[str | None]
    title_ru: str = Field(min_length=1, max_length=255)
    title_orig: str
    isbn: str = Field(min_length=10, max_length=13)
    volume_number: str
    price: float = Field(gt=0, description="Цена должна быть больше 0")
    stock: int | None = Field(default=0, ge=0)
    pages: int = Field(gt=0)
    weight_g: int = Field(gt=0)
    dimensions: str
    cover_type: str
    publishing_year: int = Field(gt=0)
    age_rating: str
    description: str
