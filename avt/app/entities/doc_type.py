from dataclasses import dataclass
from enum import Enum


class DocType(str, Enum):
    THEORY = "theory"
    TASK = "task"
    FAQ = "faq"
    SUPPORT = "support"