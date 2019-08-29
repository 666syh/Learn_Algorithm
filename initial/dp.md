# 动态规划

&emsp;&emsp;**动态规划** (dynamic programming) 是运筹学的一个分支，是求解决策过程(decision process)最优化的数学方法。20世纪50年代初美国数学家R.E.Bellman等人在研究多阶段决策过程(multistep decision process)的优化问题时，提出了著名的最优化原理(principle of optimality)，把多阶段过程转化为一系列单阶段问题，利用各阶段之间的关系，逐个求解，创立了解决这类过程优化问题的新方法——[动态规划](https://baike.baidu.com/item/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92/529408?fr=aladdin)
<div style="text-align: right">----百度百科</div>
<br>
&emsp;&emsp;动态规划算法通常用于求解具有某种最优性质的问题。在这类问题中，可能会有许多可行解。每一个解都对应于一个值，我们希望找到具有最优值的解。动态规划算法与分治法类似，其基本思想也是将待求解问题分解成若干个子问题，先求解子问题，然后从这些子问题的解得到原问题的解。与分治法不同的是，适合于用动态规划求解的问题，经分解得到子问题往往不是互相独立的。若用分治法来解这类问题，则分解得到的子问题数目太多，有些子问题被重复计算了很多次。如果我们能够保存已解决的子问题的答案，而在需要时再找出已求得的答案，这样就可以避免大量的重复计算，节省时间。我们可以用一个表来记录所有已解的子问题的答案。不管该子问题以后是否被用到，只要它被计算过，就将其结果填入表中。这就是动态规划法的基本思路。具体的动态规划算法多种多样，但它们具有相同的填表格式。  

&emsp;&emsp;与分治法最大的差别是：适合于用动态规划法求解的问题，经分解后得到的子问题往往不是互相独立的（即下一个子阶段的求解是建立在上一个子阶段的解的基础上，进行进一步的求解)  

```md
   解决动态规划问题一般的步骤是：

1. 找出最优解的性质，刻画其结构特征和最优子结构特征；
2. 递归地定义最优值，刻画原问题解与子问题解间的关系；
3. 以自底向上的方式计算出各个子问题、原问题的最优值，并避免子问题的重复计算；
4. 根据计算最优值时得到的信息，构造最优解。 
``` 

<br>
&emsp;&emsp;应用场景：  

&emsp;&emsp;适用动态规划的问题必须满足最优化原理、无后效性和重叠性。  
1. **最优化原理**（最优子结构性质） 最优化原理可这样阐述：一个最优化策略具有这样的性质，不论过去状态和决策如何，对前面的决策所形成的状态而言，余下的诸决策必须构成最优策略。简而言之，一个最优化策略的子策略总是最优的。一个问题满足最优化原理又称其具有最优子结构性质。

2. **无后效性**  将各阶段按照一定的次序排列好之后，对于某个给定的阶段状态，它以前各阶段的状态无法直接影响它未来的决策，而只能通过当前的这个状态。换句话说，每个状态都是过去历史的一个完整总结。这就是无后向性，又称为无后效性。

3. **子问题的重叠性**  动态规划将原来具有指数级时间复杂度的搜索算法改进成了具有多项式时间复杂度的算法。其中的关键在于解决冗余，这是动态规划算法的根本目的。动态规划实质上是一种以空间换时间的技术，它在实现的过程中，不得不存储产生过程中的各种状态，所以它的空间复杂度要大于其它的算法。


### 例子
例1：[POJ1651--Multiplication Puzzle](http://poj.org/problem?id=1651)  
&emsp;&emsp;1) **题意：**   
&emsp;&emsp;给出一组N个数，每次从中抽出一个数（第一和最后一个不能抽），该次的得分即为抽出的数与相邻两个数的乘积。直到只剩下首尾两个数为止。问最小得分？  
&emsp;&emsp;2) **解题思路**   
&emsp;&emsp;假设有a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub>三个数，那么我们只能取a<sub>2</sub>，最后得分为 a<sub>1</sub>\*a<sub>2</sub>\*a<sub>3</sub> ;假如有n个数，设k为最后一次取出的数，那么最后一次的得分只与a<sub>1</sub>, a<sub>k</sub>, a<sub>n</sub>有关，与其他数无关，那么我们可以把整个区间以k为中心分成两段，左边一段的最后一次得分必然为a<sub>1</sub>, a<sub>i</sub>, a<sub>k</sub>, 其中1 < i < k,且左边如何取与右边无关，右边同理。  
&emsp;&emsp;因此可得 `dp[1][n] = dp[1][k] + dp[k][n] + a[1]*a[k]*a[n]`, 且对于任意的 `dp[i][j]` 都有 `dp[i][j] = dp[i][k] + dp[k][j] + a[i]*a[k]*a[j]`，所以最终结果就是要计算 `dp[i][j] = min(a[i] * a[k] * a[j] + dp[i][k] + dp[k][j])   i<k<j`  
&emsp;&emsp;3) **伪代码**   
```python
dp = []
INF = 99999
def solve(i, j):
    if dp[i][j] != INF:
        return dp[i][j]
    if j == i + 1:
        return dp[i][j]=0;
    for k in range(i+1, j)
        dp[i][j]=min(dp[i][j], a[k] * a[i] * a[j] + solve(i,k) + solve(k,j));
    return dp[i][j];

def solution(nums):
    #init dp
    for l in range(len(nums)):
        dp[l] = [INF]*len(nums)
    return solve(0, n-1)
```
<br>

例2：[POJ1163--The Triangle](http://poj.org/problem?id=1163)  
&emsp;&emsp;1) **题意：**  
&emsp;&emsp;有一个由非负整数组成的三角形，第一行只有一个数，除了最下行之外每个数的左下方和右下方各有一个数，从第一行的数开始，每次可以往左下和右下走一格，直到走到最下行，把沿途经过的数全部加起来，如何才能使这个和最大？  
&emsp;&emsp;2) **解题思路**   
&emsp;&emsp;把当前的位置（i,j）看成一个状态，然后定义状态（i,j）的指标函数d(i,j)为从格子（i，j）出发时能得到的最大和（包括（i，j）本身的值）。在这个状态定义下，原问题的解为d(1,1)。从格子（i，j）出发有两种决策，往左下走或者往右下走，所以应选择 `d(i+1,j) 与 d(i+1,j+1)` 中较大的那一个，即 `d(i,j) = (i,j) + max{d(i+1,j), d(i+1,j+1)}`  
&emsp;&emsp;3) **伪代码**  
```python
# 从下至上
def solution(nums):
    for i in range(len(nums)-2, -1, -1):
        for j in range(i+1):
            nums[i][j] += max(nums[i+1][j], nums[i+1][j+1])
```
<br>

例3：[POJ1458--Common Subsequence](http://poj.org/problem?id=1458)  
&emsp;&emsp;1) **题意：**  
&emsp;&emsp;给你两个字符串, 要你求出两个字符串的最长公共子序列长度。(LCS)  
&emsp;&emsp;2) **解题思路**   
&emsp;&emsp;令 `dp[i][j] = x` 表示 A 串的前 i 个字符和 B 串的前 j 个字符的最长公共子序列长度为 x .那么如果 `A[i] == B[j]`，则 `dp[i][j] =  dp[i-1][j-1] + 1`, 否则 `dp[i][j] = max(dp[i-1][j], dp[i][j-1])` 最终要求 `dp[n][m]`  
&emsp;&emsp;3) **伪代码** 
```python
def solution(s1, s2):
    dp = []
    # init dp
    for i in range(len(s1)):
        dp[i] = [0]*len(s2)
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[len(s1)][len(s2)]
```
<br>

例4：[POJ2533--Longest Ordered Subsequence](http://poj.org/problem?id=2533)  
&emsp;&emsp;1) **题意：**   
&emsp;&emsp;给出一序列，求出该序列的最长上升子序列的最大长度。  
&emsp;&emsp;2) **解题思路**   
&emsp;&emsp;外层循环 i 遍历整个数组，内层循环 j 遍历 i 之前的数，只要找到 j 小于 i ，即 `A[j] < A[i]` ,dp[i] 便可以 +1，状态转移方程为 `if A[j] < A[i]` 那么 `dp[i] = max(1, dp[j] + 1)` ，所以置 dp 初始化为 1 ，每次更新 dp[i] 即可，最后比较每个 dp[i]，最大的即为要求的结果。  
&emsp;&emsp;3) **伪代码**  
```python
def solution(nums):
    # init dp
    dp = [1]*len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    return max(dp)
```
<br>

例5：[最大子段和](https://baike.baidu.com/item/%E6%9C%80%E5%A4%A7%E5%AD%90%E6%AE%B5%E5%92%8C/14891077?fr=aladdin)  
&emsp;&emsp;1) **题意：**   
&emsp;&emsp;给定n个整数组成的序列a1,a2,…,an，求该序列子段和的最大值。  
&emsp;&emsp;2) **解题思路**   
&emsp;&emsp;如果我们知道了某个数前面一段数的和，我们就该考虑把这个数加入到前一段，还是重新开始一段。若记 dp[j] 为前面一段的和，其中 1 <= j <= n 。注意，dp[j]一定包括了a[j], 且 dp[j] 不一定是从 0 开始的。因此所求的最大子段和为 `max(dp[j])，1 <= j <= n` 。由 dp[j] 的定义可知，当 dp[j-1] > 0 时 `dp[j] = dp[j-1] + a[j]`，否则 dp[j] = a[j] (重新开始一段)。故 dp[j] 的动态规划递归式为: `dp[j] = max(dp[j-1]+a[j], a[j])，1 <= j <= n`。  
&emsp;&emsp;3) **伪代码**  
```python
def solution(nums):
    # init dp
    dp = [0]*len(nums)
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(dp[i-1]+nums[i], nums[i])
    return max(dp)
```
<br>

例6：[背包问题](https://baike.baidu.com/item/%E8%83%8C%E5%8C%85%E9%97%AE%E9%A2%98/2416931?fr=aladdin)  
&emsp;&emsp;1) **题意：**   
&emsp;&emsp; **零一背包问题** : 有 n 种重量和价值分别为 W<sub>i</sub> 和 V<sub>i</sub> 的物品。从这些物品中挑选出总重量不超过 w 的物品，每种物品都只能挑选一件，求所有挑选方案中价值总和的最大值。  
&emsp;&emsp;2) **解题思路**   
&emsp;&emsp;在给定的重量范围内，挑选前 i 件物品的最大价值量为在保证第 i 件物品可以放入背包中时,挑选前 i - 1 件物品在剩余的重量中的最大价值量加上第 i 件物品的价值与前 i - 1 件物品在给定重量范围内最大价值量的最大值；如果第 i 件物品无法放入背包中，那么就只能将前 i-1 件商品放入背包中。因此 dp[i][j] 表示前 i 件物品放入容量为 j 的背包中的最大价值量，[详情参考](https://blog.csdn.net/sunhengzhi_212/article/details/81205935)。  
&emsp;&emsp;3) **伪代码**  
```python
def soltion(w, v, W):
    # init dp
    dp = [0]*len(w)
    for i in range(len(w)):
        dp[i] = [0]*W
    for i in range(1, len(w)):
        for j in range(1, W):
            if i == 0:
                if w[i] >= j:
                    dp[i][j] = v[i]
                continue
            elif j < w[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]]+v[i])
    return dp[len(w)-1, W-1]
```
---
---
&emsp;&emsp;1) **题意：**   
&emsp;&emsp; **完全背包问题** : 有 n 种重量和价值分别为 W<sub>i</sub> 和 V<sub>i</sub> 的物品。从这些物品中挑选出总重量不超过w的物品，每种物品都可以挑选多件，求所有挑选方案中价值总和的最大值。  
&emsp;&emsp;2) **解题思路**   
&emsp;&emsp;对于完全背包问题，当我们用了第 i 件物品以后，因为第 i 件物品还可以再次被用，因此其中一个最优子结构 `dp[i - 1, j - w[i]] + v[i]` 应该变为 `dp[i, j - w[i]] + v[i]` ，代表用了第 n 个物品以后，还可以用第 n 个物品。  
&emsp;&emsp;3) **伪代码**  
```python
def soltion(w, v, W):
    # init dp
    dp = [0]*len(w)
    for i in range(len(w)):
        dp[i] = [0]*W
    for i in range(1, len(w)):
        for j in range(1, W):
            if i == 0:
                if w[i] >= j:
                    dp[i][j] = v[i]
                continue
            elif j < w[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-w[i]]+v[i])
    return dp[len(w)-1, W-1]
```
<br>

