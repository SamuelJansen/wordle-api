from python_framework import Controller, ControllerMethod, HttpStatus

from dto import SessionDto


@Controller(url = '/api/match', tag='RapiApiSecurity', description='RapiApi Security controller')
class RapiApiSessionController:

    @ControllerMethod(url = '/authenticate',
        responseClass = [SessionDto.SessionResponseDto]
    )
    def post(self):
        return self.service.game.createContext(), HttpStatus.CREATED
