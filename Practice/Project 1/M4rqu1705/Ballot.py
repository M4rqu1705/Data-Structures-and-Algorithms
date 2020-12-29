#!/usr/bin/env python
# -*- coding: utf-8 -*-
from DoublyLinkedList import DoublyLinkedList
from Set import Set

class Ballot:
    def __init__(self, text):
        self.number = 0
        self.votes = DoublyLinkedList(int)
        self.invalid = False
        self.blank = False

        # Parsing line of text
        text = text.strip().lower()

        data = DoublyLinkedList(str)
        buff = ""
        for char in text:
            if char != ",":
                buff += char
            else:
                data.append(buff)
                buff = ""
        data.append(buff)
            
        self.number = int(data[0])

        for i in range(data.size() - 1):
            self.votes.append(0)

        for el in data[1:]:
            candidate, rank = el.split(":")
            self.votes[int(candidate)] = int(rank)


        # Validate ballots
        k = len(data) - 1

        for el in self.votes:
            # Ranking value must be within 1 to k
            if el > k or el < 0:
                #  raise ValueError("Invalid Balot: Discontinuous ranks")
                self.invalid = True

            # There are duplicate ranks
            if self.votes.index(el) != self.votes.last_index(el) and el != 0:
                #  raise ValueError("Invalid Ballot: Duplicate ranks")
                self.invalid = True

            # If there are more than one zeros in the ballot, then it is blank
            if self.votes.last_index(0) != 0:
                self.blank = True



    def getBallotNum(self):
        return self.number

    def getRankByCandidate(self, candidate):
        return self.votes[candidate]

    def getCantidateByRank(self, rank):
        return self.votes.index(rank)

    def eliminate(self, candidate):
        rank = self.getRankByCandidate(candidate)

        # "Move up" higher-ranked candidates up one position
        for i in range(self.votes.size()):
            if self.votes[i] > rank:
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
    # Read data from file and store in DoublyLinkedList
    data = DoublyLinkedList(str)

    with open("ballots.csv", "r") as fp:
        for line in fp.readlines():
            data.append(line)

    ballots = DoublyLinkedList(Set)

    # Allocate the necessary space for the ballot sets
    for i in range(6):
        ballots.append(Set(type(Ballot)))

    total_ballots = data.size()
    added_ballots = 0
    # Store ballots in the corresponding set where the candidate has a rank value of 1
    for i in range(ballots.size()):
        candidate = i + 1

        j = 0
        while j < data.size():
            ballot = Ballot(data[j])
            if ballot.getRankByCandidate(candidate) == 1 and not ballot.invalid:
                # Somehow the Set "forgets" its datatype, so I have to repeat it. Otherwise I get an error
                ballots[candidate].dataType = type(Ballot)

                ballots[candidate].add(ballot)

                # There is no need to check this ballot again, so we can delete it
                data.delete(j)

                added_ballots += 1
            else:
                j += 1

    print(ballots)
