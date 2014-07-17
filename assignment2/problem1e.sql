 select count(*) from (select docid, sum(term) as term_count
from frequency
group by docid
having sum(count)>300);
