#!/usr/bin/env python
# -*- coding: utf-8 -*-
from DoublyLinkedList import DoublyLinkedList
from Set import Set
from Ballot import Ballot

class Election:
    def __init__(self, candidates_file, ballots_file):
        self.eliminated = Set(int)

        # Parse candidates_file

        # Read data from file and store in DoublyLinkedList
        candidate_data = DoublyLinkedList(str)
        with open(candidates_file, "r") as fp:
            for line in fp.readlines():
                candidate_data.append(line.strip())

        self.candidates = DoublyLinkedList(str)
        self.candidates.append("")

        for candidate_info in candidate_data:
            name = ""

            for j in range(len(candidate_info)):
                char = candidate_info[j]
                if char != ",":
                    name += char
                else:
                    break

            self.candidates.append(name)


        # Parse ballots file
        data = DoublyLinkedList(str)

        with open("ballots.csv", "r") as fp:
            for line in fp.readlines():
                data.append(line)

        ballots = DoublyLinkedList(type(Ballot))

        for line in data:
            ballots.append(Ballot(line))

        self.ballots_received = ballots.size()
        self.invalid_ballots = 0
        self.blank_ballots = 0

        for ballot in ballots:
            if ballot.isInvalid():
                self.invalid_ballots += 1

            if ballot.isBlank():
                self.blank_ballots += 1

        self.storeBallots(ballots)


    def storeBallots(self, ballots):
        self.ballots = DoublyLinkedList(Set)

        # Allocate the necessary space for the ballot sets
        for i in range(self.candidates.size()):
            self.ballots.append(Set(type(Ballot)))

        # Store ballots in the corresponding set where the candidate has a rank value of 1
        for ballot in ballots:
            if ballot.isInvalid():
                continue

            # Othewise, we can process it and store it accordingly
            candidate = ballot.getCandidateByRank(1)

            # Somehow the Set "forgets" its datatype, so I have to repeat it. Otherwise I get an error
            self.ballots[candidate].dataType = type(Ballot)

            self.ballots[candidate].add(ballot)


    def determineWinner(self):
        # This will help by using set operations in order to find which candidates will still be considered
        all_candidates_set = Set(int)
        for i in range(len(self.candidates)):
            all_candidates_set.add(i + 1)

        round_number = 1
        winner_found = False
        while not winner_found:
            frequency = DoublyLinkedList(type(DoublyLinkedList(int)))

            # Add a dummy for the 0th index
            frequency.append(DoublyLinkedList(int))

            # Iterate through all the candidates
            for i in range(1, self.ballots.size()):
                ballot_set = self.ballots[i]
                # Criteria 1: Check if candidate has more than 50% of 1s
                if ballot_set.size() // 2 > (self.ballots_received - self.invalid_ballots):
                    print(f"Round #{round_number}: {self.candidates[i]} wins with {self.ballots[i].size()} 1's")
                    winner_found = True
                    break

                # Criteria 2: Check for the person with least amount of ones
                else:
                    amountsByRank = DoublyLinkedList(int)
                    
                    for j in range(self.candidates.size()):
                        amountsByCandidate.append(0)

                    for el in ballot_set:
                            amountsByCandidate[j] = el.getRankByCandidate(j)








            
            round_number += 1
                    
                    







if __name__ == "__main__":
    example = Election("candidates.csv", "ballots.csv")
    example.determineWinner()
