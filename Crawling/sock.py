import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
google_ip = socket.gethostbyname("google.com")
sock.connect((google_ip, 80))

sock.send("GET / HTTP/1.1\n".encode())
sock.send("\n".encode())

buffer = sock.recv(4096)
buffer = buffer.decode().replace("\r\n", "\n")
sock.close()

print(buffer)

'''
HTTP/1.1 200 OK
Date: Fri, 03 Apr 2020 06:20:15 GMT
Expires: -1
Cache-Control: private, max-age=0
Content-Type: text/html; charset=ISO-8859-1
P3P: CP="This is not a P3P policy! See g.co/p3phelp for more info."
Server: gws
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN
Set-Cookie: 1P_JAR=2020-04-03-06; expires=Sun, 03-May-2020 06:20:15 GMT; path=/; domain=.google.com; Secure
Set-Cookie: NID=201=pi3e8HAsecVXVT7b2p-vyBjPJNH1OiTXM4uzRYhyxvC0P7R_ukiI7sfnFNNHWG72sO9zqtEcezt6irMXoLrfvnhd3uQEKssJ41M2oSi1rslYGCOUJW1_cmJUE1pA-M3_HqQ8KdhS7Bhbx9KiaQpjyGzBL_n0UcrQngdjDfIc1B4; expires=Sat, 03-Oct-2020 06:20:15 GMT; path=/; domain=.google.com; HttpOnly
Accept-Ranges: none
Vary: Accept-Encoding
Transfer-Encoding: chunked

6363
<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="ko"><head><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"><title>Google</title><script nonce="00KEEg5xWGvGVo1fWikISw==">(function(){window.google={kEI:'n9WGXunuBJTWmAXGw6_QBQ',kEXPI:'0,202123,3,1151621,5662,731,223,5104,207,3204,10,290,761,175,364,542,893,4,60,703,114,383,139,107,5,960,38,19,337,728,41,43,104,5,12,433,50,1126350,1197755,136,133,125,329118,1294,12383,4855,32691,15248,867,28684,369,8819,8384,4858,1362,283,9007,3025,7861,7915,1808,4020,978,7626,305,5297,2054,920,873,1217,1710,1,1264,6434,11302,2883,21,317,4517,2778,520,399,2277,8,2796,889,704,1279,2212,202,328,149,1103,840,517,1474,48,157,663,3438,312,1137,2,2063,606,1839,184,1777,520,1947,747,1482,93,330,1282,16,2927,2247,473,1339,748,1039,3227,773,2072,7,7633,6513,2662,642,632,1817,2459,1226,1462,3935,1274,108,3407,908,2,940,553,420,1642,2132,265,808,4611,225,996,1670,190,290,606,1349,3,346,200,30,156,814,183,388,173,121,373,1639,1906,440,267,148,189,3312,909,320,814,47,399,28,201,247,911,591,274,121,1677,193,415,192,1344,47,83,1661,4,1528,17,304,112,208,300,70,4,280,1009,152,183,482,209,166,44,644,225,276,327,68,2,10,39,64,1065,5,413,272,1259,498,718,124,329,565,118,88,143,4,208,130,52,74,4,7,57,177,583,50,264,108,5830265,1805894,4194806,2801216,549,333,444,1,2,80,1,900,896,1,8,1,2,2551,1,748,141,59,736,563,1,4265,1,1,1,1,137,1,1193,722,450,1,216,6,6,3,3,1,1,2,3,1,1,1,1,1,1,1,9,1,1,2,2,2,3,1,3,11,6,1,5,3,5,6,1,2,23962918,25',kBL:'Ukmn'};google.sn='webhp';google.kHL='ko';})();(function(){google.lc=[];google.li=0;google.getEI=function(a){for(var c;a&&(!a.getAttribute||!(c=a.getAttribute("eid")));)a=a.parentNode;return c||google.kEI};google.getLEI=function(a){for(var c=null;a&&(!a.getAttribute||!(c=a.getAttribute("leid")));)a=a.parentNode;return c};google.ml=function(){return null};google.time=function(){return Date.now()};google.log=function(a,c,b,d,g){if(b=google.logUrl(a,c,b,d,g)){a=new Image;var e=google.lc,f=google.li;e[f]=a;a.onerror=a.onload=a.onabort=function(){delete e[f]};google.vel&&google.vel.lu&&google.vel.lu(b);a.src=b;google.li=f+1}};google.logUrl=function(a,c,b,d,g){var e="",f=google.ls||"";b||-1!=c.search("&ei=")||(e="&ei="+google.getEI(d),-1==c.search("&lei=")&&(d=google.getLEI(d))&&(e+="&lei="+d));d="";!b&&google.cshid&&-1==c.search("&cshid=")&&"slh"!=a&&(d="&cshid="+google.cshid);b=b||"/"+(g||"gen_204")+"?atyp=i&ct="+a+"&cad="+c+e+f+"&zx="+google.time()+d;/^http:/i.test(b)&&"https:"==window.location.protocol&&(google.ml(Error("a"),!1,{src:b,glmm:1}),b="");return b};}).call(this);(function(){google.y={};google.x=function(a,b){if(a)var c=a.id;else{do c=Math.random();while(google.y[c])}google.y[c]=[a,b];return!1};google.lm=[];google.plm=function(a){google.lm.push.apply(google.lm,a)};google.lq=[];google.load=function(a,b,c){google.lq.push([[a],b,c])};google.loadAll=function(a,b){google.lq.push([a,b])};}).call(this);google.f={};(function(){
document.documentElement.addEventListener("submit",function(b){var a;if(a=b.target){var c=a.getAttribute("data-submitfalse");a="1"==c||"q"==c&&!a.elements.q.value?!0:!1}else a=!1;a&&(b.preventDefault(),b.stopPropagation())},!0);document.documentElement.addEventListener("click",function(b){var a;a
'''
