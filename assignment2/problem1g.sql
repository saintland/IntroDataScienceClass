select new_value from (
select a.row_num, b.col_num, sum(a.value*b.value) as new_value
from A as a, B as b
where  a.col_num=b.row_num
group by a.row_num, b.col_num)
where row_num=2 and col_num=3;
 
