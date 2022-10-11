from bds_framework.cache.base import DEFAULT_TTL, BaseCache


class NoCache(BaseCache):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add(self, key, value, ttl=DEFAULT_TTL, version=None):
        return True

    def get(self, key, default=None, version=None):
        return default

    def set(self, key, value, ttl=DEFAULT_TTL, version=None):
        pass

    def touch(self, key, ttl=DEFAULT_TTL, version=None):
        return False

    def delete(self, key, version=None):
        return False

    def has_key(self, key, version=None):
        return False

    def clear(self):
        pass
