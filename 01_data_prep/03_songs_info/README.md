
This stage begain with `info_music（含名字）.txt` and `info_music.txt`. Their structures are listed below:

|table name|row|column|field1|field2|field3|
|---|---|---|---|---|---|
|info_music（含名字）.txt|820663|3|  orders| songID| song|
|info_music.txt|820663|2|orders| songID| |

These tables were driven from `relation` table in MySQL(which I specified in [02_database_schema]()).

`orders` means `Timeorder` in the table `relation`, this field records the order of users' favorite songs according to the time they added songs into their libraies,  reverse-chronological.

I selected unique **820663** songs from the favorites of users' sample.
