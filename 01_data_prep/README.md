# WebCrawler for Xiami Music

> This is for data collecting stage

## 1. Generate the sample: 3,250,000 user with their userID


## 2. Get the favorite lists of these users

> **(including the IDs and the names of their favorite songs)**

This step was conducted in [02_favorites_info](https://github.com/Vida42/XiamiMusicAnalysis/tree/master/01_data_prep/02_favorites_info). And then I import data into MySQL. After series of manipulation(which I specified in [02_database_schema]()), I got three tables:


|table name|row|column|field1|field2|field3|
|---|---|---|---|---|---|
|info_music  |820,663  |3 |orders   |songID|song    |
|info_user   |585,801  |1 |userID   |      |        |
|relation    |8,338,301|3 |Timeorder|userID|songID  |


## 3. Get the information of songs

> **(including the artist_ID, album_ID and album_name of these songs)**

Then I got this table:

|field1|field2|field3|field4|field5|
|---|---|---|---|---|
|order|song_ID|artist_ID|album_ID|album_name|

```
8123199	xLzbQid39f7	eH1u78067	kH5vd7e53	正能量·三元素
8123205	xLzbqldc8b1	bgrSabed9	g8jd81620	COUNTDOWN
8123206	xLzbQvcaa4a	dSlr47767	kKvVa5bfb	福島から伝えたい
8123207	xLzBrCb0c82	bmk2af9bd	pakRf9e96	丽风金典系列 歌坛好好先生
8123208	xLzBrGb674f	GNQ56112	pakSea3a1	終わりなき愛の決闘者(デュエリスト)
8123209	xLzBrK11586	bwqIe908d	gA9i947dc	Dusk to Dawn
8123214	xLzBrMd31b0	bwqIe908d	gA9i947dc	Dusk to Dawn
8123217	xLzBrOd6d1b	bwqIe908d	gA9i947dc	Dusk to Dawn
……
```


## 4. Get the information of albums

> **(including the album_language, album_released_date, album_genre of these albums)**


Then I got this table:

|field1|field2|field3|field4|field5|
|---|---|---|---|---|
|order|album_ID|album_language|album_released_date|album_genre|



```
728	0EEf2e69e	英语	2004年11月01日	280,875
729	0eeo34109	英语	2006年10月10日	473,831
730	0EEq33c11	英语	2007年05月14日	3076
731	0Ef630b95	英语	1995年01月31日	
732	0Eg8330e5	英语	2003年05月13日	147,768,773
733	0eH12f0cd	英语	1954年01月01日	721,1320
734	0Eh433809	英语	2008年12月12日	252,3076,265
736	0eiA321bd	英语	2006年03月27日	221,237,240
735	0EhN30acb	英语	2008年03月09日	280,3076
737	0Eik30de3	日语	2007年06月29日	
738	0eir2e234	英语	2006年08月08日	1353
739	0EIV313ad	国语	2001年10月29日	
740	0EIw2e4cf	英语	2007年01月01日	/genre/detail/gid/10
741	0eJ42f725	英语	2004年03月23日	265
742	0Eja30c81	其他	1999年01月01日	696
……
```


## 5. Get the information of artists

> **(including the artist_name, artist_genre info of artists of these artists)**

Then I got this table:

|field1|field2|field3|field4|
|---|---|---|---|
|order|artist_ID|artist_name|artist_genre|



```
253	2ML881cb	Supergrass	941
254	2Mn77ca5	Spiritualized	956,989,1200,1331,1381
255	2Mp7c3b8	Dusty Springfield	343,404,415,421,428
256	2MPea2d0	Matthew Sweet	685
257	2MS5b0e5	T. Rex	1148,275,278,322
258	2Mu53033	Status Quo	275,286
259	2Mz84ac5	Al Stewart	269,270,271,272,344
260	2N1641ee	Van Halen	275,280,283
261	2N35466a	Stevie Ray Vaughan & Double Trouble	113,118,323
262	2NA5aa4c	Violent Femmes	686,685,1331
263	2NG8c6f4	Weezer	835,1096,1331
……
```


## 6. Get the information of users

> **(including general information, jion time, play count, level, visit, follow, fans, feed of these users)**

Then I got this table:

|field1|field2|field3|field4|field5|field6|field7|field8|field9|
|---|---|---|---|---|---|---|---|---|
|order|general information|jion time|play count|level|visit|follow|fans|feed|


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


## 7. Get the information of genres

> **(including ID, Chinese name and English name of these genres)**
Then I got this table:

|field|field2|field3|
|---|---|---|
|genre_ID|genre_name_CN|genre_name_EN|


```
gid2	流行	Pop
3076	流行	Pop
1541	国语流行	Mandarin Pop
1542	粤语流行	Cantopop
2980	电音流行	Electropop
2970	欧美流行	Western Pop
360	日本流行	J-Pop
……
```
