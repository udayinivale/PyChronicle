import sys
import linecache
from types import FrameType
from typing import Optional

class PyChronicleTracer:

    def __init__(self):
        self.step_number = 0
    def next_step(self):
        self.step_number += 1
        return self.step_number