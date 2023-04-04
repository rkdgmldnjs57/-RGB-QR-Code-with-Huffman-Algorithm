import Huffman_Quinary_4_RGBQR as hq
NOTATION = '0123456789ABCDEF'

def numeral_system(number, base):                                                       #5진수 변환
    q, r = divmod(number, base)
    n = NOTATION[r]
    return numeral_system(q, base) + n if q else n


f = open("save.txt", 'r')                                                               #5진 허프만 코드 문자열 파일입력(QR코드의 색 값을 변환해야하지만
sentence = f.read()                                                                     #영상처리 능력이 딸려서 문자열 디코딩으로 간소화했어요)
f.close()

Decode=str()
dictionary = {}
maxlen = int(sentence[0])
minlen = int(sentence[1])
sentence = sentence[2:]

while True :                                                                            #허프만 코드 문자열 초반의 딕셔너리값 디코딩
    char = chr(int(sentence[0])*25 + int(sentence[1])*5 + int(sentence[2]) + 32)        #key 값(5진수 3자리)
    code = sentence[3:3+maxlen]                                                         #value 값(5진수 (maxlen)자리)
    
    sentence = sentence[3+maxlen:]                                                      #읽은 자리 삭제
    if ord(char) == 32 and int(code) == 0 :                                             #0만 나오는 구간에서 중단
        break
    dictionary[code] = char                                                             #딕셔너리에 추가

dic = {}
for (k, v) in dictionary.items() :                                                      #읽은 딘셔너리의 키값을 정수로 변환하여 허프만 디코드 함수 호출
    dic[int(k)] = v
Decode = hq.Huffman_decode(dic, sentence, maxlen, minlen)
print(Decode)