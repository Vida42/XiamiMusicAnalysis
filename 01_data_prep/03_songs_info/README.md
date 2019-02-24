
This stage begain with `info_music（含名字）.txt` and `info_music.txt`. Their structures are listed below:

|table name|row|column|field1|field2|field3|
|---|---|---|---|---|---|
|info_music（含名字）.txt|820663|3|  orders| songID| song|
|info_music.txt|820663|2|orders| songID| |

These tables were driven from `relation` table in MySQL(which I specified in [02_database_schema]()).

`orders` means `Timeorder` in the table `relation`, this field records the order of users' favorite songs according to the time they added songs into their libraies,  reverse-chronological.

I selected unique **820663** songs from the favorites of users' sample.



First I used `arrange&combine.py` to split `info_music.txt` to 12 files:

info_music1.txt to info_music12.txt

Then I ran the program in different computers and combine the results into one file by using `arrange&combine.py` again.

## Issues

the results should be:

index, song_id, artist_id, album_id, album_name

```
368 0Gmi523a9   ev94f6c1    7Th6c17f    appears
369 0GMs32352   j8Qf7140    XYQd3ce1    Delicious! ~The Best of Hitomi Shimatani~
371 0GQD4b948   b5UJf0496   7Y25b932    雅
378 0GTH2fa8c   ew5941a7    deen3a543   Gravity
……
```

but for 302(ixiami):

That means there is a redirection. When you input `https://www.xiami.com/song/` + `sond_id`, it will redirect to a new link, which shows it's a song of `Xiami Artists`: independent artists or signing singers who share their music, interact with fans and sell songs by Xiami's [Artists Channel](https://technode.com/2013/07/17/xiami-artists-music-retail-platform-for-musicians/).

And these songs have no album info.

index, song_id, url, 302, 302

```
538513  8GlG08e2a90 http://i.xiami.com/aiyan    302_redirected  302_redirected
538517  8GlG0N18ac9 http://i.xiami.com/liuminghui   302_redirected  302_redirected
542258  8GlHS1f21bb http://i.xiami.com/chenyonghai  302_redirected  302_redirected
5420105 mQVTcS5dc8d http://i.xiami.com/wishbao  302_redirected  302_redirected
5420220 mQVTfK6129b http://i.xiami.com/jimingzzhan  302_redirected  302_redirected
5420587 mQVtLA562dc http://i.xiami.com/mcshenqi 302_redirected  302_redirected
……
```

for 404(deleted):

that means the link of song can't be open. it shows:"您所查看的歌曲不存在或已经删除"

<p align="center">
    <img src="https://github.com/Vida42/XiamiMusicAnalysis/blob/master/01_data_prep/03_songs_info/01_03_song_404.PNG" alt="Sample"  width="512" height="380">
    <p align="center">
        <em></em>
    </p>
</p>

so there is no artist or album accordingly

index, song_id, 404, 404, 404

```
3474568 JASF5l20d95 404_deleted 404_deleted 404_deleted
3489233 JAUPXK23f14 404_deleted 404_deleted 404_deleted
1395003 b5XNv9889e  404_deleted 404_deleted 404_deleted
1036646 b1pRMCH647e7    404_deleted 404_deleted 404_deleted
1062968 b1pX5bT4255d    404_deleted 404_deleted 404_deleted
……
```


some have no album(and some have no artist):

that means the link of album can be open, but thers is nothing. it shows:"您所查看的专辑不存在或已经删除"


<p align="center">
    <img src="https://github.com/Vida42/XiamiMusicAnalysis/blob/master/01_data_prep/03_songs_info/01_03_album_none.PNG" alt="Sample"  width="512" height="380">
    <p align="center">
        <em></em>
    </p>
</p>


When an albumID is `ucad5b`, it's definitely empty(already deleted from the website). WHen an albumID is not `ucad5b`, it also has the probability to be empty.


index, song_id, ucad5b, ucad5b, 专辑为空

```
4802730 mQHzLJ870b1 fZg05q26f0e ucad5b  专辑为空
821738  8GzKNCe571c mNmzDa73dbc ucad5b  专辑为空
828592  8GzXX4e35f0 mNmzDa73dbc ucad5b  专辑为空
1010414 b1pOj943d324    ucad5b  fLfp5fe35   专辑为空
1010415 b1pOj95404db    ucad5b  fLfp5fe35   专辑为空
……
```


By the end, I got two files:

* one for normal songs
* one for abnormal songs(302, 404, empty album)
