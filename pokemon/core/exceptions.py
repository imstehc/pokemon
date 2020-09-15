from rest_framework.exceptions import APIException
from core import messages


# personalized classes of exceptions to validate make error messages more friendly to the user
class TeamLengthNameNotAllowedException(APIException):
    status_code = 500
    default_detail = messages.ERROR_LENGTH_TEAM_NAME


class TeamLengthNotAllowedException(APIException):

    status_code = 500
    default_detail = messages.ERROR_LENGTH_TEAM


