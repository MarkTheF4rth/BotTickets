from Decorators.func import func

@func()
def ticket_unvote(self, index_list, author_id, server):
    """Removes a vote from a given ticket index"""

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
            if author_id == ticket_type.tickets[index][0][0]:
                if ticket_type.variable_author and len(ticket_type.tickets[index][0]) > 1: 
                    new_player_id = ticket_type.tickets[index][0][1]
                    user = server.get_member(new_player_id)

                    if not user: # player has left the server
                        mention_string = author_id
                    else:
                        mention_string = user.mention

                    ticket_type.remove_vote(index, author_id)
                    output.append(self.ticket_messages.pass_author.format(index, mention_string))

                else:
                    del(self.reverse_ticket_ref[index])
                    ticket_type.remove_ticket(index)
                    self.save_file('backref', self.reverse_ticket_ref)
                    output.append(self.ticket_messages.unvote_self_del.format(index))

            else:
                ticket_type.remove_vote(index, author_id)
                output.append(self.ticket_messages.unvote.format(index))

        else:
            output.append(self.ticket_messages.bad_unvote.format(index))

        self.save_file(ticket_type.name, ticket_type.tickets, ticket=True)
    return '\n'.join(output)


