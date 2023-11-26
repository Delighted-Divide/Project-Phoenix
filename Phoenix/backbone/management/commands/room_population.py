from django.core.management import BaseCommand
from accounts.models import CustomUser
from backbone.models import Room
import random
import string
import requests
import math
from django.db.models import Count


class Command(BaseCommand):
    help = 'Creates Rooms'

    def add_arguments(self, parser):
        parser.add_argument('--GW', type=int, default=0,
                            help='The number of Rooms')
        parser.add_argument('--SP', type=int, default=0,
                            help='The number of Rooms')
        parser.add_argument('--PR', type=int, default=0,
                            help='The number of Rooms')
        parser.add_argument('--DL', type=int, default=0,
                            help='The number of Rooms')
        parser.add_argument('--KD', type=int, default=0,
                            help='The number of Rooms')                         
        parser.add_argument('--all', type=int, default=0,
                            help='The number of Rooms')

    def handle(self, *args, **kwargs):
        list_of_room_types = ["GW", "SP", "PR", "DL", "KD"]
        room_dict = {room_type: kwargs[room_type] + kwargs['all']
                     for room_type in list_of_room_types}
        [Room(room_type=room_type).save()
         for room_type in room_dict for times in range(room_dict[room_type])]
        self.stdout.write(self.style.SUCCESS(
            f'Successfully created Rooms '))
        for rtype, room_count in room_dict.items():
            self.stdout.write(self.style.SUCCESS(
                f'Successfully created {rtype} - {room_count}'))
