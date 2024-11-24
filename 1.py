def addNodeToStack(item:int, top:Node)->Node:
    x = Node()
    x.data = item
    x.link = top
    top = x
    return top

def delStack(top: Node) -> tuple[int, Node]:
    if top is None:
        raise Exception("STACK_EMPTY")
    x = top
    item = x.data
    top = top.link
    del x
    
def addQueue(item,front,rear):
    x = Node()
    x.data = item
    x.link = None
    rear.link = x
    rear = x
    return front, rear

def delQueue(front,rear):
    if front is None:
        raise Exception("Queue_Empty")
    else:
        x = front
        front = front.link
        del x
    return front,rear     