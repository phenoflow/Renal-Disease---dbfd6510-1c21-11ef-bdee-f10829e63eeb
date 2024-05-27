# Victor W Zhong, Juhaeri Juhaeri, Stephen R Cole, Christian M Shay, Carolyn A Chew-Graham, Penny Gordon-Larsen, Evangelos Kontopantelis, Elizabeth J Mayer-Davis, 2024.

import sys, csv, re

codes = [{"code":"Kyu1100","system":"readv2"},{"code":"K03V.00","system":"readv2"},{"code":"Kyu5G00","system":"readv2"},{"code":"K06..12","system":"readv2"},{"code":"K035.00","system":"readv2"},{"code":"K10y200","system":"readv2"},{"code":"K06..00","system":"readv2"},{"code":"K10y100","system":"readv2"},{"code":"L070300","system":"readv2"},{"code":"K10y000","system":"readv2"},{"code":"K03..12","system":"readv2"},{"code":"7L1Ay00","system":"readv2"},{"code":"K10yz00","system":"readv2"},{"code":"L393000","system":"readv2"},{"code":"K190X00","system":"readv2"},{"code":"K10y.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('renal-disease-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["renal-disease-specif---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["renal-disease-specif---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["renal-disease-specif---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
