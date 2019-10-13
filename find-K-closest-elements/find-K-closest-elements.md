## 问题描述

- 给定一个排序后的数组，两个整数 k 和 x，找出数组中最接近 x 的 k 个元素
- 结果按升序排序
- 如果存在和 x 的距离相等的多个元素，则优先选择较小的元素（例如：x = 5，那么 4 和 6 中优先选择 4）



## 算法 1

- 将输入数组 arr 按照到 x 的距离升序排序
- 取出前 k 个就是所要的结果



## 代码 1

### using Java

```java
package find_K_closest_elements;

import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

/**
 * 从给定数组中找到 k 个和已知数 x 最接近的数
 * @author xieziwei99
 * 2019-10-12
 */
public class Solution {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int k = 4, x = 3;
        System.out.println(new Solution().findClosestElements(arr, k, x));
    }

    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        // 将arr按照到x的距离升序排序
        List<Integer> ret = IntStream.of(arr).boxed().sorted(
                Comparator.comparingInt(a -> Math.abs(a - x))).collect(Collectors.toList());
        // 取出前k个
        ret = ret.subList(0, k);
        ret.sort(Comparator.naturalOrder());
        return ret;
    }
}
```



### using c++

```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm> 

#define EQ(a, b, x) (a == b) 
#define LT(a, b, x) (abs(a - x) < abs(b - x) || (abs(a - x) == abs(b - x) && a < b)) 
#define LQ(a, b, x) (LT(a, b, x) || EQ(a, b, x))

using namespace std;

// 快速排序		平均：O(nlogn)		需设一个栈来实现递归	不稳定
int partition(vector<int>& arr, int low, int high, int x) {		// 进行一趟排序
	int temp = 0;
	temp = arr[low];
	int pivotkey = arr[low];	// 或者 (low + high) / 2，或其他
	while (low < high) {
		while (low < high && LQ(pivotkey, arr[high], x)) {
			high--;
		}
		arr[low] = arr[high];
		while (low < high && LQ(arr[low], pivotkey, x)) {
			low++;
		}
		arr[high] = arr[low];
	}
	arr[low] = temp;
	return low;
}
void quickSort(vector<int>& arr, int low, int high, int x) {
	if (low < high) {		// 长度>1
		int pivotPos = partition(arr, low, high, x);
		quickSort(arr, low, pivotPos - 1, x);
		quickSort(arr, pivotPos + 1, high, x);
	}
}
void quickSort(vector<int>& arr, int x) {
	quickSort(arr, 0, arr.size() - 1, x);
}

class Solution {
public:
	vector<int> findClosestElements(vector<int>& arr, int k, int x) {
		quickSort(arr, x);
		vector<int>::iterator itr = arr.begin();
		arr.erase(itr + k, arr.end());
		sort(arr.begin(), arr.end());
		return arr;
	}
};

int main() {
	vector<int> arr = { 1, 3, 5, 7, 9};
	int k = 4, x = 4;
	arr = Solution().findClosestElements(arr, k, x);
	for (int i = 0; i < arr.size(); i++) {
		cout << arr[i] << " ";
	}
	return 0;
}
```