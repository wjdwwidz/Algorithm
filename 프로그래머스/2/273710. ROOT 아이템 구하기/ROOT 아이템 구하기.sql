-- 코드를 작성해주세요
SELECT t.ITEM_ID, i.ITEM_NAME 
FROM ITEM_INFO i 
    JOIN ITEM_TREE t 
    ON t.ITEM_ID = i.ITEM_ID
WHERE PARENT_ITEM_ID IS NULL 