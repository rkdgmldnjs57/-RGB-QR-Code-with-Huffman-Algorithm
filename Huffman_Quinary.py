class NodeTree(object):
    def __init__(self, n1=None, n2=None, n3=None, n4=None, n5=None):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.n5 = n5
    def children(self):
        return (self.n1, self.n2, self.n3, self.n4, self.n5)
    def __str__(self):
        return '%s_%s_%s_%s_%s' % (self.n1, self.n2, self.n3, self.n4, self.n5)     #허프만 

def huffman_code_tree(node, QuiString=''):
    if type(node) is str:
        return {node: QuiString}
    (n1, n2, n3, n4, n5) = node.children()
    d = dict()
    d.update(huffman_code_tree(n1, QuiString + '0')) 
    d.update(huffman_code_tree(n2, QuiString + '1'))
    d.update(huffman_code_tree(n3, QuiString + '2'))
    d.update(huffman_code_tree(n4, QuiString + '3'))
    d.update(huffman_code_tree(n5, QuiString + '4'))
    return d

def Huffman_encode(string) :
    freq = {}
    for c in string:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1

    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    nodes = freq

    while len(nodes) > 1:
        length = len(nodes)
        for _ in range(5-length) :
            nodes.insert(0,('', 0))
        (key1, c1) = nodes[-1]
        (key2, c2) = nodes[-2]
        (key3, c3) = nodes[-3]
        (key4, c4) = nodes[-4]
        (key5, c5) = nodes[-5]
        nodes = nodes[:-5]
        node = NodeTree(key1, key2, key3, key4, key5)
        nodes.append((node, c1 + c2 + c3 + c4 + c5))
        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
    huffmanCode = huffman_code_tree(nodes[0][0])

    encoded = ''
    for char in string:
        encoded += huffmanCode[char]

    return (huffmanCode, encoded)

def Huffman_decode(dict, encoded) :
    i = 0
    decoded = ''
    while encoded != '' :
        i += 1
        if encoded[:i] not in dict.keys() :
            continue
        d = dict[encoded[:i]]
        decoded += d
        encoded = encoded[i:]
        i=0
    return decoded


##### Huffman_Binary와 구조는 같지만 이진트리에서 오진트리로 추가하여 구성했습니다. #####