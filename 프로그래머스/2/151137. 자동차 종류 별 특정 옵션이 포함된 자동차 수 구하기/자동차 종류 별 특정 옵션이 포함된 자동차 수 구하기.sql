-- 코드를 입력하세요
SELECT CAR_TYPE, count(car_id) as CARS
from CAR_RENTAL_COMPANY_CAR
where OPTIONS LIKE '%통풍시트%' or OPTIONS LIKE '%열선시트%' or OPTIONS LIKE '%가죽시트%'
group by 1
order by 1