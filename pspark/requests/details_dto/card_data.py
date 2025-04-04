from typing import Optional, Union
from dataclasses import dataclass
from ..abstract_request import AbstractRequest


@dataclass
class CardData(AbstractRequest):
    number: Optional[Union[int, str]] = None
    exp_month: Optional[str] = None
    exp_year: Optional[str] = None
    cvv: Optional[int] = None
