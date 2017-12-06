from Decorators.command import command

@command(description='view reported bugs')
def viewreports(self, message, ctx):
    """Dedicated command to print a list of report tickets"""
    output = self.ticket_view(self.tickets['report'], message.server)
    self.message_printer(output, message.channel)
