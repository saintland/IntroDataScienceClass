select freq from (
select a.docid, b.docid as id2, sum(a.count*b.count) as freq
from frequency as a, frequency as b
where  a.term=b.term and a.docid<b.docid and a.docid='10080_txt_crude'
group by a.docid, b.docid )

where docid= '10080_txt_crude' and id2='17035_txt_earn';


