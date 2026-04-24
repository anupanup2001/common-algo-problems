/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        List<String> nodes = new ArrayList<>();
    
        rser(root, nodes);
        return String.join(",", nodes);

    }

    public void rser(TreeNode node, List<String> nodes) {
        if (node == null) {
            nodes.add("N");
            return;
        }

        nodes.add(String.valueOf(node.val));
        rser(node.left, nodes);
        rser(node.right, nodes);
        return;
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        String[] parts = data.split(",");
        LinkedList<String> nodes = new LinkedList<>(Arrays.asList(parts));

        return rdeser(nodes);
    }

    public TreeNode rdeser(LinkedList<String> nodes) {
        if (nodes.isEmpty()) {
            return null;
        }

        String strNode = nodes.remove();
        if (strNode.equals("N")) {
            return null;
        }

        System.out.println(strNode);
        TreeNode node = new TreeNode(Integer.valueOf(strNode));
        node.left = rdeser(nodes);
        node.right = rdeser(nodes);
        return node;
    }
}
