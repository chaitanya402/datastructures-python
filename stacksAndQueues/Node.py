from typing import Optional


class Node:
    def __init__(self,data:Optional[int],next):
        self.data = data
        self.next = next

