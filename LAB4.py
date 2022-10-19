#1-Мысал . startswith() - егер жол берілген мәннен басталса, True мәнін қайтарады; әйтпесе - False
text= 'Aiman is a student of Satbayev University'
print(text.startswith("Aiman")) #True
print(text.startswith("is",7,20)) #False


#2-Мысал. swapcase() методы - бас әріппен жазылғанды кішіге,ал кішіні үлкенге айналдырады
text = 'AimaN is a STUDENT oF SatbAyev UNIVERsity'
print(text.swapcase()) # aIMAn IS A student Of sATBaYEV univerSITY


#3-Мысал . zfill() методы - жолдың басына нөлдерді (0) қосады
text = 'Python'
print(text.zfill(10)) # 0000Python


#4-Мысал . center() методы -  жолды центрге туралайды. Ол белгілі бір таңбаға байланысты орындалады
text = 'Aiman'#Айман деген строка берілсін
print(text.center(9, ''))# **Aiman* деп центрге выравнивать етіп береді


#5-Мысал . find() методы строканың индексі бойынша іздейді
text = 'Она продает ракушки на берегу моря. Товары, которые она продает, безусловно, ракушки.'
print(text.find('ракушки',0,9)) # -1 қайтарады,себебі 0 мен 9 индекстері арасында табылмады


#6- Мысал . format() методы - жолдарды форматитровать етеді
text = 'Aiman is {} year student of Satbayev University'
print(text.format(4)) # Aiman is 4 year student of Satbayev University


#7 - Мысал . replace() методы жолдардың мәнін өзгертеді
text = 'Aiman is a  student of Kazakh National Technical University'
print(text.replace("Kazakh National Technical", "Satbayev")) #Aiman is a  student of Satbayev University


#8-Мысал . list() - жолды жеке таңбаларға бөледі
text = 'Aiman is a  student of Kazakh National Technical University'
print(list(text))

#9-Мысал . count() - берілген жолдың берілген жолда қанша рет кездесетінін анықтайды
text1 = "Aiman is a student"
text2 = "is"
count = text1.count(text2) # 1-ші текстта 2ші тексттің қанша рет кездесетінін есептейді
print(count) #1

#10- Мысал . join() - берілген жолдағы символдар арасында берілген таңбаны қосады
word = "hello"
joined_word = "|".join(word)
print(joined_word) # h|e|l|l|o

#Қосымша есептер
text = str(input()) #Текст енгіземіз
upper = 0 #Үлкен әріптің счетчигі
lower = 0 #Кіші әріптің счетчигі
for i in text: #Тексттегі сиволдардың индексіне цикл ашамыз
    if i.isupper(): # Егер үлкен әріп болса
        upper += 1 #Үлкн әріптің счетына +1
    else:#Кіші әріп көп болса
        lower += 1#Кіші әріптің счетына +1
if upper > lower:#Егер үлкен әріп көбірек болса
    print(text.upper())#Экранға тексттің барлық символын үлкен әріппен шығарамыз
else:#Егер кіші әріп көп болса
    print(text.lower())#Экранға кіші әріппен шығарамыз


while True:#Тру болғанша
    num1 = input() #1ші мжолды енгіземіз
    num2 = input() #2ші жолды енгіземіз
    if num1.isdigit() and num2.isdigit(): #Егер 1 мен 2ші жол саннан тұрса
        print(int(num1) + int(num2))#Екеуін қосып экранға шығарамвз
        break #Программа тоқтайды


sentence = 'Алматы керемет қала. Мен Алматыны сүйемін. Алматыда алма көп өседі.'
p = 'Алма'
print(sentence.count(p)) #3
print(sentence.count(p,0,25)) #1
print(sentence.count(p.lower())) #1
print(sentence.lower().count(p.lower())) #4


sentence = 'Алматы керемет қала. Мен Алматыны сүйемін. Алматыда алма көп өседі.'
p = 'Алма'
print(sentence.find(p)) #0
print(sentence.find(p,0,25)) #0
print(sentence.find(p.lower())) #52
print(sentence.lower().find(p.lower())) #0

str = " h3110 23 cat 444.4 rabbit 11 2 dog"
print(str.strip()) #h3110 23 cat 444.4 rabbit 11 2 dog
print(str.replace(' ', '')) #h311023cat444.4rabbit112dog


s1 = input("s1 = ") # s1 строканы енгіземіз
s2 = input("s2 = ") #s2 строканы енгіземіз
if s1>s2: # Егер s1 үлкен болса s2-ден
  print("s1 > s2") # Экранға шығарамыз
elif s1==s2:# Егер s1 мен s2 тең болса
  print("s1 == s2")#Экранға шығарамыз
else:# Жоғарыдағы 2 шарт орындалмаса
  print("s1 < s2") #Экранға шығарамыз