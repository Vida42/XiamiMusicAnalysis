
# Get the album_language, album_released_date, album_genre of albums

Using album_ID to get these infomation.

## Issues

有的专辑（比如s7xRpa52f9）
爬音乐信息的时候获得专辑id为此

然而访问时显示被删，在数据库查名字，又有专辑名，在虾米搜，发现真实id为325213
这类专辑包括：


```
472819	8GiEVie46e1	iSdJd008c	kCoRbb594	光蕊
744707	8GuIt7ec0a7	eGTA86eb6	xdJhS0b2de2	Honest (Remixes)
883817	8HNXlpf59e0	yhDqpSc0d56	bfMQK3N33975	Still Got Time (The Remixes)
2280641	bqvuuY937cdb	iSdJd008c	gTd1zd4ba3b	原来你在这里等我
2291726	bqvwD9P3997c	eGTA86eb6	xdJhS0b2de2	Honest (Remixes)
2625802	creKmffa13	bcnJdb709	s7xRpa52f9	Hôtel Costes, Vol. 1
2626286	crf0Ze6d07	bMgK23ea4	Q9VSi3a75d	Funkymix_122
2667735	cXcm4230f2	berra9395	s7xRpa52f9	Hôtel Costes, Vol. 1
2667736	cXcm821f85	bih0c1465	s7xRpa52f9	Hôtel Costes, Vol. 1
2667795	cXcTy24021	nnaYB850f92	Q9VSi3a75d	Funkymix_122
2962842	esXOa3015d	ba19a30b8	Q9VSi3a75d	Funkymix_122
3016460	eYU93394f3	3RG4dff3	s7xRpa52f9	Hôtel Costes, Vol. 1
3956981	mQ4bEc6a8c1	dnyl36798	jQBUa07ee	CHANGE オリジナル・サウンドトラック
1635046	bBhrFe0331	TTZb01a6	s7xRpa52f9	Hôtel Costes, Vol. 1
1635055	bBhrGc464a	3SY87240	s7xRpa52f9	Hôtel Costes, Vol. 1
1635057	bBhrLd4036	doVn394a4	s7xRpa52f9	Hôtel Costes, Vol. 1
1635058	bBhrMccb40	b9a1fdb45	s7xRpa52f9	Hôtel Costes, Vol. 1
1635060	bBhrOd6526	berra9395	s7xRpa52f9	Hôtel Costes, Vol. 1
1635061	bBhrPa41e3	berra9395	s7xRpa52f9	Hôtel Costes, Vol. 1
1635088	bBhrT12547	Z5Pbf22d	s7xRpa52f9	Hôtel Costes, Vol. 1
5314543	mQRHpQ60be0	e3Acfc24	bC6Xc7a48ffa	台湾美乐地
5649893	mSsKrb60523	nn9nQo550cd	nndY2i56d69	Strip That Down (Acoustic)
6447814	VjPy7f056	berra9395	s7xRpa52f9	Hôtel Costes, Vol. 1
6842973	xL7OA5a5442	dtM943a6	7QOtVtf763c	被遗忘的名字
7014998	xLAMlXd2777	lLWnF67575	cuqmW6c70ee	挥别昨天的我
8036192	xLxGg5d1e03	iSdJd008c	kCoRbb594	光蕊
7236786	xLHBtcd034a	nmSr7b5e8d5	yhEFXycfd49	广东队2016CYPHER
8307731	xNga7ec81b3	dVSO49802	nnenbL5f9b6	I Get the Bag
8308912	xNgTpBab7db	6rzec77a	yhPtDMd9fee	Los Ageless
5678926	mSvPyw6e8b2	bqH0qBe3589f	yhPsOOa2295	Plot Twist (Remix)
```

其中歌曲共被收藏125次


能加信息的就325213（从虾米都打不开，只能从外链打开）

CHANGE オリジナル・サウンドトラック的专辑id不对了（song id打不开，艺人id正确）

By the end, I got one file:

* order, album_ID, album_language, album_released_date, album_genre
