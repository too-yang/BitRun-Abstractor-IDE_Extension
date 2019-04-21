from sklearn.feature_extraction.text import CountVectorizer

texts=["dog cat fish","dog cat cat","fish bird", 'bird'] # “dog cat fish” 为输入列表元素,即代表一个文章的字符串
cv = CountVectorizer()#创建词袋数据结构
cv_fit=cv.fit_transform(texts)
#上述代码等价于下面两行
#cv.fit(texts)
#cv_fit=cv.transform(texts)

print(cv.get_feature_names())    #['bird', 'cat', 'dog', 'fish'] 列表形式呈现文章生成的词典

print(cv.vocabulary_	)              # {‘dog’:2,'cat':1,'fish':3,'bird':0} 字典形式呈现，key：词，value:词频

print(cv_fit)
# （0,3） 1   第0个列表元素，**词典中索引为3的元素**， 词频
#（0,1）1
#（0,2）1
#（1,1）2
#（1,2）1
#（2,0）1
#（2,3）1
#（3,0）1

