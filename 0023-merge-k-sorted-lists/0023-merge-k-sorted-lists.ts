/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */
function mergeTwoLists(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    const dummy = new ListNode();
    let curr = dummy;
    while (l1 !== null && l2 !== null) {
        if (l1.val <= l2.val) {
            curr.next = l1;
            l1 = l1.next;
        } else {
            curr.next = l2;
            l2 = l2.next;
        }
        curr = curr.next; 
    }
    curr.next = l1 !== null ? l1 : l2;
    return dummy.next;
}
function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
    if (lists.length === 0) {
        return null;
    }
    while (lists.length > 1) {
        let mergedLists: Array<ListNode | null> = [];
        for (let i=0;i<lists.length;i+=2) {
            let l1 = lists[i];
            let l2 = i+1<lists.length ?  lists[i+1] : null;
            
            mergedLists.push(mergeTwoLists(l1, l2));
        }
        lists = mergedLists;    
    }
    return lists[0];

};