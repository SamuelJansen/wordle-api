from python_helper import log
from python_framework import HttpStatus, FlaskUtil
from queue_manager_api import MessageListener, MessageListenerMethod, MessageDto

from config import WordleQueueConfig


@MessageListener(
    timeout = WordleQueueConfig.LISTENER_TIMEOUT
    , muteLogs = False
    # , logRequest = True
    # , logResponse = True
)
class WordleListener:

    @MessageListenerMethod(url = '/listener/word',
        requestClass=[dict]
        # , logRequest = True
        # , logResponse = True
    )
    def acceptWord(self, dto):
        ###- {'wordList':[wordGuess]}
        for word in dto.get('wordList', []):
            self.service.word.createOrUpdateByText(word)
        return {}, HttpStatus.ACCEPTED


    @MessageListenerMethod(url = '/listener/guess',
        requestClass=[dict]
        # , logRequest = True
        # , logResponse = True
    )
    def acceptGuess(self, dto):
        ###- {'guess': wordGuess,'userId': match.user.id,'matchId': match.id}
        self.service.guessEvent.createModel(dto)
        return {}, HttpStatus.ACCEPTED
