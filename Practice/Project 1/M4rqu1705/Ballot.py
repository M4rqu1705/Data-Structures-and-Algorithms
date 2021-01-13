#!/usr/bin/env python
# -*- coding: utf-8 -*-
from DoublyLinkedList import DoublyLinkedList

# Helps with the annotations
from typing import NoReturn

'''Class that stores ballot information

Stores all of the information regarding a single ballot. Receives the line of text
from the input file from which the ballot information is extracted and stored

Votes information is stored in a list. The 0th index is not used, but from the 1st
index forward each position corresponds to a specific candidate and the value
stored in that position is this ballot's rank for that particular candidate

Attributes:
   number(int): Stores the ballot number; basically its own id
   invalid(bool): Indicates if the ballot is invalid or not
   blank(bool): Indicates if the ballot is blank or not
   votes(list): Stores the ranks selected for each candidate based on index

'''
class Ballot:
    def __init__(self, text: str) -> NoReturn:
        '''Constructor for Ballot class

        Processes and parses text in order to extract the relevant information
        and store it in a Doubly-Linked List. Additionally initializes
        attributes and determines if vote is blank or invalid

        Args:
          text(str): Line of the ballots.csv from which votes and ballot number
             will be extracted
        '''

        # INITIALIZE SOME ATTRIBUTES
        self.number = 0
        self.invalid = False
        self.blank = False

        # PARSE LINE OF TEXT
        data = DoublyLinkedList(text.strip().lower().split(","))

        self.number = int(data[0])

        self.votes = DoublyLinkedList(data.size())

        for el in data[1:]:
            candidate, rank = el.split(":")
            self.votes[int(candidate)] = int(rank)

        # VALIDATE BALLOTS
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


    def getBallotNum(self) -> int:
        '''Return ballot number

        Returns:
          number(int): Ballot number (which serves as an id)
        '''

        return self.number


    def getRankByCandidate(self, candidate: int) -> int:
        '''Return the rank of the specified candidate

        Args:
           candidate(int): Id number of the candidate whose rank we want to check

        Returns:
           rank(int): The corresponding candidate's rank
        '''

        return self.votes[candidate]


    def getCandidateByRank(self, rank: int) -> int:
        '''Return the candidate that has the specified rank

        Args:
           rank(int): Specific rank we want to look fro

        Returns:
           candidate(int): Candidate that has this rank
        '''

        return self.votes.index(rank)


    def eliminate(self, candidate: int) -> NoReturn:
        '''Eliminates specific candidate from ballot

        First elimintes the candidate and then increases lower candidate's ranks.
        This way the next iterations will have the most up to date data

        Args:
           candidate(int): Id of the candidate that will be eliminated
        '''
        rank = self.getRankByCandidate(candidate)

        # "Move up" higher-ranked candidates up one position
        for i in range(self.votes.size()):
            if self.votes[i] is not None and self.votes[i] > rank:
                self.votes[i] -= 1

        self.votes[candidate] = 0

    def isInvalid(self) -> bool:
        '''Getter method for `invalid` attribute

        Returns:
           invalid(bool): If this ballot is valid or not
        '''

        return self.invalid

    def isBlank(self) -> bool:
        '''Getter method for `blank` attribute

        Returns:
            blank(bool): If this ballot is blank or not
        '''

        return self.blank

    def __str__(self) -> str:
        '''Returns string representation that helps visualize a summary of this ballot

        Returns:
            message(str): Ballot number followed by the list of votes
        '''

        return f'#{self.getBallotNum()} -> {self.votes}'

    def __repr__(self) -> str:
        '''Returns string representation that helps visualize a summary of this ballot

        Returns:
            message(str): Ballot number followed by the list of votes
        '''

        return f'#{self.getBallotNum()} -> {self.votes}'


if __name__ == "__main__":
    breakpoint()
