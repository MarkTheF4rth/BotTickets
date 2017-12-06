from Decorators.func import func

@func()
def ticket_vote(self, index_list, author_id):
    """Allows the given author to vote on a given index, 
        if votes are enabled on the ticket"""

    output = ['**__Damage Report:__**']

    for index in set(index_list):
        ticket_message, ticket_type = self.validate_ticket_index(index, author_id)
        
        if not ticket_type:
            output.append(ticket_message.format(index))
            continue
    
        index = int(index)

        if not ticket_type.votes:
            output.append(self.ticket_messages.vote_bad_ticket.format(ticket_type.plural))
            continue
    
        if author_id in ticket_type.tickets[index][0]:
            output.append(self.ticket_messages.already_voted.format(index))
            continue

        ticket_type.add_vote(index, author_id)
        output.append((self.ticket_messages.vote_ticket.format(index)))

    return '\n'.join(output)
