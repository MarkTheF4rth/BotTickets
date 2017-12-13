from Decorators.command import command

@command(usage=[('ticket type', ''), ('ticket description', '...')], 
        category='TicketDefault',
        description='Create a ticket of a chosen ticket type')
def ticket(self, message, ctx):
    """Creates a ticket of the given ticket type"""

    ticket_type = ctx.message_content['ticket type']

    if ticket_type not in self.tickets:
        self.message_printer(self.ticket_messages.bad_ticket_type.format(ticket_type), message.channel)
        return

    output = self.ticket_edit(self.tickets[ticket_type], message.author.id, ctx.message_content)

    self.message_printer(output, message.channel)
