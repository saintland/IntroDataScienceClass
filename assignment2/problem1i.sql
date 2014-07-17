select max(freq) from (
select a.docid as docid, b.docid as id2, sum(a.count*b.count) as freq
from (
SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count ) as a, 
(
SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count ) as b


where  a.term=b.term and a.docid='q'and a.docid!=b.docid
group by a.docid, b.docid );




