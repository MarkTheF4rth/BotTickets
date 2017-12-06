from Decorators.command import command

@command(usage=[('ticket type', ''), ('', '...')], description="clears all tickets of a given ticket type")
def cleartickets(self, message, ctx):
    """Finds which ticket type needs to be cleared, then runs a function to clear it"""

    ticket_name = ctx.message_content[0]

    if ticket_name not in self.tickets:
        self.message_printer(self.ticket_messages.bad_ticket_type.format(ticket_name), message.channel)
        return

    ticket_type = self.tickets[ticket_name]
    ticket_type.clear_tickets()
    self.clear_reverse_ticket_ref(ticket_type)

    self.save_file(ticket_type.name, ticket_type.tickets, ticket=True)

    self.message_printer(self.ticket_messages.clear_all.format(ticket_type.plural), message.channel)
