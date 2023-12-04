text = "Я помню чудное мгновенье:\n\
Передо мной явилась ты,\n\
Как мимолетное виденье,\n\
Как гений чистой красоты.\n\
\n\
В томленьях грусти безнадежной,\n\
В тревогах шумной суеты,\n\
Звучал мне долго голос нежный\n\
И снились милые черты.\n\
\n\
Шли годы. Бурь порыв мятежный\n\
Рассеял прежние мечты,\n\
И я забыл твой голос нежный,\n\
Твои небесные черты.\n\
\n\
В глуши, во мраке заточенья\n\
Тянулись тихо дни мои\n\
Без божества, без вдохновенья,\n\
Без слез, без жизни, без любви.\n\
\n\
Душе настало пробужденье:\n\
И вот опять явилась ты,\n\
Как мимолетное виденье,\n\
Как гений чистой красоты.\n\
\n\
И сердце бьется в упоенье,\n\
И для него воскресли вновь\n\
И божество, и вдохновенье,\n\
И жизнь, и слезы, и любовь."

print(text)
print("*"*50)

PUNCT = ('?', '!', ':', ';', '-', '—', '()', '[]', '— ', '.', '’', '“ ”', '/', ',', "  ", "   ", "    ")

def changed_text(text):
    for t in PUNCT:
        text = text.lower()
        text = text.replace(t, " ")         
        text = " ".join(text.split())                                             
    return text
#print(changed_text(text))
w= changed_text(text)
def split_text(w,s= " "):
    w = w.split(s)
    return w, len(w)
#print(split_text(w,s= " "))

text_result = changed_text(text)
text,n = split_text(text_result)

uniq_words = set (text)
text_sorted = list(uniq_words)
text_sorted.sort()

word_list = dict()
for word in text_sorted:
    word_list[word] = text.count(word)

print(word_list)
