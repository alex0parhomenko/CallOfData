import json
import pdftotree
import html2text
import re
from collections import defaultdict
from run_ozon_ticket import run as get_dates
from run_polyglot import run_polyglot

def load_pdf(path):
    html = pdftotree.parse(path)
    test = html2text.html2text(html)
    return text.lower()

def load_json(path):
    text = json.loads(json_data["body"]['text'])
    #text = json.load(open(path))['text']
    return text.lower()

def prepare_regexp_locations(s):
    #locations = ['москв[а-я]', 'саратов[а-я]{0,1}', 'калуlocations = run_polyglot(s)
    good_locations = sorted(locations, key = lambda k:locations[k])[::-1][:2]
    regex = r'\s|'.join([r"("  +loc + ")" for loc in good_locations]) + '\s'

    #if len(re.findall(regex, s)) == 0:
    #    locations = ['moscow', 'erevan', 'kaluga']
    #    regex = r'\s|'.join([r"("  +loc + ")" for loc in locations]) + '\s'
    return regex

def find_all_locations_text(s, regex, prev_num_str = 2):
    lst =[]
    num_str = prev_num_str
    for match in re.finditer(regex, s):
        location = [group for group in match.groups() if group is not None][0]
        start = match.start()
        str_split = [macth.end() for macth in re.finditer(r'\n',s[:start])]
        if len(str_split) >= num_str:
            start_pos = str_split[-num_str]
        else:
            start_pos = str_split[0]

        lst.append((location, start_pos, match.end()))
    return lst

def group_flights(s, locations_lst):
    flights = defaultdict(lambda:[])
    for i in list(range(2, len(locations_lst) + 1, 2)):
        cur_flight = locations_lst[i - 2: i]
        start = min(cur_flight[0][1], cur_flight[1][1])
        end = max(cur_flight[0][2], cur_flight[1][2])
        from_loc, to_loc = cur_flight[0][0], cur_flight[1][0]
        if from_loc != to_loc:
            flights[(from_loc, to_loc)].append((start, end))   

    top_keys = sorted(flights, key = lambda x: len(flights[x]), reverse=True)[:2]
    flights_text = dict()
    for key in top_keys:
        flights_text[key] = '\n'.join([s[start:end] for start, end in flights[key]])
        
    res = dict()
    for key in flights_text:
        res[key] = get_dates(flights_text[key])[0]
    return res

def parse_flights(text):
    regexp = prepare_regexp_locations(text)
    locations = find_all_locations_text(text, regexp)
    return group_flights(text, locations)

def avia_handler(self, data, files):
    try:
        text = load_json(data)
        res = parse_flights(text)
        if len(res) > 0:
            return True, res
    except:
         pass
        
    for file in files:
        if file.endwith('.pdf'):
            try:
                text = load_json(data)
                res = parse_flights(text)
                if len(res) > 0:
                    return True, res
            except:
                pass
    return False, None