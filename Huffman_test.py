#import Huffman_Quinary as hq
import Huffman_Binary as hq

sentence = input()
(dict, encode) = hq.Huffman_encode(sentence)
new_dict = {}
for (key, value) in dict.items() :
    new_dict[value] = key

decode = hq.Huffman_decode(new_dict, encode)
print(encode)
print(decode)


##### 문자열 입력 받은 후 허프만 코드로 인코딩한 것과 이를 다시 디코딩한 것을 출력 (맨 위 주석 바꾸면 5진 / 2진 변환할 수 있어요)#####