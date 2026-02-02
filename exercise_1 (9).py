class Tree_Node :
    def __init__(self , x):
        self.Data = x
        self.Lchild = None
        self.Rchild = None
#تابع بازگشتی بنویسید که تعداد برگ های درخت باینری روت را محاسبه کند
def Count_leaves(root):
    if root is None:
        return 0
    if 2 :
#       if root.Lchild is None :
#           and root.Rchild is not None:
#       if root.Rchild is None:
#           and root.Lchild is not None:                
        return 1
    return Count_leaves(root.Lchild) + Count_leaves(root.Rchild)

#تابع بازگشتی بنویسید که گره های درجه یک ، درخت باینری را محاسبه کند
def Count_1Deg(root):
    if root is None:
        return 0
    if root.Lchild:
        return 1
    if root.Rchild:
        return 1
    return Count_1Deg(root.Lchild) + Count_1Deg(root.Rchild)   

def Count_2Deg (root):
    if root is None:
        return 0
    if root.Lchild:
        return Count_2Deg(root.Lchild)
    if root.Rchild:
        return Count_2Deg(root.Rchild)
    return Count_2Deg(root.Lchild) + Count_2Deg(root.Rchild)

#تابعی بازگشتی بنویسید که حاصل جمع تمامی داده های یک درخت دودویی را بازگرداند
def sum_Tree(root):
    if root is None:
        return 0
    if root.Lchild:
        return sum_Tree(root.Lchild) + root.Data
    if root.Rchild:
        return sum_Tree(root.Rchild) + root.Data
    return sum_Tree(root.Lchild) + sum_Tree(root.Rchild) + root.Data

#تابعی بازگشتی بنوبسید که تعداد نود های یک درخت باینری را بازگرداند
def Count(root):
    if root is None:
        return 0
    return 1+ Count(root.Lchild) + Count(root.Rchild)





def pre(root):
    if root is None:
        return
    print(root.Data)
    print(root.Lchild)
    print(root.Rchild)       

#تابعی بازگشتی بنویسید که مقدار تارگت را در یک درخت جستجو کند
def search(root , t):
    if root is None:
        return False
    if root.Data == t:
        return True
    return search(root.Lchild) or search(root.Rchild)      

#تابعی بازگشتی بنویسید که مقدار حداکثر یک درخت را بازگرداند
def max_t(root):
    if root is None:
        return float("inf")
    return max(max_t(root.Lchild) , max_t(root.Rchild) , root.Data)
    










def count(root):
    if root is None:
        return 0
    return 1+ count(root.left) + count(root.right)
 

