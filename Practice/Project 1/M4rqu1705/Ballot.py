#!/usr/bin/env python
# -*- coding: utf-8 -*-
from DoublyLinkedList import DoublyLinkedList

class Ballot:
    def __init__(self, text):
        self.number = 0
        self.invalid = False
        self.blank = False

        # Parsing line of text
        data = DoublyLinkedList(text.strip().lower().split(","))
            
        self.number = int(data[0])


        self.votes = DoublyLinkedList(data.size())

        for el in data[1:]:
            candidate, rank = el.split(":")
            self.votes[int(candidate)] = int(rank)

        # Validate ballots
        k = data.size() - 1

        for el in self.votes[1:]:
            # Ranking value must be within 1 to k
            if el > k or el < 0:
                #  raise ValueError("Invalid Balot: Discontinuous ranks")
                self.invalid = True

            # There are duplicate ranks
            if self.votes.index(el) != self.votes.last_index(el) and el != 0:
                #  raise ValueError("Invalid Ballot: Duplicate ranks")
                self.invalid = True

            # If every ranking in the ballot is 0, or there are no votes then it is blank
            if self.votes[:].remove_all(0) == self.votes.size() or self.votes.size() == 0:
                self.blank = True


    def getBallotNum(self):
        return self.number

    def getRankByCandidate(self, candidate):
        return self.votes[candidate]

    def getCandidateByRank(self, rank):
        return self.votes.index(rank)

    def eliminate(self, candidate):
        rank = self.getRankByCandidate(candidate)

        # "Move up" higher-ranked candidates up one position
        for i in range(self.votes.size()):
            if self.votes[i] is not None and self.votes[i] > rank:
                self.votes[i] -= 1

        self.votes[candidate] = 0

    def isInvalid(self):
        return self.invalid

    def isBlank(self):
        return self.blank
    
    def __str__(self):
        return f'#{self.getBallotNum()} -> {self.votes}'

    def __repr__(self):
        return f'#{self.getBallotNum()} -> {self.votes}'


if __name__ == "__main__":
    breakpoint()
