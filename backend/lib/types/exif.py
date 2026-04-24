from typing import Optional

from pydantic import BaseModel


class ExtractedExif(BaseModel):
    make: str
    model: str
    datetime_original: str
    iso: int
    exposure_time: float  # seconds
    fnumber: float  # f-stop
    focal_length: float  # mm
    gps_latitude: Optional[float] = None  # decimal degrees
    gps_longitude: Optional[float] = None  # decimal degrees
