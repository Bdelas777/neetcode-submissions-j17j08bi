class TimeMap:

    def __init__(self):
        self.names = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.names:
            self.names[key] = {}
        if timestamp not in self.names[key]:
            self.names[key][timestamp] = []
        self.names[key][timestamp].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.names:
            return ''
        seen = 0
        for time in self.names[key]:
            if time <= timestamp:
                seen = max(seen,time)
        return '' if seen == 0 else self.names[key][seen][-1]    
