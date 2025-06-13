#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (48.69%)
# Likes:    17111
# Dislikes: 809
# Total Accepted:    2.1M
# Total Submissions: 4.3M
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of numCourses courses you have to take, labeled from 0 to
# numCourses - 1. You are given an array prerequisites where prerequisites[i] =
# [ai, bi] indicates that you must take course bi first if you want to take
# course ai.
#
#
# For example, the pair [0, 1], indicates that to take course 0 you have to
# first take course 1.
#
#
# Return true if you can finish all courses. Otherwise, return false.
#
#
# Example 1:
#
#
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.
#
#
# Example 2:
#
#
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0, and to take course 0 you
# should also have finished course 1. So it is impossible.
#
#
#
# Constraints:
#
#
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.
#
#
#
from typing import List


# @lc code=start
class Solution:
    def canFinish(
        self, numCourses: int, prerequisites: List[List[int]]
    ) -> bool:
        # 做一個圖
        graph = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            # 兩個方向都可以，我覺得可以想一下
            graph[a].append(b)
            # graph[b].append(a)

        visit = [0] * numCourses

        def dfs(node):
            if visit[node] == 1:
                return False
            if visit[node] == 2:
                return True
            visit[node] = 1
            for n in graph[node]:
                if not dfs(n):
                    return False
            visit[node] = 2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


# @lc code=end
