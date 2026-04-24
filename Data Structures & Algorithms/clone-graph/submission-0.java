/*
Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    Map<Node, Node> cloneMap = new HashMap();
    public Node cloneGraph(Node node) {
        return dfsClone(node);
    }

    public Node dfsClone(Node node) {
        if (node == null) {
            return null;
        }
        if (cloneMap.containsKey(node)) {
            return cloneMap.get(node);
        }

        Node clone = new Node();
        clone.val = node.val;
        cloneMap.put(node, clone);

        // Clone neighbors
        for (Node neighbor: node.neighbors) {
            clone.neighbors.add(dfsClone(neighbor));
        }
        return clone;

    }
}