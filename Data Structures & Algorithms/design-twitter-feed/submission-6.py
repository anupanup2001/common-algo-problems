from collections import defaultdict
class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.tweets = defaultdict(set)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].add((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        q = []
        for time, tweet in self.tweets[userId]:
            heapq.heappush(q, (time, tweet))
            if len(q) == 11:
                heapq.heappop(q)
        for follower in self.followers[userId]:
            for time, tweet in self.tweets[follower]:
                heapq.heappush(q, (time, tweet))
                if len(q) == 11:
                    heapq.heappop(q)
        l = [0]* len(q)
        
        length = len(q)
        for i in range(length):
            l[length - 1 - i] = heapq.heappop(q)[1]
        return l
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        
        self.followers[followerId].discard(followeeId)