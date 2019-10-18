## 问题描述

- 见[官网](https://leetcode.com/problems/grumpy-bookstore-owner/)



## 算法 1

例如，对于：

```shell
Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. 
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
```

这实际上是一个求规定长度的子串最大的和的问题：

将 customers 和 grumpy 数组对应位置相乘，可以得到 [0,0,0,2,0,1,0,5]，可知 [1,0,5] 最大，问题得解



## 代码 1

### using Java

```java
package grumpy_bookstore_owner;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

/**
 * 暴躁的书店老板
 * @author xieziwei99
 * 2019-10-18
 */
public class Solution {
    public int maxSatisfied(int[] customers, int[] grumpy, int X) {
        int ret = 0;
        List<Integer> temp = new ArrayList<>();
        for (int i = 0; i < customers.length; i++) {
            temp.add(customers[i] * grumpy[i]);
            if (0 == grumpy[i]) {
                ret += customers[i];
            }
        }
        int maxTemp = 0;
        for (int i = 0; i < temp.size() - X + 1; i++) {
            Optional<Integer> reduce = temp.subList(i, i + X).stream().reduce(Integer::sum);
            if (reduce.isPresent()) {
                maxTemp = Math.max(maxTemp, reduce.get());
            }
        }
        return ret + maxTemp;
    }

    public static void main(String[] args) {
        int[] customers = {1,0,1,2,1,1,7,5};
        int[] grumpy = {0,1,0,1,0,1,0,1};
        int X = 3;
        System.out.println(new Solution().maxSatisfied(customers, grumpy, X));
    }
}
```

