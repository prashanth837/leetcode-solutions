# Write your MySQL query statement belo
select max(num) as num from (select * from MyNumbers group by num having count(num)=1) as temp;