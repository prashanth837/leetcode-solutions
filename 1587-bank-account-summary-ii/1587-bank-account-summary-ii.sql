# Write your MySQL query statement below
select name,sum(amount) as balance from  Transactions as t join Users as u on u.account=t.account group by t.account having sum(amount)>10000;