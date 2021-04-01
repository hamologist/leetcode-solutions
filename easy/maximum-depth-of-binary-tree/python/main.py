from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        def dig(level: int, node: Optional[TreeNode]):
            if node is None:
                return level

            return max(dig(level+1, node.left), dig(level+1, node.right))

        return dig(0, root)


if __name__ == '__main__':
    solution = Solution()

    _input = TreeNode(
        3,
        left=TreeNode(9),
        right=TreeNode(
            20,
            left=TreeNode(15),
            right=TreeNode(7)
        )
    )
    print(solution.maxDepth(_input))
