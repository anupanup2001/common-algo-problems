import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks) # task => freq

        heap = [-c for c in count.values()]
        heapq.heapify(heap)

        queue = deque() # We store count + cooldown time
        time = 0
        while heap or queue:
            time += 1
            
            if heap:
                cnt = heapq.heappop(heap)
                cnt += 1
                if cnt != 0:
                    queue.append((cnt, time + n))
            
            if queue and queue[0][1] == time:
                c, t = queue.popleft()
                heapq.heappush(heap, c)
            print(f"time: {time}, heap={heap}, queue={queue}")
        return time