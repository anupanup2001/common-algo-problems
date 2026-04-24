class MedianFinder {
    PriorityQueue<Integer> min = new PriorityQueue<>();
    PriorityQueue<Integer> max = new PriorityQueue<>((x, y) -> Integer.compare(y, x));

    public MedianFinder() {
        
    }
    
    public void addNum(int num) {
        min.add(num);
        max.add(min.poll());

        // Rebalance;
        if (max.size() - min.size() > 1) {
            min.add(max.poll());
        }
    }
    
    public double findMedian() {
        if (min.isEmpty() && max.isEmpty()) {
            return 0.0;
        }

        if (max.size() - min.size() == 1) {
            return max.peek();
        } else {
            return (max.peek() + min.peek())/2.0;
        }
    }
}
