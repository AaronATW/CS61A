email = 'example_key'

def symdiff(salmons):
    """
    A 'salmon list' is a linked list that contains integers in increasing order
        with no duplicates.

    The symdiff operation takes in a list of salmon lists and produces a salmon list that
        contains the elements that appear in an odd number of the
        original lists. It does not modify the original lists.

    >>>> salmon1 = Link(0, Link(1, Link(2, Link(3,  Link(5, Link(9))))))
    >>>> salmon2 = Link(1, Link(4))
    >>>> symdiff([salmon1, salmon2])
    Link(0, Link(2, Link(3, Link(4, Link(5, Link(9))))))
    >>>> salmon1 # unchanged
    Link(0, Link(1, Link(2, Link(3, Link(5, Link(9))))))
    >>>> salmon2 # unchanged
    Link(1, Link(4))
    >>>> salmon1 = Link(0, Link(1, Link(2, Link(3,  Link(5, Link(9))))))
    >>>> salmon2 = Link(1, Link(4))
    >>>> symdiff([salmon1, salmon1, salmon2])
    Link(1, Link(4))
    >>>> salmon3 = Link(0, Link(1, Link(2, Link(3,  Link(5, Link(9))))))
    >>>> salmon4 = Link(1, Link(2, Link(3,  Link(5, Link(9)))))
    >>>> symdiff([salmon3, salmon4])
    Link(0)
    >>>> symdiff([salmon1, salmon2, salmon3, salmon4])
    Link(2, Link(3, Link(4, Link(5, Link(9)))))
    """
    salmons = [salmon for salmon in salmons if len(salmon) > 0]
    if not salmons:
        return Link.empty
    first = min([salmon.first for salmon in salmons])
    new_salmons = []
    count = 0
    for salmon in salmons:
        if salmon.first == first:
            count, salmon = count + 1, salmon.rest
        new_salmons.append(salmon)
    if count % 2 == 0:
        return symdiff(new_salmons)
    else:
        return Link(first, symdiff(new_salmons))

class Link:
    """A linked list.

    >>>> s = Link(1, Link(2, Link(3, Link(4))))
    >>>> len(s)
    4
    >>>> s[2]
    3
    >>>> s
    Link(1, Link(2, Link(3, Link(4))))
    """
    empty = ()

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

    def __len__(self):
        return 1 + len(self.rest)

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)

# ORIGINAL SKELETON FOLLOWS

# def symdiff(salmons):
#     """
#     A 'salmon list' is a linked list that contains integers in increasing order
#         with no duplicates.

#     The symdiff operation takes in a list of salmon lists and produces a salmon list that
#         contains the elements that appear in an odd number of the
#         original lists. It does not modify the original lists.

#     >>>> salmon1 = Link(0, Link(1, Link(2, Link(3,  Link(5, Link(9))))))
#     >>>> salmon2 = Link(1, Link(4))
#     >>>> symdiff([salmon1, salmon2])
#     Link(0, Link(2, Link(3, Link(4, Link(5, Link(9))))))
#     >>>> salmon1 # unchanged
#     Link(0, Link(1, Link(2, Link(3, Link(5, Link(9))))))
#     >>>> salmon2 # unchanged
#     Link(1, Link(4))
#     >>>> salmon1 = Link(0, Link(1, Link(2, Link(3,  Link(5, Link(9))))))
#     >>>> salmon2 = Link(1, Link(4))
#     >>>> symdiff([salmon1, salmon1, salmon2])
#     Link(1, Link(4))
#     >>>> salmon3 = Link(0, Link(1, Link(2, Link(3,  Link(5, Link(9))))))
#     >>>> salmon4 = Link(1, Link(2, Link(3,  Link(5, Link(9)))))
#     >>>> symdiff([salmon3, salmon4])
#     Link(0)
#     >>>> symdiff([salmon1, salmon2, salmon3, salmon4])
#     Link(2, Link(3, Link(4, Link(5, Link(9)))))
#     """
#     salmons = [______ for ______ in ______ if ______]
#     if ______:
#         return Link.empty
#     first = min(______)
#     new_salmons = []
#     count = 0
#     for salmon in salmons:
#         if ______:
#             ______, ______ = ______, ______
#         new_salmons.append(salmon)
#     if ______:
#         return symdiff(new_salmons)
#     else:
#         return ______

# class Link:
#     """A linked list.

#     >>>> s = Link(1, Link(2, Link(3, Link(4))))
#     >>>> len(s)
#     4
#     >>>> s[2]
#     3
#     >>>> s
#     Link(1, Link(2, Link(3, Link(4))))
#     """
#     empty = ()

#     def __init__(self, first, rest=empty):
#         self.first = first
#         self.rest = rest

#     def __getitem__(self, i):
#         if i == 0:
#             return self.first
#         else:
#             return self.rest[i-1]

#     def __len__(self):
#         return 1 + len(self.rest)

#     def __repr__(self):
#         if self.rest:
#             rest_str = ', ' + repr(self.rest)
#         else:
#             rest_str = ''
#         return 'Link({0}{1})'.format(repr(self.first), rest_str)
