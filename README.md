# icuText2Anki
A simple code to import Q&amp;A notes into  Anki by Add-on

需要导入Anki的Q&A笔记文件，存在
/Users/ad/Downloads/Anki_ICU_Book.txt
或者自己把笔记文件在这里改成需要的位置和名字.

直接把Anki Add-on文件中 icu-Importer.py 直接丢到Anki的add-on目录，
重启Anki，tools菜单里会有一个 icuImpoter，
点下就可以自动把设置的Q&A笔记整理成Anki能导入的csv格式，并自动导入到Anki的 Test Deck中.
可以设置一下自己的inbox duck，替换掉我在代码里写的是 test
重复卡片的问题，Anki自己会做处理，重复的不导入，所以先在一个测试用的deck里试试看吧，以后没问题再往正式的deck里自动填.
可以设置一下代码中自己笔记的位置.
支持的格式为：
问题——
Q： xxxxxx
问题只支持一行的格式。

答案——
A：xxxxx
答案支持回车与换行、多行内容。
