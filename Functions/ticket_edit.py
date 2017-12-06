from Decorators.func import func

@func()
def ticket_edit(self, ticket_type, user_id, content, index=-1):
    """Creates a ticket for a given ticket type, optional arguments allow 
        setting ticket index and allowing users to place votes on the ticket"""

    if not self.buffer_compare(user_id, content): # prevents duplicate messages
        return

    if not index+1: # if no index is given, create a new one
        index = self.index
        self.index += 1

    self.reverse_ticket_ref[index] = ticket_type.name
    ticket_type.add_ticket(index, ' '.join(content), user_id)

    self.save_file('index', self.index)
    self.save_file('backref', self.reverse_ticket_ref)
    self.save_file(ticket_type.name, ticket_type.tickets, ticket=True)

    return self.ticket_messages.add_ticket.format(str(index))

