class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
         
            fast = head 
            slow = head
            while(fast != None and fast.next != None):
                fast = fast.next.next
                slow = slow.next
                if(slow == fast ):
                    return True
                
            return False    
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast,slow = head,head
        while(fast != None and fast.next != None):
            fast = fast.next.next
            slow =slow.next 
            if(fast == slow ):
                current = head
                while(current != slow ):
                    current = current.next
                    slow = slow.next 
                return slow
        return None   

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) :
        h1 = headA
        h2 = headB
        
        while h1 != h2:
            if(not h1):
                h1 = headB
            else:
                h1 = h1.next
                           
            
            if(not h2):
                h2 = headA
            else:    
                h2 = h2.next
                
        return h1        
        
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast , slow = head , head
        
        for i in range(n):
            fast = fast.next
            
        if(not fast) : return head.next
        while( fast.next ):
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head   
        
        
        
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head 
        
        while(curr):  
          nex = curr.next
          curr.next = prev
          prev = curr
          curr = nex
        
        return prev            
        
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None :
            return head
        if head.next == None :
            return head
        odd , oddhead = head,head
        even , evenhead = head.next , head.next
        while(even != None and even.next != None):
         odd.next = even.next
         odd = odd.next
         even.next = odd.next
         even = even.next
        odd.next = evenhead
        return oddhead    
        
     def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        while(slow):
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        left,right = head,prev
        while(right):
            if(left.val != right.val):
                return False
            left = left.next
            right = right.next
        return True   
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        resultList = ListNode()
        ref = resultList
        if(list1 is None and list2 is None):
            return ref.next
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val <= list2.val:
            resultList = list1
            list1 = list1.next
        else:
            resultList = list2
            list2 = list2.next
        ref = resultList
        while list1 is not None and list2 is not None :
            if list1.val <= list2.val:
                ref.next = list1
                ref = ref.next
                list1 = list1.next
            else:
                ref.next = list2
                ref = ref.next
                list2 = list2.next
        if list1 is None:
            ref.next = list2
        else:
            ref.next = list1
        return resultList
    
        def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            resultList = ListNode()
            res = resultList
            if(l1 is None and l2 is None):
                return res.next
            if(l1 is None ):
                return l2
            if(l2 is None):
                return l1

            sum = 0 
            sum = l1.val + l2.val 
            carry = sum // 10 
            l1 = l1.next 
            l2 = l2.next 
            res = ListNode(sum % 10,None )
            resultList = res


            while(l1 and l2):
                sum = l1.val + l2.val + carry 
                l1 = l1.next
                l2 = l2.next
                res.next = ListNode(sum % 10,None)
                res = res.next
                carry = sum // 10 

            while(l1):
                sum = l1.val + carry 
                l1 = l1.next
                res.next = ListNode(sum % 10,None)
                res = res.next
                carry = sum // 10 

            while(l2):
                sum = l2.val + carry 
                l2 = l2.next
                carry = sum // 10 
                res.next = ListNode(sum % 10,None) 
                res = res.next

            if (carry > 0 ):
                res.next = ListNode(carry,None)
            return resultList
