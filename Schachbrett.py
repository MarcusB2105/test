summe = 0
for feld in range(64):
    reiskorn = 2**feld
    summe=summe+reiskorn
    print("Feld {}. = {:>30,} Reiskörner und damit insgesamt {:>30,} Reiskörner" \
            .format(feld+1,reiskorn,summe))