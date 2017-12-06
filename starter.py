from Decorators.task import task
import os, sys

sys.path.insert(0, os.getcwd())

from Classes.ticket_messages import Ticket_Messages

BOTTICKETS_DESCRIPTION = 'A bot that manages user tickets'
BOTTICKETS_CREDITS = 'Created by @MII#0255 (<https://github.com/MarkTheF4rth/Ticket_Bot>)'

@task(run_time='init')
async def ticket_bot_startup(self):
    self.module_info.update({'Ticket_Bot':(BOTTICKETS_DESCRIPTION, BOTTICKETS_CREDITS)})

    self.ticket_file_suffix = '.p' # suffix added onto every file saved in this module
    self.ticket_data_dir = self.data_dir+'Ticket_Bot/'
    self.ticket_messages = Ticket_Messages
    self.buffer = {}

    self.ticket_types = self.config['TicketBot']['ticket types']
    self.ticket_config = self.config['TicketBot']['main']
    self.sync_ticket_data()
