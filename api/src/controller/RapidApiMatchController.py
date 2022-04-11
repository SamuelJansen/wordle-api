from python_framework import Controller, ControllerMethod, HttpStatus

from enumeration.MatchContext import MatchContext
from dto import WordGuessDto, MatchDto


@Controller(url='/api/match', tag='RapiApiMatch', description='RapiApi Match controller')
class RapidApiMatchController:

    @ControllerMethod(url = '/verify',
        requestParamClass = WordGuessDto.WordGuessRequestParamDto,
        contextRequired = [MatchContext.USER],
        responseClass = [MatchDto.MatchResponseDto]
    )
    def patch(self, params=None):
        return self.service.game.addGuess(params), HttpStatus.OK


    @ControllerMethod(
        contextRequired = [MatchContext.USER],
        responseClass = [MatchDto.MatchResponseDto]
    )
    def post(self):
        return self.service.game.findOrCreateMatch(), HttpStatus.CREATED


    @ControllerMethod(
        contextRequired = [MatchContext.USER],
        responseClass = [MatchDto.MatchResponseDto]
    )
    def delete(self):
        return self.service.game.abandonMatch(), HttpStatus.DELETED
