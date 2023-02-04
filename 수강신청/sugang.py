import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
}
user = {
    "j_id": "2019150022",  # id
    "j_password": "3241132",  # pw
    "NETFUNNEL_KEY": "undefined"
}

data1 = {
    "STUNO" : "2019150022",
    "TYPE" : "2",
    "TLSN_THTM_HY_SH_JA" : "3",
    "DAYNGT_GBN_SH_JA" : "1",
    "SC_CD" : "AAK10050",
    "LT_NO" : "03",
    "NETFUNNEL_KEY" : "undefined"
}#노동인권과법

data2 = {
    "STUNO" : "2019150022",
    "TYPE" : "2",
    "TLSN_THTM_HY_SH_JA" : "3",
    "DAYNGT_GBN_SH_JA" : "1",
    "SC_CD" : "ACS20021",
    "LT_NO" : "05",
    "NETFUNNEL_KEY" : "undefined"
}#운영체제

data3 = {
    "STUNO" : "2019150022",
    "TYPE" : "2",
    "TLSN_THTM_HY_SH_JA" : "3",
    "DAYNGT_GBN_SH_JA" : "1",
    "SC_CD" : "ACS33010",
    "LT_NO" : "01",
    "NETFUNNEL_KEY" : "undefined"
}#소프트웨어공학

data4 = {
    "STUNO" : "2019150022",
    "TYPE" : "2",
    "TLSN_THTM_HY_SH_JA" : "3",
    "DAYNGT_GBN_SH_JA" : "1",
    "SC_CD" : "ACS34013",
    "LT_NO" : "02",
    "NETFUNNEL_KEY" : "undefined"
}#마이크로프로세서응용

data5 = {
    "STUNO" : "2019150022",
    "TYPE" : "2",
    "TLSN_THTM_HY_SH_JA" : "3",
    "DAYNGT_GBN_SH_JA" : "1",
    "SC_CD" : "ACS35030",
    "LT_NO" : "01",
    "NETFUNNEL_KEY" : "undefined"
}#네트워크프로그래밍

data6 = {
    "STUNO" : "2019150022",
    "TYPE" : "2",
    "TLSN_THTM_HY_SH_JA" : "2",
    "DAYNGT_GBN_SH_JA" : "1",
    "SC_CD" : "ACS40012",
    "LT_NO" : "02",
    "NETFUNNEL_KEY" : "undefined"
}#인공지능
#
# data7 = {
#     "STUNO" : "2018150001",
#     "TYPE" : "2",
#     "TLSN_THTM_HY_SH_JA" : "2",
#     "DAYNGT_GBN_SH_JA" : "1",
#     "SC_CD" : "ACS34032",
#     "LT_NO" : "02",
#     "NETFUNNEL_KEY" : "undefined"
# }#디지털영상처리


with requests.Session() as s:
    print("아무키나 누르기")
    input()
    s.post("http://sugang.tukorea.ac.kr/SsoCtr/login.do", data=user)
    s.get("http://sugang.tukorea.ac.kr/ApplyCtr/findSugangCncl.do")
    s.post("http://sugang.tukorea.ac.kr/MajorCtr/proc.do", headers=headers, data=data1)
    s.post("http://sugang.tukorea.ac.kr/MajorCtr/proc.do", headers=headers, data=data2)
    s.post("http://sugang.tukorea.ac.kr/MajorCtr/proc.do", headers=headers, data=data3)
    s.post("http://sugang.tukorea.ac.kr/MajorCtr/proc.do", headers=headers, data=data4)
    s.post("http://sugang.tukorea.ac.kr/MajorCtr/proc.do", headers=headers, data=data5)
    r = s.post("http://sugang.tukorea.ac.kr/MajorCtr/proc.do", headers=headers, data=data6)
    # s.post("http://sugang.tukorea.ac.kr/MajorCtr/proc.do", headers=headers, data=data6)
    # r = s.post("http://sugang.tukorea.ac.kr/MajorCtr/proc.do", headers=headers, data=data7)

    print(r.text)