import chardet
import csv
import datetime
import os

codec = 'utf-16'
table_cwidth = [7.5, 15, 7.5, 2.5, 7.5, 7.5, 7.5, 12.5, 12.5, 7.5, 7.5]
event_name = "Swimming Gala"
event_date = ["06", "10", "2025"]
event_year = ["2025", "2026"]

script_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_dir)

try:
    def convert(csv_filename, html_filename, is_result=False):
        global codec
        global table_cwidth

        title = "Entry List"
        if is_result == True:
            title = "Result"
        print(title)
        init = '<html>\n<head>\n<style>table, th, td {\n  text-align: center;\n  margin-left: auto;\n  margin-right: auto;\n  border: 1px solid black;\n  border-collapse: collapse;\n}\n</style>\n<title> ' + title + ' </title>\n</head>\n<body><p style="text-align: right;"><i>\n'
        init += str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        init += "\n</i></p>"
        init += '<pre style="text-align:center; font-family:Arial; font-size: 300%; margin-bottom: 0.5%; margin-top: 2%;"><b> ' + "St. Mark's School" + ' </b></pre>\n'
        init += '<pre style="text-align:center; font-family:Arial; font-size: 250%; margin: 0.5%;"><b> ' + event_name + " (" + event_year[0] + '-' + event_year[1] + ') </b></pre>\n'
        init += '<pre style="text-align:center; font-family:Arial; font-size: 150%; margin: 0.5%;"><b><i> ' + event_date[0] + "/" + event_date[1] + "/" + event_date[2] + ' </i></b></pre>\n'
        init += '<pre style="text-align:center; font-family:Times New Roman; font-size: 150%; margin: 1.5%;"><b><i> ' + "EVENT RECORD SHEET" + ' </i></b></pre>\n'
        print(init)
        with open(html_filename, "w", encoding=codec) as output:
            output.write(init)
        print(init)
        with open(csv_filename, "r", encoding=codec) as table:

            # initialize
            head_info = ""
            group = "O"

            # input head text
            for i in range(5):
                line = table.readline().split('"')
                print(line)
                head = line[1]
                cont = line[3]
                if i == 1:
                    cont_words = cont.split()
                    if cont_words[1] == "C":
                        group = "C"
                if cont == "":
                    cont = "None"
                if i != 0:
                    head_info += '          '
                head_info += (head+": "+cont)
            if is_result == True:
                with open(html_filename, 'a', encoding=codec) as output:
                    output.write('<h2><pre style="text-align:center; font-family:Arial;"> ' + head_info + ' </pre></h2>\n')
                print(head_info)
            line = table.readline()

            # output the tables
            for i in range(1, 10000):
                line = table.readline().split('"')
                if (line == ['']):
                    break
                print(i, line)
                fmt_table = '<table style="width: 95%;"> <tr height="27.5px"> <th colspan="11">Heat No. ' + str(i) + ' Grade: ' + group + '</th> </tr> '
                
                for j in range(1, 100000):
                    line = table.readline().split('"')
                    print("Scanning for", j, "th time:", line)
                    print(len(line))
                    if (len(line) == 23):
                        fmt_table += ' <tr height="27.5px"> '
                        for z in range(11):
                            print("Formatting", z, "th column:")
                            fmt_table += (' <th width=' + str(table_cwidth[z]) + '%> ' + line[z*2+1] + ' </th> ')
                        fmt_table += ' </tr> '
                    elif (line == ['', '', '\n']) or (line == ['']):
                        line = table.readline().split('"')
                        fmt_table += ' </table> <br> '
                        break
                with open(html_filename, 'a', encoding=codec) as output:
                    output.write(fmt_table)
                print(fmt_table)
                
                # with open(html_filename, 'w', encoding='utf-8') as htmlfile:
                #     htmlfile.write('<html>\n<head><title>CSV Data</title></head>\n<body>\n')
                #     htmlfile.write('<table border="1">\n')
                #     htmlfile.write('<tr>' + ''.join(f'<th>{header}</th>' for header in headers) + '</tr>\n')

                #     for row in reader:
                #         htmlfile.write('<tr>' + ''.join(f'<td>{cell}</td>' for cell in row) + '</tr>\n')

                #     htmlfile.write('</table>\n</body>\n</html>')
        with open(html_filename, 'a', encoding=codec) as output:
            output.write("</body>")

    # Example usage
    convert('event-result.csv', 'convert.html', True)
except Exception as e:
    print(e)