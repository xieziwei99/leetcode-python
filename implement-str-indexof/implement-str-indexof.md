#### 问题描述

- 返回字符串 s 中子串第一次出现的索引，如果子串不是字符串 s 的一部分，返回-1。
- 当子串是空字符串时，返回0



#### 解法1 - 模式匹配暴力算法



- | 母串 | a b c a b c |
  | ---- | ----------- |
  | 子串 | b c b       |

  |         i = 0          |    j = 0     | 失配 |
  | :--------------------: | :----------: | :--: |
  |  i=1  (**i - j + 1**)  |  **j = 0**   |      |
  |          i++           |     j++      |      |
  |      i++  (i = 3)      | j++  (j = 2) | 失配 |
  | i = 2 ( **i - j + 1**) |  **j = 0**   |      |
  |          ...           |     ...      |      |



#### 代码1 - 模式匹配暴力算法

```python
class Solution:

    @staticmethod
    def str_str(haystack: str, needle: str) -> int:
        i, j = 0, 0
        n1, n2 = len(haystack), len(needle)
        while i < n1 and j < n2:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                i = i - j + 1
                j = 0
        return i - j if j >= n2 else -1
```



#### 解法2 - KMP算法

-  next[j] 数组
- 当失配时，不移动到下一位，而是移动到 next[j]



#### 代码2 - KMP算法 - C语言 - 基1

```c
//得到next[j]
void getNext(MyString str) {
	int i = 1;
	int j = 0;
	next[i] = j;
	while (i < str[0])
	{
		if (j == 0 || str[i] == str[j])
		{
			i++;
			j++;
			if (str[i] != str[j]) next[i] = j;		//修正
			else next[i] = next[j];
		}
		else j = next[j];
	}
}

//模式匹配KMP算法
int index_KMP(MyString str, MyString subStr, int pos) {
	getNext(subStr);
	int i = pos;
	int	j = 1;
	while (i <= str[0] && j <= subStr[0])
	{
		if (str[i] == subStr[j] || j == 0) { i++; j++; }
		else { j = next[j]; }
	}
	if (j > subStr[0]) return i - subStr[0];
	else return 0;
}
```



