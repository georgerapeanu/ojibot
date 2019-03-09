import subprocess
import argparse
import time
import os.path

subprocess.call("rm log.txt",shell = True);

parser = argparse.ArgumentParser()
parser.add_argument("--year",type=str,help="year of oji",required=True)
parser.add_argument("--sub_category",type=str,help="lic or gim",required=True)
parser.add_argument("--city",type=str,help="city number",required=True)
parser.add_argument("--grade",type=str,help="for which grade you want tracking",required=True)
parser.add_argument("--first_name",type=str,help='the first name which appears on olimpiada.info EXACTLY as it is there, use " if needed',required=True)
parser.add_argument("--second_name",type=str,help='the second name which appears on olimpiada.info EXACTLY as it is there, use " if needed',required=True)
tmp = parser.parse_args()
year = tmp.year
sub_category = tmp.sub_category
city = tmp.city
grade = tmp.grade
first_name = tmp.first_name
second_name = tmp.second_name

comand = "scrapy runspider crawl.py -a year=" + year + " -a sub_category="+ sub_category + " -a city=" + city + " -a grade=" + grade + ' -a first_name="' + first_name + '"' + ' -a second_name="' + second_name + '"'; 

TIME_INTERVAL = 5;

while(os.path.exists("./log.txt") == False):
    subprocess.call(comand,shell = True)
    if(os.path.exists("./log.txt") == True):
        break;
    time.sleep(TIME_INTERVAL)

print("done\n");
subprocess.call("cat ./log.txt",shell = True);
