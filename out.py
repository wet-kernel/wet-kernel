
def out(values):
    for i in values:
        print(i.replace("\\n","\n").replace("\\a","\a").replace("\\b","\b").replace("\\f","\f").replace("\\r","\r").replace("\\t","\t").replace("\\v","\v").replace("\\s"," "),end=' ')