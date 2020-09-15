# file to compile all the return messages used to inform the user
from django.utils.translation import ugettext_lazy as _

ERROR_LENGTH_TEAM = _('Não foi possível criar o seu time :(. Um time precisa ter 6 pokémons, '
                      'por favor adicione mais amiguinhos para continuar sua jornada.')

ERROR_LENGTH_TEAM_NAME = _('O nome do seu time precisa ter no mínimo 5 caracteres.')


ERROR_TEAM_WITHOUT_NAME = _('Este campo não pode ser em branco.')