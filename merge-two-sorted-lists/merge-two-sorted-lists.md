#### 问题描述

- 合并两个已排序的链表，并将其作为一个新列表返回。新列表应该通过将前两个列表的节点拼接在一起来创建。

- **Example:**

  ``` sh
  Input: 1->2->4, 1->3->4
  Output: 1->1->2->3->4->4
  ```



#### 解法1（C语言）

- 用两个指针分别指向两个链表头
- 依次向后比较，将较小者加入新建链表尾部，被加入的链表指针向后加一
- 直到某个链表指针到达尾部，将另一个剩余的链表加入新建链表尾部即可



#### 代码1（C语言）

```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2){
    struct ListNode* pa = l1;
    struct ListNode* pb = l2;
    struct ListNode* pc;
    struct ListNode* lc;
    lc = (struct ListNode*)malloc(sizeof(struct ListNode));
    pc = lc;
    while (pa && pb)
    {
        if (pa->val <= pb->val)
        {
            pc->next = pa;
            pa = pa->next;
        }
        else if(pa->val > pb->val)
        {
            pc->next = pb;
            pb = pb->next;
        }
        pc = pc->next;
    }
    pc->next = pa ? pa : pb; //pa存在则为pa, 不存在则为pb
    return lc->next;
}
```

