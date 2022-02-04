import math
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

def function_tokenization(data):
    special_char = ['!','@', '?', '-', '.', ',', '"', ';', '—', "'", '"', '“', '’', '”']
    remove_character = data
    for char in special_char:
        while char in remove_character:
            remove_character = remove_character.replace(char, "")
    remove_split_line = ' '.join(remove_character.splitlines())
    remove_dbl_space = remove_split_line.replace('  ', ' ')
    lowercase = remove_dbl_space.lower()
    words = lowercase.split(' ')

    if '' in words:
        words.remove('')

    for x in range(0, len(words)):
        words[x] = stemmer.stem(words[x])

    return words


def function_type(words):
    i = 0
    k = 0
    count_word = len(words)
    token = []
    stemming = []


    for k in range(count_word):
        token.append(0)

    k = 0
    for word in words:
        if word not in token:
            token[i] = word
            i += 1

    for i in range(count_word):
        if 0 in token:
            token.remove(0)

    token.sort()
    type = []
    # type2 = []
    factory = StopWordRemoverFactory()
    stopWords = factory.get_stop_words()
    for w in token:
        if w not in stopWords:
            type.append(w)
            # type2.append(w)
    return type


def function_get_stopwords(words):
    i = 0
    k = 0
    count_word = len(words)
    token = []
    stemming = []


    for k in range(count_word):
        token.append(0)

    k = 0
    for word in words:
        if word not in token:
            token[i] = word
            i += 1

    for i in range(count_word):
        if 0 in token:
            token.remove(0)

    token.sort()
    type = []
    # type2 = []
    factory = StopWordRemoverFactory()
    stopWords = factory.get_stop_words()
    list_stopwords = []
    for w in token:
        if w in stopWords and w not in list_stopwords:
            list_stopwords.append(w)

    # print(list_stopwords)
    return list_stopwords


def function_cari_term(teks_biasa):
    data = teks_biasa
    words = function_tokenization(data)

    type = function_type(words)
    list_stopwords = function_get_stopwords(words)
    return type, list_stopwords


def function_split_teks(paragraf):
    # data = paragraf
    paragraph = []
    data = paragraf.split('\n')

    if '' in data:
        data.remove('')

    all_kalimat = ''
    jml_para = len(data)
    # Untuk mengelompokkan kalimat dalam satu paragraf
    for x in range(0, jml_para):
        if '! ' in data[x]:
            data[x] = data[x].replace('! ', '. ')
        elif '? ' in data[x]:
            data[x] = data[x].replace('? ', '. ')

        if all_kalimat == '':
            all_kalimat = data[x]
        else:
            all_kalimat = all_kalimat+' '+data[x]

    if '. ' in all_kalimat:
        paragraph = all_kalimat.split('. ')

    if '' in paragraph:
        paragraph.remove('')

    for y in range(0, len(paragraph)):
        if '.' in paragraph[y]:
            paragraph[y] = paragraph[y].replace('.', '')
    # ============================================================
    # print(paragraph)

    type_per_kalimat = []
    for x in paragraph:
        words = function_tokenization(x)
        type_per_kalimat.append(function_type(words))
    return (type_per_kalimat, paragraph)


def get_matrix(type_per_kalimat, paragraph):
    counter = 0
    # print(paragraph)
    for x in paragraph:
        if counter == 0:
            kalimat = x
            counter += 1
        else:
            kalimat = kalimat + '. ' + x

    type, list_stopwords = function_cari_term(kalimat)
    words = type_per_kalimat

    tf_all = []
    for x in words:
        type_paragraph = []
        for a_type in type:
            count = 0
            for word in x:
                if a_type == word:
                    count = count + 1
                    # Frequency tiap term dicatat setelah looping ketiga berhenti
                    # Looping ketiga adalah looping untuk membandingkan term dengan setiap kata pada kalimat
            type_paragraph.append(count)
        tf_all.append(type_paragraph)
    x = tf_all
    sentences = words
    t = type

    return x, sentences, t, list_stopwords


def check_df(temp, jml_kal, jml_t):
    df = []
    for i in range(0, jml_t):
        count = 0
        for j in range(0, jml_kal):
           if temp[i][j] > 0:
               count = count+1
        df.append(count)

    return df


def bobot_kalimat(x, jml_t, jml_kal):
    temp = list(map(list, zip(*x)))
    df = check_df(temp, jml_kal, jml_t)
    bobot = []
    for i in range(0, jml_kal):
        hasil2 = 0
        for j in range(0, jml_t):
            hasil = temp[j][i] * math.log10(jml_kal/df[j])
            hasil2 = hasil2+hasil
        bobot.append(hasil2)

    return bobot


