-- 코드를 입력하세요

SELECT b.title, b.board_id, r.reply_id, r.writer_id, r.contents,date_format(r.CREATED_DATE,'%Y-%m-%d')
FROM used_goods_board AS b
JOIN used_goods_reply AS r ON b.board_id = r.board_id
WHERE date_format(b.CREATED_DATE,'%Y-%m') ='2022-10'
ORDER BY r.created_date ASC, b.title ASC

