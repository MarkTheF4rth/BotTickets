from Decorators.func import func

@func()
def validated_ticket_removal(self, ticket_type, index, author_id, admin):
    """Validates whether a given user can remove a given ticket index, 
        then removes the ticket if appplicable"""


    ticket_message, ticket_type = self.validate_ticket_index(index, author_id, ticket_type)

    if not ticket_type:
        return ticket_message.format(index)

    index = int(index)

    if ticket_message == self.ticket_messages.not_owned_index and not admin:
        return ticket_message.format(index)

    del(self.reverse_ticket_ref[index])
    ticket_type.remove_ticket(index)
    return self.ticket_messages.remove_ticket.format(index)
