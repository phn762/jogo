from django.core.management.base import BaseCommand
from jogo.models import Usuario


class Command(BaseCommand):
    help = 'Este é um comando personalizado para deletar todos os usuários.'

    def handle(self, *args, **kwargs):
        usuarios_deletados, _ = Usuario.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(
            f'Todos os usuários foram deletados com sucesso! Total: {usuarios_deletados}'))
