from pydantic import BaseModel


class Weather(BaseModel):
    location: str
    temperature: float
    rain_expected: bool
