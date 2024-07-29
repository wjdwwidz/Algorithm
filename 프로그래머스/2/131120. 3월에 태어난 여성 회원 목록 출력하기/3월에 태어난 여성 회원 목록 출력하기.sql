-- 코드를 입력하세요

SELECT MEMBER_ID, MEMBER_NAME, GENDER, date_format(DATE_OF_BIRTH,'%Y-%m-%d')
from MEMBER_PROFILE
where month(date_of_birth) = 3 and TLNO is not null and gender = 'w'
order by MEMBER_ID;