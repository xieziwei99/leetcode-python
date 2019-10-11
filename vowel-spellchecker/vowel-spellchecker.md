## 问题描述

- 给定一个正确单词的列表`wordlist`，写一个单词检查器，将查询的单词转化为正确的单词
- 我们检查两个方面：
  - 若单词中出现大小写不一致，则返回`wordlist`中第一个匹配的单词（情况1）
  - 若单词中出现将元音字母更换后，可使其一致时，返回`wordlist`中的第一个匹配的单词（情况2）
- 其他情况，返回空字符串

> 详细问题介绍查看 [leetcode](https://leetcode.com/problems/vowel-spellchecker/)



## 解决算法 1

- 分三种情况进行匹配，且按先后顺序进行检查
  - 若查询单词完全匹配，则直接返回
  - 情况1，将`wordlist`和查询单词都全部转化为小写，可以解决
  - 情况2，抽取出`wordlist`中的辅音字母，若与查询单词对应位置上辅音字母相同，且查询单词其他字母均为元音，则OK

> 对于情况2，查看 leetcode 上解决办法后，可将`wordlist`和查询单词中的元音字母用同一个特殊字符如`*`表示，然后比较两者是否相同



## 代码 1

### Java 版

```java
package vowel_spellchecker;

import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;

/**
 * @author xieziwei99
 * 2019-10-11
 */
public class Solution {
    public static void main(String[] args) {
        String[] wordlist = {"KiTe", "kite", "hare", "Hare"};
        String[] queries = {"kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti",
                "keet", "keto"};
        String[] spellchecker = new Solution().spellchecker(wordlist, queries);
        assert Arrays.equals(spellchecker, new String[]{"kite", "KiTe", "KiTe", "Hare", "hare", "", "",
                "KiTe", "", "KiTe"});
    }

    /**
     * 将单词中的元音字母用同一个特殊字符如`*`表示，并全部转换为小写
     *
     * @param s 输入字符串
     * @return 用 ‘*’代替元音字母后的字符串
     */
    private String replaceVowel(String s) {
        String ret = s.toLowerCase();
        for (char c : Arrays.asList('a', 'e', 'i', 'o', 'u')) {
            ret = ret.replace(c, '*');
        }
        return ret;
    }

    private String[] spellchecker(String[] wordlist, String[] queries) {
        String[] ret = new String[queries.length];
        HashSet<String> check1 = new HashSet<>();   // 完全匹配
        HashMap<String, String> check2 = new HashMap<>();   // 大小写不一致
        HashMap<String, String> check3 = new HashMap<>();   // 将元音字母更换
        for (String s : wordlist) {
            check1.add(s);
            check2.putIfAbsent(s.toLowerCase(), s);
            check3.putIfAbsent(replaceVowel(s), s);
        }
        for (int i = 0; i < queries.length; i++) {
            if (check1.contains(queries[i])) {
                ret[i] = queries[i];
            } else if (check2.containsKey(queries[i].toLowerCase())) {
                ret[i] = check2.get(queries[i].toLowerCase());
            } else {
                ret[i] = check3.getOrDefault(replaceVowel(queries[i]), "");
            }
        }
        return ret;
    }
}
```

