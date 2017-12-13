from Decorators.command import command

@command(description='view requested features')
def viewrequests(self, message, ctx):
    """Dedicated command to print a list of request tickets"""
    channel = message.author

    if len(ctx.message_content) > 0 and ctx.message_content[0].lower() == 'pub':
        channel = message.channel

    output = self.ticket_view(self.tickets['request'], message.server)
    self.message_printer(output, channel)
