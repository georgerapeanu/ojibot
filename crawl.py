import scrapy
from scrapy.crawler import CrawlerProcess
import re
import subprocess

TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        
        url = 'http://www.olimpiada.info/oji' + str(self.year) + \
              '/index.php?cid=rezultate&w=' + str(self.sub_category) + \
              '&judet=' + str(self.city) + '&clasa=' + str(self.grade);
        
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        retrieved_data = response.css("td").getall();
        
        st = 26
        dr = 36
        delta = 10
        
        if(self.sub_category == "gim"):
            delta = delta - 1;
       

        print('"%s"\n"%s"\n' % (self.first_name , self.second_name));

        while(dr < len(retrieved_data)):
            data = []
            for i in range(st,dr):
                data.append(remove_tags(retrieved_data[i]).strip())
            if data[1] == self.first_name and data[2] == self.second_name:
                f = open("log.txt","w");
                for item in data:
                    f.write(str(item) + " ");
                f.write("\n");
            st = st +  delta;
            dr = dr + delta;
