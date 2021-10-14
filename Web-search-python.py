import webbrowser
google = input("Google Search:")
webbrowser.open_new_tab("http://www.google.com/search?btnG=1&q=%s"% google)
