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

class Solution {
    int numEntries = 0;
    int kth = -1;
    public int kthSmallest(TreeNode root, int k) {
        inOrder(root, k);
        return kth;
    }

    public void inOrder(TreeNode node, int k) {
        if (numEntries >= k) {
            return;
        }

        if (node == null) {
            return;
        }
        inOrder(node.left, k);
        if (numEntries >= k) {
            return;
        }
        kth = node.val;
        numEntries++;
        inOrder(node.right, k);

    }
}
