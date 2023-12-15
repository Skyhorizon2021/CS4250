from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
#html = urlopen("http://www.pythonscraping.com/pages/page1.html")
bs = BeautifulSoup('''<html>
<head>
<title>My first web page</title>
</head>
<body>
<h1>My first web page</h1>
<h2>What this is tutorial</h2>
<p>A simple page put together using HTML. <em>I said a simple page.</em>.</p>
<ul>
 <li>To learn HTML</li>
 <li>
 To show off
 <ol>
 <li>To my boss</li>
 <li>To my friends</li>
 <li>To my cat</li>
 <li>To the little talking duck in my brain</li>
 </ol>
 </li>
 <li>Because I have fallen in love with my computer and want to give her some HTML loving.</li>
</ul>
<h2>Where to find the tutorial</h2>
<p><a href="http://www.aaa.com"><img src=http://www.aaa.com/badge1.gif></a></p>
<h3>Some random table</h3>
<table>
 <tr class="tutorial1">
 <td>Row 1, cell 1</td>
 <td>Row 1, cell 2<img src=http://www.bbb.com/badge2.gif></td>
 <td>Row 1, cell 3</td>
 </tr>
 <tr class="tutorial2">
 <td>Row 2, cell 1</td>
 <td>Row 2, cell 2</td>
 <td>Row 2, cell 3<img src=http://www.ccc.com/badge3.gif></td>
 </tr>
</table>
</body>
</html>''','html.parser')
print(bs.title.get_text())
for text in bs.find_all('h2',string=re.compile("tutorial")):
    print(text.get_text())
print(bs.find('tr',{'class':'tutorial2'}).get_text())
#print(bs.find('tr',{'class':"tutorial"}).get_text())
# for text in bs.find_all('',string=re.compile("HTML")):
#     print(text.get_text())
#print(bs.find('tr',{'class':'tutorial1'}).get_text())
for image in bs.find('table').find_all('img'):
    print(image['src'])
