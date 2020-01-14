import glob
import urllib


class MysteriousBotHandler(object):
    '''
    A docstring documenting this bot.
    ed28a8253771abc270763026cd15b95df138101a
    '''
    def __init__(self):
        self.commands = {
          "default": self.usage,
          "list": self.handle_list,
        }

    def usage(self, args, message):
        return '''
        This is the wiki bot.\nTry typing `list`
        '''

    def handle_message(self, message, bot_handler):
        args = message["content"].split()
        response = self.commands.get(args[0], self.commands["default"])(args[1:], message)
        print(response)
        bot_handler.send_reply(message, response)

    def handle_list(self, args, message):
        response = self.format_index_response(self.get_wiki_index())
        return response

    def get_wiki_index(self):
        wiki_files = {}
        for file in glob.glob("./rc-wiki/*.md"):
            wiki_title = file[10:-3].replace("-", " ")
            wiki_files[wiki_title] = file
        return wiki_files
    
    def format_index_response(self, wiki_dict):
      wiki_return_array = []
      for wiki in wiki_dict:
        wiki_uri = urllib.parse.quote(wiki_dict[wiki][10:-3])
        formatted_wiki_entry = "[{}](https://github.com/recursecenter/wiki/wiki/{})".format(wiki, wiki_uri)
        wiki_return_array.append(formatted_wiki_entry)
      
      wiki_return_array = sorted(wiki_return_array, key=str.casefold)
      return "\n".join(wiki_return_array)


handler_class = MysteriousBotHandler
