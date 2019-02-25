# Get basic info of users

These information includes 8 fields(besides userID):

* general information: includes user's location, generation, constellation, sex
* jion time
* play count
* level
* visit: number of visitor
* follow
* fans
* feed: number of user's share

## info_user.txt

585, 801 users' ID

## 切割与合并.py

splits info_user.txt into 24 files

combines the results into one file

## Xinfo_user

Program used to get the data

## Issues

### lack of fields

Some users lack of location info

![缺第一个字段的：13000989](https://github.com/Vida42/XiamiMusicAnalysis/blob/master/01_data_prep/06_users_info/issues/lackof1stfield.png)
 
Some users lack of generation info

![缺第二个字段的：11286938](https://github.com/Vida42/XiamiMusicAnalysis/blob/master/01_data_prep/06_users_info/issues/lackof2ndfield.png)
 
Some users lack of constellation info

![缺第三个字段的：42653808](https://github.com/Vida42/XiamiMusicAnalysis/blob/master/01_data_prep/06_users_info/issues/lackof3rdfield.png)

At this step, I put general information in one field, so I would tackle these problems when it needs to use these sub-general information.

### 152 abnormal users

These users are xiami artists and xiami users at the same time. I used 'tackle.py' to solve it.

## others.txt

152 abnormal users

## 48+25+79.md

log returned

## tackle.py

program used to solve it


## Glance

```
76664358    来自山东的女生 2015-10-25  3087    Lv6 25次访问   0   0   3
7666568 来自山东淄博的80后未知女生  2012-01-14  4635    Lv5 160次访问  2   2   8
76666466    欢迎 大虾   2015-10-25  351 Lv1 0次访问    0   0   0
7666786 欢迎 大虾   2012-01-14  3513    Lv5 243次访问  1   0   6
7666795 来自江苏苏州的80后射手座男生 2012-01-14  2045    Lv2 204次访问  1   1   6
7666816 欢迎 大虾   2012-01-14  19  Lv1 88次访问   0   0   0
76668528    欢迎 大虾   2015-10-25  267 Lv1 0次访问    0   0   0
76669322    欢迎 男生   2015-10-25  1204    Lv4 0次访问    0   0   1
766710  来自广东广州的魔羯座大虾    2010-03-30  19595   Lv6 759次访问  4   21  8
……
```
