import json
import dateutil.parser
htmlstart = "<html><body><div class=\"mTable\"><table><link rel=\"stylesheet\" href=\"chat.css\">"

htmlend = "</body></table></div></html>"
mid = ""
sentTo = input().strip()
tooltip = "<span class=\"tooltiptext\">"
tooltipend= "</span>"
with open("messages.json", "r",encoding="utf8") as read_file:
    data = json.load(read_file)
    for c in data:
        if(c['participants'][0] == sentTo or c['participants'][1] == sentTo):
            print(c['participants'])
            for x in (c['conversation'])[::-1]:
                dt = dateutil.parser.parse(x['created_at'])
                mint = "{:02}".format(int(dt.time().minute))
                dt = str(dt.date())+" "+ str(dt.time().hour)+ ":" + mint
                if(x['sender'] == sentTo):
                    try:
                        mid += "<tr><td class=\"to tooltip\" >"+tooltip+dt + tooltipend + x['text'] + "</td></tr>\n "
                    except:
                        try:
                            mid += "<tr><td class=\"to tooltip\" >"+tooltip+dt + tooltipend + "<img src=\"{}\"".format(x['media_share_url']) + "</td></tr>\n "
                        except:
                            try:
                                mid += "<tr><td class=\"to tooltip\" >"+tooltip+dt + tooltipend + "<img src=\"{}\"".format(x['media']) + "</td></tr>\n "
                            except:
                                pass
                else:
                    try:
                        mid += "<tr><td class=\"me tooltip\">" +tooltip+dt + tooltipend +  x['text'] + "</td></tr>\n"
                    except:
                        try:
                            mid += "<tr><td class=\"me tooltip\">" +tooltip+dt + tooltipend +  "<img src=\"{}\"".format(x['media_share_url']) + "</td></tr>\n"
                        except:
                            try:
                                mid += "<tr><td class=\"me tooltip\">" +tooltip+dt + tooltipend +  "<img src=\"{}\"".format(x['media']) + "</td></tr>\n"
                            except:
                                pass

f = open('output.html', 'w',encoding="utf8")
start = "<h1>" + sentTo + "</h1>"
f.write(htmlstart + start + mid + htmlend)
f.close()