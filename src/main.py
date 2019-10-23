

import conversation_engine
import conversation_db
from conversation_engine import ConversationEngine
from conversation_db import ConversationDb

conv = ConversationEngine(lang="nl", translate_lang="es")
db = ConversationDb()
db.read_database("conversations.txt")
db.dump_database()
my_conversation = db.get_conversation("Een slecht weer")
for text in my_conversation:
    conv.speak(text)
    
# conv.tranlate_speech()
# conv.speak("Esta es una prueba")
# conv.listen()

