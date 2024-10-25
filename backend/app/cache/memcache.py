import time
from typing import Optional


class SimpleCache:
    def __init__(self):
        self.cache = {}
        self.ttl = 60 * 60

    def get(self, key: str) -> Optional[dict]:
        if (
            key in self.cache
            and (time.time() - self.cache[key]["timestamp"]) < self.ttl
        ):
            return self.cache[key]["data"]
        return None

    def set(self, key: str, data: dict):
        self.cache[key] = {"data": data, "timestamp": time.time()}
