class NodeTree(object):                                                                     #허프만 트리를 위한 노드 클래스 생성
    def __init__(self, n1=None, n2=None, n3=None, n4=None, n5=None):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.n5 = n5
    def children(self):
        return (self.n1, self.n2, self.n3, self.n4, self.n5)
    def __str__(self):
        return '%s_%s_%s_%s_%s' % (self.n1, self.n2, self.n3, self.n4, self.n5)

def huffman_code_tree(node, QuiString=''):                                                  #노드와 함께 호출시 허프만 코드 딕셔너리 생성
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
    for c in string:                                                                        #문자별 빈도수 측정해 딕셔너리에 저장
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1

    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    nodes = freq

    while len(nodes) > 1:                                                                   #빈도수 작은 것부터 트리 구성하여 허프만 트리 구성
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
    huffmanCode = huffman_code_tree(nodes[0][0])                                            #허프만 트리 딕셔너리 구성

    encoded = ''
    for char in string:                                                                     #문자열 허프만코드로 인코딩
        encoded += huffmanCode[char]

    return (huffmanCode, encoded)                                                           #허프만 코드 딕셔너리와 인코딩된 문자열 반환

def Huffman_decode(dict, encoded, maxlen, minlen) :                             #Huffman_Quinary와 다른 점은 여기서 딕셔너리의 key 값을 정수로 변환하여 인식한다는 점..
    i = minlen - 1
    j = maxlen + 1
    decoded = ''
    while encoded != '' :
        if i > maxlen :
            print('error')
            break
        i += 1
        j -= 1
        if int(encoded[:i]) not in dict.keys() :        #이 부분이 골치 아팠습니다.. 딕셔너리 정보의 자릿수가 고정되어 들어와서 원래 코드의 자릿수를 몰라서 정수로 바꿔서
            if int(encoded[:j]) in dict.keys() :        #넣었는데 문제가 발생했었습니다. 예를들어 01을 1로 처리하기 때문에 01과 123이 있을 때 인코딩된 문자열에서 
                d = dict[int(encoded[:j])]              #앞에서부터 비교를 하면 123에서는 123이 아닌 1이 먼저 나오게 됩니다. 그래서 코드들의 최소자리수를 구해 거기부터 
                                                        #앞에서 스캔을 하면 드물지만 동일한 문제가 3자리에서 발생했습니다. 그래서 반대로 최대자리수를 구해 그것부터
                decoded += d                            #뒤에서 스캔을 하게되면 발생하는 문제가 01, 02, 03, 123이 있을 때 123을 입력하면 123이 아닌 01,02,03으로
                encoded = encoded[j:]                   #인식한다는 문제가 있었습니다. 그래서 이를 섞어 우선 최소자릿수에서부터 앞에서 스캔을 하되 동시에 뒤에서도 스캔을
                i = minlen - 1                          #해서 앞에서 나온 결과를 우선으로 하되 앞에서 딕셔너리에 해당하는 값이 없으면 뒤에서 스캔한 것을 사용하게
                j = maxlen + 1                          #만들었습니다.
            continue
        d = dict[int(encoded[:i])]
        decoded += d
        encoded = encoded[i:]
        i = minlen - 1
        j = maxlen + 1
    return decoded