
import re

class ConversationDb:
    def __init__(self):
        self.db = {}
        pass
        
    def read_database(self, filename):
        with open(filename) as file:
            lines = file.readlines()
            conv_start = False
            conv_key = ""
            for line in lines:
                print(line)
                if conv_start and conv_key != "":
                    match = re.match("\[EndConversation\]", line)
                    if match:
                        conv_start = False
                        conv_key = ""
                    else:
                        match = re.match("\d\.\s*(.*)", line)
                        if match:
                            self.db[conv_key].append(match.group(1))
                            print ("Append to key {} string {}".format(conv_key, match.group(1)))
                        else:
                            pass # Ignore any line that does not start with number and dot
                else:
                    if not conv_start:
                        match = re.match("\[Conversation\]", line)
                        if match:
                            conv_start = True
                            print("Conversation found")
                        else:
                            print("here??")
                            pass # ignore anything until a conversation tag is found
                    else:
                        match = re.match("Title=(.*)", line)
                        if match:
                            title = match.group(1)
                            print ("Setting key to: {}".format(title))
                            conv_key = title
                            self.db[conv_key] = []
                        else:
                            pass # ignore anything until a title is found
                            
    def dump_database(self):
        print (self.db)
        
    def get_conversation(self, key):
        return self.db[key]

