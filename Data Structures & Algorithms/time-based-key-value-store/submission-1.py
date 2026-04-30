import bisect
class TimeMap:

    def __init__(self):
        self.keymap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keymap:
            self.keymap[key] = []
        self.keymap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keymap:
            return ""
        history = self.keymap[key]
        # left = 0
        # right = len(history) - 1
        # result = ""
        # while (left <= right):
        #     mid = left + int((right - left)/2)
        #     if history[mid][0] <= timestamp:
        #         result = history[mid][1]
        #         left = mid + 1
        #     else:
        #         right = mid - 1

        # return result
        idx = bisect.bisect_right(history, (timestamp + 1, ''))
        if idx == 0:
            return ''
        return history[idx - 1][1]
            
            
