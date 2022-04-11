from sqlalchemy.sql import func
from sqlalchemy.orm import load_only

from python_helper import ObjectHelper
from python_framework import SqlAlchemyProxy as sap
from python_framework import Repository

import Word


@Repository(model = Word.Word)
class WordRepository:

    def findAll(self) :
        return self.repository.findAllAndCommit(self.model)

    def existsById(self, id) :
        return self.repository.existsByIdAndCommit(id, self.model)

    def findById(self, id) :
        if self.existsById(id) :
            return self.repository.findByIdAndCommit(id, self.model)

    def notExistsById(self, id) :
        return not self.existsById(id)

    def save(self, model) :
        return self.repository.saveAndCommit(model)

    def saveAll(self, modelList):
        return self.repository.saveAllAndCommit(modelList)

    def deleteById(self, id):
        self.repository.deleteByIdAndCommit(id, self.model)

    def findAllByIdIn(self, idList) :
        modelList = self.repository.session.query(self.model).filter(self.model.id.in_(idList)).all()
        self.repository.session.commit()
        return modelList

    def findAllByTextIn(self, textList):
        modelList = self.repository.session.query(self.model).filter(self.model.text.in_(textList)).all()
        self.repository.session.commit()
        return modelList

    def getRandomWordList(self, amount, length):
        return self.repository.session.query(self.model).filter(self.model.length == length).order_by(func.random()).limit(amount).all()
