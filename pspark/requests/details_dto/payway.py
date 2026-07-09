from dataclasses import dataclass
from typing import Optional

from ..abstract_request import AbstractRequest


@dataclass
class Payway(AbstractRequest):
    pwid: Optional[str] = None
