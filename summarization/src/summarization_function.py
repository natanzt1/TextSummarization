from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import math

ps = PorterStemmer()

def function_split_teks_tanpa_type_no_lowercase(paragraf):
    # data = paragraf
    paragraph = []
    data = paragraf.split('\n')
    if '' in data:
        data.remove('')
    jml_para = len(data)

    for x in range(0, jml_para):
        if '! ' in data[x]:
            data[x] = data[x].replace('! ', '. ')
        elif '? ' in data[x]:
            data[x] = data[x].replace('? ', '. ')
        if '. ' in data[x]:
            paragraph.append(data[x].split('. '))

    for x in range(0, len(paragraph)):
        for y in range(0, len(paragraph[x])):
            if '.' in paragraph[x][y]:
                paragraph[x][y]=paragraph[x][y].replace('.', '')

    stopWords = stopwords.words('english')
    all_split_kalimat = []
    for x in paragraph:
        split_kalimat = []
        for y in x:
            words = function_tokenization_no_lowercase(y)
            words2 = []
            for x in words:
                if x not in stopWords:
                    words2.append(x)
            split_kalimat.append(words2)
        all_split_kalimat.append(split_kalimat)

    return all_split_kalimat


def function_tokenization_no_lowercase(data):
    special_char = ['!','@', '?', '-', '.', ',', '"', ';', '—', "'", '"', '“', '’', '”']
    remove_character = data
    for char in special_char:
        while char in remove_character:
            remove_character = remove_character.replace(char, "")
    remove_split_line = ' '.join(remove_character.splitlines())
    remove_dbl_space = remove_split_line.replace('  ', ' ')
    lowercase = remove_dbl_space
    words = lowercase.split(' ')
    if '' in words:
        words.remove('')
    return words

def function_tokenization(data):
    special_char = ["’s",'!','@', '?', '-', '.', ',', '"', ';', '—', "'", '"', '“', '’', '”']
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
        words[x] = ps.stem(words[x])
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
    stopWords = stopwords.words('english')
    for w in token:
        if w not in stopWords:
            type.append(w)
            # type2.append(w)
    return type


def function_type_freq(type, words):
    k = 0
    type_freq = []
    count_type = len(type)
    for k in range(count_type):
        type_freq.append(0)

    i = 0
    for a_type in type:
        for word in words:
            if a_type == word:
                type_freq[i] += 1
        i += 1

    return type_freq

def function_cari_term(teks_biasa):
    data = teks_biasa
    words = function_tokenization(data)
    ps = PorterStemmer()

    type = function_type(words)
    return (type, words)


def function_split_teks_tanpa_type(paragraf):
    # data = paragraf
    paragraph = []
    data = paragraf.split('\n')
    if '' in data:
        data.remove('')
    jml_para = len(data)

    for x in range(0, jml_para):
        if '! ' in data[x]:
            data[x] = data[x].replace('! ', '. ')
        elif '? ' in data[x]:
            data[x] = data[x].replace('? ', '. ')
        if '. ' in data[x]:
            paragraph.append(data[x].split('. '))

    for x in range(0, len(paragraph)):
        for y in range(0, len(paragraph[x])):
            if '.' in paragraph[x][y]:
                paragraph[x][y]=paragraph[x][y].replace('.', '')

    stopWords = stopwords.words('english')
    all_split_kalimat = []
    for x in paragraph:
        split_kalimat = []
        for y in x:
            words = function_tokenization(y)
            words2 = []
            for x in words:
                if x not in stopWords:
                    words2.append(x)
            split_kalimat.append(words2)
        all_split_kalimat.append(split_kalimat)

    return all_split_kalimat


def function_split_teks(paragraf):
    # data = paragraf
    paragraph = []
    data = paragraf.split('\n')
    if '' in data:
        data.remove('')
    jml_para = len(data)

    for x in range(0, jml_para):
        if '! ' in data[x]:
            data[x] = data[x].replace('! ', '. ')
        elif '? ' in data[x]:
            data[x] = data[x].replace('? ', '. ')
        if '. ' in data[x]:
            paragraph.append(data[x].split('. '))

    for x in range(0, len(paragraph)):
        for y in range(0, len(paragraph[x])):
            if '.' in paragraph[x][y]:
                paragraph[x][y]=paragraph[x][y].replace('.', '')

    all_split_kalimat = []
    for x in paragraph:
        split_kalimat = []
        for y in x:
            words = function_tokenization(y)
            split_kalimat.append(function_type(words))
        all_split_kalimat.append(split_kalimat)

    return (all_split_kalimat, paragraph)


def function_kalimat_terpanjang(all_split_kalimat):
    panjang_kalimat = []

    for x in all_split_kalimat:
        for y in x:
            panjang_kalimat.append(len(y))

    for y in range(1, len(panjang_kalimat)):
        if panjang_kalimat[0] < panjang_kalimat[y]:
            sample = panjang_kalimat[0]
            panjang_kalimat[0] = panjang_kalimat[y]
            panjang_kalimat[y] = sample

    kalimat_terpanjang = panjang_kalimat[0]
    return kalimat_terpanjang


def function_kemiripan_judul(kalimat, judul):
    words_kalimat = function_tokenization(kalimat)
    words_judul = function_tokenization(judul)
    type_kalimat = function_type(words_kalimat)
    type_judul = function_type(words_judul)
    kesamaan = 0
    for x in range(0, len(type_kalimat)):
        kata1 = type_kalimat[x]
        for y in range(0, len(type_judul)):
            kata2 = type_judul[y]
            if kata1 == kata2:
                kesamaan += 1
                y = len(type_judul)
    fitur1 = kesamaan/len(type_judul)
    return fitur1

# Fitur Pertama = Kemiripan Judul
def function_fitur1(judul, paragraph):
    all_kemiripan = []
    for x in range(0, len(paragraph)):
        kemiripan = []
        for y in range(0, len(paragraph[x])):
            kalimat = paragraph[x][y]
            fitur = function_kemiripan_judul(kalimat, judul)
            kemiripan.append(fitur)
        all_kemiripan.append(kemiripan)

    return all_kemiripan

# Fitur Kedua = Panjang Kalimat
def function_fitur2(kalimat_terpanjang, paragraph):
    all_panjang_kalimat = []
    for x in range(0, len(paragraph)):
        panjang_kalimat = []
        for y in range(0, len(paragraph[x])):
            pjg_kalimat = len(paragraph[x][y])
            fitur2 = pjg_kalimat/kalimat_terpanjang
            panjang_kalimat.append(fitur2)
        all_panjang_kalimat.append(panjang_kalimat)

    return all_panjang_kalimat


def function_fitur3(paragraph):
    all_posisi = []
    for x in range(0, len(paragraph)):
        posisi = []
        total_kalimat = len(paragraph[x])
        for y in range(0, total_kalimat):
            if y == 0 or y == total_kalimat-1:
                posisi.append(1)
            elif y == 1 or y == total_kalimat-2:
                posisi.append(0.8)
            elif y == 2:
                posisi.append(0.6)
            elif y == total_kalimat-3:
                posisi.append(0.4)
            elif y == 3:
                posisi.append(0.2)
            else:
                posisi.append(0)
        all_posisi.append(posisi)
    return all_posisi


def function_fitur4(paragraph):
    counter = 0
    for x in paragraph:
        for y in x:
            if counter == 0:
                kalimat = y
                counter += 1
            else:
                kalimat = kalimat + '. ' + y
    result = function_cari_term(kalimat)
    # print(result)
    type = result[0]

    words = function_split_teks_tanpa_type(kalimat)
    words = words[0]
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

    df_all = []
    bobot = []
    bobot_all = []
    N = len(words)

    for a_type in type:
        df_count = 0
        for x in words:
            if a_type in x:
                df_count = df_count + 1
        df_all.append(df_count)

    for counter in range(0, len(words)):
        tf_idf_kalimat = 0
        for counter2 in range(0, len(type)):
            df = df_all[counter]

            tf_idf = tf_all[counter][counter2] * math.log10(N / df)
            tf_idf_kalimat = tf_idf_kalimat + tf_idf
        # print("TF IDF")
        # print(tf_idf_kalimat)
        bobot.append(tf_idf_kalimat)

        bobot_terbesar = bobot[0]
    for y in range(1, len(bobot)):
        if bobot_terbesar < bobot[y]:
            bobot_terbesar = bobot[y]

    counter = 0
    for x in paragraph:
        temp = []
        for y in x:
            real_bobot = bobot[counter]/bobot_terbesar
            temp.append(real_bobot)
            counter += 1
        bobot_all.append(temp)
    return bobot_all


def function_fitur5(meta):
    paragraph = function_split_teks_tanpa_type_no_lowercase(meta)
    all_kapital = []
    for x in range(0, len(paragraph)):
        kapital = []
        for y in range(0, len(paragraph[x])):
            jumlah_kata = len(paragraph[x][y])

            jumlah = 0
            for z in range(1, jumlah_kata):
                word = paragraph[x][y][z]
                if word[0].isupper():
                    jumlah += 1
            if jumlah > 0:
                fitur = jumlah/(jumlah_kata-1)
                kapital.append(fitur)
            else:
                fitur = 0
                kapital.append(fitur)
        all_kapital.append(kapital)
    return all_kapital


def function_fitur6(meta):
    paragraph = function_split_teks_tanpa_type(meta)
    all_number = []
    for x in range(0, len(paragraph)):
        kapital = []
        for y in range(0, len(paragraph[x])):
            jumlah_kata = len(paragraph[x][y])
            jumlah = 0
            for z in range(0, jumlah_kata):
                word = paragraph[x][y][z]
                for char in range(0, len(word)):
                    if word[char].isdigit():
                        jumlah +=1
                        break

            if jumlah > 0:
                fitur = jumlah/(jumlah_kata)
                kapital.append(fitur)
            else:
                fitur = 0
                kapital.append(fitur)
        all_number.append(kapital)
        # print(all_number)
    return all_number


def function_fuzzy(fitur):
    sangat_rendah_min = 0
    sangat_rendah_max = 0.225
    rendah_min = 0.1
    rendah_max = 0.45
    sedang_min = 0.325
    sedang_max = 0.675
    tinggi_min = 0.55
    tinggi_max = 0.9
    sangat_tinggi_min = 0.775
    sangat_tinggi_max = 1

    output_tidak_penting_min = 0
    output_tidak_penting_max = 0.4
    output_sedang_min = 0.1
    output_sedang_max = 0.9
    output_penting_min = 0.6
    output_penting_max = 1


    # Sangat Tinggi = 5
    # Tinggi = 4
    # Sedang = 3
    # Rendah = 2
    # sangat Rendah = 1
    fuzzy_all = []
    for x in fitur:
        fuzzy = []
        for y in x:
            if y > tinggi_max:
                result = 5

            elif y >= sangat_tinggi_min:
                result1 = (tinggi_max-y)/(tinggi_max-sangat_tinggi_min)
                result2 = (y-sangat_tinggi_min)/(tinggi_max-sangat_tinggi_min)
                if result1 < result2:
                    result = 4
                else:
                    result = 5

            elif y > sedang_max:
                result = 4

            elif y >= tinggi_min:
                result1 = (sedang_max - y) / (sedang_max - tinggi_min)
                result2 = (y - tinggi_min) / (sedang_max - tinggi_min)
                if result1 < result2:
                    result = 3
                else:
                    result = 4

            elif y > rendah_max:
                result = 3

            elif y >= sedang_min:
                result1 = (rendah_max - y) / (rendah_max - sedang_min)
                result2 = (y - sedang_min) / (rendah_max - sedang_min)
                if result1 < result2:
                    result = 2
                else:
                    result = 3

            elif y > sangat_rendah_max:
                result = 2

            elif y >= rendah_min:
                result1 = (sangat_rendah_max - y) / (sangat_rendah_max - rendah_min)
                result2 = (y - rendah_min) / (sangat_rendah_max - rendah_min)
                if result1 < result2:
                    result = 1
                else:
                    result = 2

            elif y < rendah_min:
                result = 1

            fuzzy.append(result)
        fuzzy_all.append(fuzzy)
    return(fuzzy_all)


def function_rule1(result1, result2, result3, result4, result5, result6):
    if result1 >= 3 and result2 >= 2 and result3 >= 3 and result4 >= 3 or result5 >= 3 or result6 >= 3:
        return "penting"
    elif result1 >= 3 and result2 >= 3 and result3 >= 2 and result4 >= 2 and result5 >= 1 and result6 >= 1:
        return "sedang"
    else:
        return "tidak penting"


def function_fuzzy_output(result1, result2, result3, result4, result5, result6):
    fuzzy_output_all = []
    for x in range(0, len(result1)):
        fuzzy_output = []
        for y in range(0, len(result1[x])):
            hasil = function_rule1(result1[x][y], result2[x][y], result3[x][y], result4[x][y], result5[x][y], result6[x][y])
            fuzzy_output.append(hasil)
        fuzzy_output_all.append(fuzzy_output)
    return fuzzy_output_all



def function_rule_fuzzy(result1, result2, result3, result4, result5, result6):
    # IF Kesamaan Judul = Sangat Tinggi AND Panjang
    # Kalimat = Sedang AND Posisi Kalimat = Sangat Tinggi
    # AND Bobot Kata = Sedang AND Huruf Besar =
    # Sangat Rendah AND Data Numerik = Sangat Rendah
    # THEN Kalimat = Penting
    index1 = []
    index2 = []
    for x in range(0, len(result1)):
        for y in range(0, len(result1[x])):
            hasil = function_rule1(result1[x][y], result2[x][y], result3[x][y], result4[x][y], result5[x][y], result6[x][y])
            if hasil == "penting":
                index1.append(x)
                index2.append(y)
                hasil = "skip"

    return (index1, index2)

def function_convert(value):
    if value == 1:
        predikat = "Sangat Rendah"
    elif value == 2:
        predikat = "Rendah"
    elif value == 3:
        predikat = "Sedang"
    elif value == 4:
        predikat = "Tinggi"
    elif value == 5:
        predikat = "Sangat Tinggi"
    return predikat

# # JUDUL
# filename = "tf_idf.txt"
# judul = "rabbit and turtle"
#
# with open(filename, 'r') as myfile:
#     meta = myfile.read()
#
# all_split_kalimat = function_split_teks(meta)
# paragraph = all_split_kalimat[1]
# all_split_kalimat = all_split_kalimat[0]
# #
# kalimat_terpanjang = function_kalimat_terpanjang(all_split_kalimat)
#
#
# fitur1 = function_fitur1(judul, paragraph)
# # print (fitur1)
# result1 = function_fuzzy(fitur1)
#
# fitur2 = function_fitur2(kalimat_terpanjang, all_split_kalimat)
# # print (fitur2)
# result2 = function_fuzzy(fitur2)
#
# fitur3 = function_fitur3(paragraph)
# # print(fitur3)
# result3 = function_fuzzy(fitur3)
#
# fitur4 = function_fitur4(paragraph)
# # print(fitur4)
# result4 = function_fuzzy(fitur4)
#
# fitur5 = function_fitur5(meta)
# # print(fitur5)
# result5 = function_fuzzy(fitur5)
#
# fitur6 = function_fitur6(meta)
# print(fitur6)
# result6 = function_fuzzy(fitur6)
#
# result = function_rule_fuzzy(result1, result2, result3, result4, result5, result6)
# index1 = result[0]
# index2 = result[1]
#
# for x in range(0, len(index1)):
#     a = index1[x]
#     b = index2[x]
#     print(paragraph[a][b])
