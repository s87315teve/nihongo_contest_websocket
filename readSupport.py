#單字的class
class Tango :
    kanji=''
    yomikata=''
    imi=''
    part=''
    type=''
    source=''
    def __init__(self, kanji,yomikata):
        self.kanji=kanji
        self.yomikata=yomikata



def getPart(part,tempTango):
    mode_part=[]
    #名詞
    if part==1:
        for temp in tempTango:
            if temp.part=='名詞':
                mode_part.append(temp)
    #動詞
    elif part==2:
        for temp in tempTango:
            if temp.part=='動詞':
                mode_part.append(temp)
    #形容詞
    elif part==3:
        for temp in tempTango:
            if temp.part=='形容詞':
                mode_part.append(temp)
    #副詞
    elif part==4:
        for temp in tempTango:
            if temp.part=='副詞':
                mode_part.append(temp)
    #print(mode_part[0].kanji)
    return mode_part

def getNanido(nanido,tempTango):
    mode_nanido=[]
    for temp in tempTango:
        if temp.nanido=='N'+nanido:
            mode_nanido.append(temp)
    #print(outTango.kanji)
    return mode_nanido

