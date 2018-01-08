import requests
import lxml.html
import logindata
import time

sess = requests.Session()
sess.get("http://bkjw2.guet.edu.cn")

formtype = {'Content-Type': 'application/x-www-form-urlencoded'}

sess.post("http://bkjw2.guet.edu.cn/student/public/login.asp", data=logindata.login, headers=formtype)

sess.get("http://bkjw2.guet.edu.cn/student/Selectinfo.asp")
sess.get("http://bkjw2.guet.edu.cn/student/select.asp")
re = sess.post("http://bkjw2.guet.edu.cn/student/select.asp", data=logindata.seltype, headers=formtype)
re.encoding="gbk"
p = lxml.html.fromstring(re.text)

for l in p.xpath("//tr"):
    try:
        idx = l.xpath("td/input/@value")[0]
    except IndexError:
        continue
    for e in l.xpath("td"):
        text = e.text
        if not text or not text.strip():
            try:
                text = e.xpath("a/text()")[0]
            except IndexError:
                text = "IndexError"
        if text and text.strip() == "1":
            reqdat = logindata.seldat.replace("1722245", idx)
            sess.post("http://bkjw2.guet.edu.cn/student/select.asp", data=reqdat, headers=formtype)
            time.sleep(10);
        print text,
    print() 
