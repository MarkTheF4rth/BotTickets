from Decorators.command import command

@command(description='view requested features')
def viewrequests(self, message, ctx):
    """Dedicated command to print a list of request tickets"""
    output = self.ticket_view(self.tickets['request'], message.server)
    self.message_printer(output, message.channel)
