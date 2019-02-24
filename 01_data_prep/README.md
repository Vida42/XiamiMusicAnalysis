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
