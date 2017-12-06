from Decorators.func import func

@func()
def validate_ticket_index(self, index, author_id, ticket_type=None):
    """validates whether a ticket index is correct, if no ticket_type is given, 
        searches if and where the index is located,
        returns the associated message and the ticket type"""

    if not index.isdigit():
        return self.ticket_messages.invalid_index, None

    index = int(index)

    if not ticket_type: # find what ticket type the index could belong to
        if index not in self.reverse_ticket_ref:
            return self.ticket_messages.bad_index, None

        ticket_type = self.tickets[self.reverse_ticket_ref[index]]

    if index not in ticket_type.tickets:
        return self.ticket_messages.bad_index, None


    if not ticket_type.tickets[index][0][0] == author_id:
        return self.ticket_messages.not_owned_index, ticket_type

    return self.ticket_messages.valid_status, ticket_type
