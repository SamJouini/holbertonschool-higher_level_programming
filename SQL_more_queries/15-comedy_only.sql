-- lists all Comedy shows in the database 
SELECT ts.title
FROM tv_shows ts
INNER JOIN tv_show_genres tsg ON ts.id = tsg.show_id
INNER JOIN tv_genres tg ON tsg.genre_id = tg.id
WHERE tg.name = 'Comedy'
ORDER BY ts.title ASC;
