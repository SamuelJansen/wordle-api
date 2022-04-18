from python_framework import Controller, ControllerMethod, HttpStatus

from enumeration.MatchContext import MatchContext
from dto import WordGuessDto, MatchDto


@Controller(url='/match', tag='Match', description='Match controller')
class MatchController:

    @ControllerMethod(url = '/verify',
        requestParamClass = WordGuessDto.WordGuessRequestParamDto,
        contextRequired = [MatchContext.USER],
        responseClass = [MatchDto.MatchResponseDto]
        , logRequest = True
        , logResponse = True
    )
    def patch(self, params=None):
        return self.service.game.addGuess(params), HttpStatus.OK


    @ControllerMethod(
        contextRequired = [MatchContext.USER],
        responseClass = [MatchDto.MatchResponseDto]
        , logRequest = True
        , logResponse = True
    )
    def post(self):
        return self.service.game.findOrCreateMatch(), HttpStatus.CREATED


    @ControllerMethod(
        contextRequired = [MatchContext.USER],
        responseClass = [MatchDto.MatchResponseDto]
        , logRequest = True
        , logResponse = True
    )
    def delete(self):
        return self.service.game.abandonMatch(), HttpStatus.DELETED
