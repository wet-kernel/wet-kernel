
def show_issue():
    issue_filename = "etc/issue"
    file = open (issue_filename,"r")
    strv = file.read()
    file.close()
    print (strv)