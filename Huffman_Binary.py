class NodeTree(object):                                         #허프만 트리를 위한 노드 클래스 생성
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
    def children(self):
        return (self.left, self.right)
    def __str__(self):
        return '%s_%s' % (self.left, self.right)            

def huffman_code_tree(node, left=True, binString=''):           #노드와 함께 호출시 허프만 코드 딕셔너리 생성
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d

def Huffman_encode(string) : 
    freq = {}
    for c in string:                                            #문자별 빈도수 측정해 딕셔너리에 저장
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    nodes = freq

    while len(nodes) > 1:                                       #빈도수 작은 것부터 트리 구성하여 허프만 트리 구성
        (key1, c1) = nodes[-1]
        (key2, c2) = nodes[-2]
        nodes = nodes[:-2]
        node = NodeTree(key1, key2)
        nodes.append((node, c1 + c2))
        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
    huffmanCode = huffman_code_tree(nodes[0][0])                #허프만 트리 딕셔너리 구성

    encoded = ''
    for char in string:                                         #문자열 허프만코드로 인코딩
        encoded += huffmanCode[char]
    return (huffmanCode, encoded)                               #허프만 코드 딕셔너리와 인코딩된 문자열 반환

def Huffman_decode(dict, encoded) :                             #허프만 코드 딕셔너리 입력받아 디코딩 후 원본 문자열 반환
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