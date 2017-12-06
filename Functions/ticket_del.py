from Decorators.func import func
import copy

@func()
def ticket_del(self, ticket_type, index_list, author_roles, author_id):
    """Deletes a ticket by given ticket index, this will check that you either
        own the ticket, or you have permission to delete other peoples tickets (administrator)
        Alternatively the "all" parameter will cause all tickets owned by the user to be deleted"""

    output = ['**__Damage Report:__**']

    if 'all' in index_list and ticket_type:
        index_list = sorted([key for key in ticket_type.tickets])

        for index in index_list:
            if ticket_type.tickets[index][0][0] == str(author_id):
                ticket_type.remove_ticket(index)
                output.append(self.ticket_messages.remove_ticket.format(index))
                del(self.reverse_ticket_ref[index])

    else:
        admin_roles = set(self.ticket_config['admin roles'])
        author_roles = set([author_role.name for author_role in author_roles])
        admin = admin_roles.intersection(author_roles)

        [output.append(self.validated_ticket_removal(ticket_type, index, author_id, admin)) 
                    for index in set(index_list)]


    
    self.save_file('backref', self.reverse_ticket_ref)
    self.save_file(ticket_type.name, ticket_type.tickets, ticket=True)
    return '\n'.join(output)

