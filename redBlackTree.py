import uuid
import inspect
from graphviz import Digraph
l=[]
l1=[]
l2=0
l3=[]
def fun(a,l,l2,e,d2):
    c = 0
    for i in l:
        if i==a+1:
            print (a,i)
            if c==0:
                print (l.index(a),l.index(i))
                print(l2[l.index(a)],l2[l.index(i)])
                if d2[l.index(a)] == 0:
                    e.node(str(l2[l.index(a)]), style='filled', color='red')
                else:
                    e.node(str(l2[l.index(a)]), style='filled', color='gray')
                if d2[l.index(i)] == 0:
                    e.node(str(l2[l.index(i)]), style='filled', color='red')
                else:
                    e.node(str(l2[l.index(i)]), style='filled', color='gray')

                e.edge(str(l2[l.index(a)]),str(l2[l.index(i)]))
            if c==1:
                k=i
                k2=l.index(i)
                l[l.index(i)]=100
                print(l.index(a), l.index(i))
                print(l2[l.index(a)],l2[l.index(i)])
                if d2[l.index(a)] == 0:
                    e.node(str(l2[l.index(a)]), style='filled', color='red')
                else:
                    e.node(str(l2[l.index(a)]), style='filled', color='gray')
                if d2[l.index(i)] == 0:
                    e.node(str(l2[l.index(i)]), style='filled', color='red')
                else:
                    e.node(str(l2[l.index(i)]), style='filled', color='gray')

                e.edge(str(l2[l.index(a)]),str(l2[l.index(i)]))
                l[k2]=k

            c+=1
            if c==2:
                print("stop")
                break

class Color(object):
    RED = 0
    BLACK = 1
class RedBlackTree(object):
    def obh(self):
        global l2
        if self.left.value!=0:
            l2+=1
            self.left.obh()
        if self.right.value!=0:
            l2+=1
            self.right.obh()
        print(self.value)
        assert isinstance(self.value, object)
        l.append(self.value)
        l3.append(self.color)
        l1.append(l2)
        l2-=1

    def __init__(self, left, value, right, color=Color.RED):
        self._color = color
        self._left = left
        self._right = right
        self._value = value
        self._count = 1 + len(left) + len(right)
        self._node_uuid = uuid.uuid4()

    def __len__(self):
        return self._count
    @property
    def uuid(self):
        return self._node_uuid
    @property
    def color(self):
        return self._color
    @property
    def value(self):
        return self._value
    @property
    def right(self):
        return self._right
    @property
    def left(self):
        return self._left
    def blacken(self):
        if self.is_red():
            return RedBlackTree(
                self.left,
                self.value,
                self.right,
                color=Color.BLACK,
            )
        return self
    def is_empty(self):
        return False
    def is_black(self):
        return self._color == Color.BLACK
    def is_red(self):
        return self._color == Color.RED
    def rotate_left(self):
        return RedBlackTree(
            RedBlackTree(
                self.left,
                self.value,
                EmptyRedBlackTree().update(self.right.left),
                color=self.color,
            ),
            self.right.value,
            self.right.right,
            color=self.right.color,
        )
    def rotate_right(self):
        return RedBlackTree(
            self.left.left,
            self.left.value,
            RedBlackTree(
                EmptyRedBlackTree().update(self.left.right),
                self.value,
                self.right,
                color=self.color,
            ),
            color=self.left.color,
        )
    def recolored(self):
        return RedBlackTree(
            self.left.blacken(),
            self.value,
            self.right.blacken(),
            color=Color.RED,
        )
    def balance(self):
        if self.is_red():
            return self
        if self.left.is_red():
            if self.right.is_red():
                return self.recolored()
            if self.left.left.is_red():
                return self.rotate_right().recolored()
            if self.left.right.is_red():
                return RedBlackTree(
                    self.left.rotate_left(),
                    self.value,
                    self.right,
                    color=self.color,
                ).rotate_right().recolored()
            return self
        if self.right.is_red():
            if self.right.right.is_red():
                return self.rotate_left().recolored()
            if self.right.left.is_red():
                return RedBlackTree(
                    self.left,
                    self.value,
                    self.right.rotate_right(),
                    color=self.color,
                ).rotate_left().recolored()
        return self

    def update(self, node):
        if node.is_empty():
            return self
        if node.value < self.value:
            return RedBlackTree(
                self.left.update(node).balance(),
                self.value,
                self.right,
                color=self.color,
            ).balance()
        return RedBlackTree(
            self.left,
            self.value,
            self.right.update(node).balance(),
            color=self.color,
        ).balance()

    def insert(self, value):
        return self.update(
            RedBlackTree(
                EmptyRedBlackTree(),
                value,
                EmptyRedBlackTree(),
                color=Color.RED,
            )
        ).blacken()

    def is_member(self, value):
        if value < self._value:
            return self.left.is_member(value)
        if value > self._value:
            return self.right.is_member(value)
        return True


class EmptyRedBlackTree(RedBlackTree):

    def __init__(self):
        self._color = Color.BLACK
        self._value=0
        self.l2=0

    def is_empty(self):
        return True
    # def value(self):
    #     return self._value
    def insert(self, value):
        return RedBlackTree(
            EmptyRedBlackTree(),
            value,
            EmptyRedBlackTree(),
            color=Color.RED,
        )

    def update(self, node):
        return node

    def is_member(self, value):
        return False

    @property
    def left(self):
        return EmptyRedBlackTree()

    @property
    def right(self):
        return EmptyRedBlackTree()

    def __len__(self):
        return 0

new_tree = EmptyRedBlackTree().insert(1)
new_tree = new_tree.insert(2)
new_tree = new_tree.insert(3)
new_tree=new_tree.insert(4)
new_tree = new_tree.insert(5)
new_tree = new_tree.insert(6)
new_tree=new_tree.insert(7)
new_tree=new_tree.insert(25)
new_tree=new_tree.insert(23)
new_tree=new_tree.insert(26)
new_tree.obh()
print(l,l1,l3)
g = Digraph('G', filename='hello.gv')
l1.reverse()
l.reverse()
l3.reverse()
for i in l1:
    fun(i, l1, l, g,l3)
    l1=l1[1:]
    l=l[1:]
    l3=l3[1:]
g.view()