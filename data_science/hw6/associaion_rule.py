import math
import collections
import itertools


class AssociationRuleMiningBase:
    """ the base class of associaion rule mining algorithm """

    def __init__(self):
        self._n_transactions = 0  # number of transactions
        self._min_support = 0  # minmun number of frequent pattern
        self._transactions = list()  # [transaction, ...]
        self.patterns = list()  # [(pattern, rate), ...]

    def fit(self, transactions, support_rate=0.7):
        """ fit the transaction and get the frequent patterns """
        self._n_transactions = len(transactions)
        self._min_support = math.ceil(self._n_transactions*support_rate)
        self._transactions = list((set(tx) for tx in transactions))
        self.patterns = []
        return self


class Apriori(AssociationRuleMiningBase):
    def __init__(self):
        super().__init__()

    def fit(self, transactions, support_rate=0.7):
        super().fit(transactions, support_rate)
        # store all items
        frequent_items = set()
        frequent_items.update(*self._transactions)

        # interate from 1-itemset to n-itemset
        n_itemset = 1
        while frequent_items:  # there still have frequent items to be iterate
            # generate itemset by combinating frequent items
            itemsets = itertools.combinations(frequent_items, n_itemset)
            frequent_items.clear()

            for itemset in itemsets:
                # count the number of itemset
                count = sum(int(tx.issuperset(itemset))
                            for tx in self._transactions)

                # determine whether itemset is frequent
                if count >= self._min_support:
                    self.patterns.append((itemset, count/self._n_transactions))
                    # all these frequent items will be use in next interation
                    frequent_items.update(itemset)
            n_itemset += 1
        return self


class _FPNode:
    """ Node for FP-tree """

    def __init__(self, item=None, count=1):
        self.parent = None
        self.children = dict()  # {item: child, ...}
        self.item = item  # the item must be hashable
        self.count = count

    def add_child(self, child):
        child.parent = self
        self.children[child.item] = child


class FPTree(AssociationRuleMiningBase):

    def __init__(self):
        super().__init__()
        self._root = None
        self._header_table = dict()  # {item: (count, heads), ...}

    def fit(self, transactions, support_rate=0.7):
        super().fit(transactions, support_rate)
        self._root, self._header_table = self._construct_fptree(
            self._transactions, self._min_support)
        self.patterns = self._mine_subtree(
            self._root, self._header_table, self._min_support, self._n_transactions)
        return self

    @staticmethod
    def _construct_fptree(transactions, min_support):
        """ contrucet FP-tree and return root and header table """
        # count the numbers for each item in transactions
        counter = collections.Counter()
        for transaction in transactions:
            counter.update(transaction)

        # remove items that are not frequent (less than min_support)
        counter = collections.Counter(dict(
            (item, count) for item, count in counter.items() if count >= min_support))

        # if there are 2 item have the same number, the sorting result may be
        # diffrient, this will cause problem when construct the FP-tree, so
        # we generate a fix prioriry of item to make sure that every time we sort
        # the item we get same order
        priorities = dict(zip(sorted(counter), range(len(counter))))

        # order frequent items in frequency descending order and store
        frequent_items_list = []
        for transaction in transactions:
            frequent_items = sorted(set(transaction).intersection(counter),
                                    key=priorities.get, reverse=True)
            frequent_items_list.append(frequent_items)

        # scan frequent items list and consturct FP-tree and header table
        root = _FPNode()
        header_table = dict(
            (item, (count, [])) for item, count in counter.items())
        for items in frequent_items_list:
            current = root
            for item in items:
                if item in current.children:
                    current = current.children[item]
                    current.count += 1
                else:
                    new = _FPNode(item)
                    current.add_child(new)
                    # link new node to the header table
                    header_table[item][1].append(new)
                    current = new
        return root, header_table

    @staticmethod
    def _generate_cond_pattern_bases(heads):
        """ generate conditional patterrn base by a frequent item """
        bases = []
        for head in heads:
            base, current = [], head
            # generate a single base of this frequent item
            while current.parent.item is not None:
                current = current.parent
                base.append(current.item)
            # if base is not equal to 0, copy n base store in bases prepare for
            # generate the conditional FP-tree
            if base:
                bases.extend(base for i in range(head.count))
        return bases

    @classmethod
    def _mine_subtree(cls, root, header_table, min_support, n_transactions):
        """ recursively mine the FP-tree and return frequent patterns """
        patterns = []
        for item, (count, heads) in header_table.items():
            # add single item to patterns
            patterns.append(((item, ), count/n_transactions))
            # construct conditional FP-tree and generate patterns
            cond_bases = cls._generate_cond_pattern_bases(heads)
            cond_root, cond_header_table = cls._construct_fptree(
                cond_bases, min_support)
            for cond_pattern, cond_rate in cls._mine_subtree(
                    cond_root, cond_header_table, min_support, n_transactions):
                pattern = (item, )+cond_pattern, cond_rate
                patterns.append(pattern)
        return patterns


def main():
    transactions = [
        (1, 3, 4),
        (2, 3, 5),
        (1, 2, 3, 5),
        (2, 5),
    ]
    apriori = Apriori().fit(transactions, support_rate=0.5)
    fptree = FPTree().fit(transactions, support_rate=0.5)
    print(apriori.patterns)
    print(fptree.patterns)


if __name__ == '__main__':
    main()
