select count(*) from (
select distinct a.docid
from frequency a, frequency b
where a.docid=b.docid
      and a.term='world' and b.term='transactions'
);
