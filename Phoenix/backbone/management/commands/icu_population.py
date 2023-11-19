from django.core.management.base import BaseCommand
from backbone.models import ICU

class Command(BaseCommand):
    help = 'Generate ICUs with Greek symbols as labels'

    GREEK_SYMBOLS = GREEK_SYMBOLS = ['α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ', 'λ', 'μ', 'ν', 'ξ', 'ο', 'π', 'ρ', 'σ', 'τ', 'υ', 'φ', 'χ', 'ψ', 'ω']

    def add_arguments(self, parser):
        parser.add_argument('number', type=int, help='Number of ICUs to generate')

    def handle(self, *args, **kwargs):
        number = kwargs['number']
        for i in range(number):
            label = self.GREEK_SYMBOLS[i % len(self.GREEK_SYMBOLS)]
            ICU.objects.create(Label=label)
            self.stdout.write(self.style.SUCCESS(f'Created ICU with label: {label}'))
