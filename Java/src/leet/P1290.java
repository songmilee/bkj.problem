package leet;

public class P1290 {

    public int getDecimalValue(ListNode head) {
        StringBuilder sb = new StringBuilder();
        int result = 0;

        sb.append(head.val);
        while (head.next != null) {
            head = head.next;
            sb.append(head.val);
        }

        int j = 0;
        for(int i = sb.length() - 1; i >= 0; i--, j++){
            if(sb.charAt(i) == '0') continue;
            result += Math.pow(2, j);
        }

        return result;
    }

    public static void main(String[] args) {
        P1290 p1290 = new P1290();

        ListNode last = new ListNode(1);
        ListNode middle = new ListNode(0, last);
        ListNode first = new ListNode(1, middle);

        int result = p1290.getDecimalValue(first);

        System.out.println(result);
    }

}


class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}
