import re


class StripHtmlCommentsMiddleware(object):
    """
    Strips all html comments from response content.
    """

    def __init__(self):
        self.htmlcomments = re.compile('\<![ \r\n\t]*(--([^\-]|[\r\n]|-[^\-])*--[ \r\n\t]*)\>')

    def process_response(self, request, response):
        if "text" in response['Content-Type']:
            new_content = self.htmlcomments.sub('', response.content)
            response.content = new_content
            return response
        else:
            return response
