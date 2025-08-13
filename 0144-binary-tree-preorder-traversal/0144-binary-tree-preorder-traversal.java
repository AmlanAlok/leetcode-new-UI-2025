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
    public List<Integer> preorderTraversal(TreeNode root) {
        
        List<Integer> result = new ArrayList<Integer>();
        
        if( root == null)
        return result;
        
        Stack<TreeNode> nodeStack = new Stack<>();
        nodeStack.push(root);
        
        while(!nodeStack.isEmpty())
        {
            TreeNode node = nodeStack.pop();
            
            result.add(node.val);
            
            if(node.right!= null)
            nodeStack.push(node.right);
            
            if(node.left!= null)
            nodeStack.push(node.left);
        }
        
        return result;
    }
}