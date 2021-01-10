#!/usr/bin/env python
# -*- coding: utf-8 -*-
from DoublyLinkedList import DoublyLinkedList
from Set import Set
from Ballot import Ballot

# Helps with the annotations
from typing import Collection, List, NoReturn

class Election:
    '''Main program for project 1

    Reads data from files and prepares and stores list of sets of ballots. Then, it can determine
    the winner of the

    Attributes:
       eliminated(Set): Contains ids of candidates that were eliminated on previous rounds
       candidates(DoublyLinkedList): Contains list of candidate names using their ids as indices for the list
       ballots_received(int): Stores the total amount of ballots received (includes blank and
          invalid ballots)
       invalid_ballots(int): Stores the amount of invalid ballots
       blank_ballots(int): Stores the amount of blank ballots
       ballots(DoublyLinkedList[Set[Ballot]]): Stores ballots in sets inside a list. Each set will contain
          ballots that have the same candidate with rank #1. The specific candidate that has #1
          across all ballots in that set will be indicated by the set's position within the
          ballot's list. The index corresponds to the candidate's id
    '''
    def __init__(self, candidates_file: str, ballots_file: str) -> NoReturn:
        '''Extract data from ballots and candidate files

        See :py:meth:`Election.Election.parse_candidate_file` and
        :py:meth:`Election.Election.parse_ballot_file` for more details as to
        how this data is processed

        Args:
           candidates_file(str): File from which candidate data will be extracted
           ballots_file(str): File from which ballots data will be extracted

        '''
        self.eliminated = Set()

        self.parse_candidate_file(candidates_file)

        self.parse_ballot_file(ballots_file)


    def parse_candidate_file(self, file_name: str) -> NoReturn:
        '''Receives candidates file and extracts and stores candidate names in list

        The index where each candidate is stored corresponds to that specific candidate's id

        Args:
           file_name(str): Name of the CSV file where the candidate names and ids are stored

        Note:
           The format is as follows:
              - Candidate1 Name, 1
              - Candidate2 Name, 2
              - ...
        '''

        with open(file_name, "r") as fp:
            candidate_data = DoublyLinkedList(fp.readlines())

            # Make the candidates list with enough space to fit all candidates from file and index 0 as None
            self.candidates = DoublyLinkedList(candidate_data.size() + 1)

            for candidate in candidate_data:
                # Extract name and candidate id from a specific line
                name, candidate_id = candidate.split(",")
                self.candidates[int(candidate_id)] = str(name).strip()


    def parse_ballot_file(self, file_name: str) -> NoReturn:
        '''Receives ballots file and extracts and stores ballots in list of sets

        Each line of the ballots file will contain only 1 ballot number followed by its fotes. After
        interpreting the ballots, each ballot is stored in a list of sets. Each ballot in a set in the list
        belongs to the candidate that has rank #1 within that ballot.

        Args:
           file_name(str): Name of the CSV file where the ballot number and votes are stored

        Note:
           The format is as follows:
              - ballot_number_1,candidate:1,candidate:2,...,candidate:k
              - ballot_number_2,candidate:1,candidate:2,...,candidate:k
              - ...
        '''


        with open(file_name, "r") as fp:
            # Use list comprehension to interpret line by line of the ballots file with help from
            # the Ballot class. Initially store all ballots in monolithic list
            ballots = DoublyLinkedList([Ballot(line) for line in fp.readlines()])

            # Initialize some ballots statistics
            self.ballots_received = ballots.size()
            self.invalid_ballots = 0
            self.blank_ballots = 0

            # Generate enough sets to later reorganize the ballots based on candidate that has rank #1
            self.ballots = DoublyLinkedList([Set() for i in range(self.candidates.size())])

            for ballot in ballots:
                if ballot.isBlank():
                    self.blank_ballots += 1

                # Ignore invalid ballots
                if ballot.isInvalid():
                    self.invalid_ballots += 1
                    continue

                # Otherwise, we can process ballot and store it accordingly
                candidate = ballot.getCandidateByRank(1)
                if 0 < candidate and candidate < self.candidates.size():
                    self.ballots[candidate].add(ballot)


    def calculate_amount_votes(self, considered_candidates: Collection[int], rank: int) -> List[int]:
        '''Helper function that calculates the amount of votes considered candidates have for a particular rank

        Args:
           considered_candidates(set[int]): The candidate ids for the candidates that are still
              being considered for the election (i.e. they have not been eliminated)
           rank(int): The particular rank we want to count votes for

        Returns:
           amount_votes(list[int]): List of votes for each candidate for this particular rank
        '''

        amount_votes = DoublyLinkedList([0]*(self.candidates.size()))

        # Iterate through all the candidates' sets
        for candidate in range(1, self.candidates.size()):

            # Iterate through subsets inside the candidates
            for ballot in self.ballots[candidate]:
                c = ballot.getCandidateByRank(rank)

                # Add to counter that this candidate had one vote for this rank and ballot is not invalid
                if c > 0 and c in considered_candidates and not ballot.isInvalid():
                    amount_votes[c] += 1

        # Convert all 0's to None so the candidate's votes won't be considered later
        for i in range(amount_votes.size()):
            if amount_votes[i] == 0 and i not in considered_candidates:
                amount_votes[i] = None

        return amount_votes


    def determineWinner(self) -> NoReturn:
        '''Determine election winner in by eliminating candidates until one has over 50% of #1 votes

        Consists of multiple rounds of elimination where if a candidate does not have over 50% of #1
        votes, a candidate will be eliminated. The candidate with the least amount of votes for rank
        #1 will be eliminated. If there's a tie, the candidate with the least amount of votes for
        rank #2 will be eliminated. etc.
        '''

        # Prepare basic information we already have for the result message
        file_message = f"Ballots Received: {self.ballots_received}\n"
        file_message += f"Blank Ballots: {self.blank_ballots}\n"
        file_message += f"Invalid Ballots: {self.invalid_ballots}\n"


        # This set will help to find which candidates will still be considered
        all_candidates = Set(range(1, self.candidates.size()))

        round_number = 1        # Round counter
        winner_found = False    # winner_found flag which will end elimination while loop

        while not winner_found:
            # The considered candidates is the subset of all candidates that are not eliminated
            considered_candidates = all_candidates - self.eliminated

            # Phase 1: Check if a candidate has more than 50% of 1s
            amount_1s = self.calculate_amount_votes(considered_candidates, 1)

            temp = amount_1s[:]
            temp.remove_all(None)
            total = sum(temp)

            for i in range(1, amount_1s.size()):
                if amount_1s[i] is not None and total // 2 < amount_1s[i]:
                    file_message += f"Winner: {self.candidates[i]} wins with {amount_1s[i]} 1's\n"
                    winner_found = True
                    break

            if winner_found:
                break

            # Phase 2: Check which candidate will be eliminated

            # Prepare a list of candidates that are still being considered for being eliminated.
            # The difference between this list and the set is that lists preserve the order, which
            #   is important in order to identify the candidate ids.
            to_be_eliminated = DoublyLinkedList(range(1, self.candidates.size()))

            for el in self.eliminated:
                to_be_eliminated.remove(el)

            # Flag to check if the loop effectively eliminated a candidate
            eliminated_candidate = False

            # Iterate through all k ranks until one candidate is eliminated (will stop early if possible)
            for rank in range(1, self.candidates.size()):
                amount_per_rank = self.calculate_amount_votes(to_be_eliminated, rank)

                # Once the amount of votes per rank is determined, eliminate candidate with least
                # amount of votes

                # Reminder: !!0th index!!
                considered_amounts = DoublyLinkedList()
                for candidate in to_be_eliminated:
                    considered_amounts.append(amount_per_rank[candidate])
                min_votes = min(considered_amounts)


                # If there are NO REPETITIONS as to which candidate has the least amount of votes ... Eliminate!
                if considered_amounts.index(min_votes) == considered_amounts.last_index(min_votes):
                    candidate = to_be_eliminated[considered_amounts.index(min_votes)]

                    self.eliminated.add(candidate)

                    # Modify the ballots where the candidate being removed has a rank value of 1
                    tempSet = Set()
                    for el in self.ballots[candidate]:
                        el.eliminate(candidate)
                        tempSet.add(el)
                    self.ballots[candidate] = tempSet

                    eliminated_candidate = True

                    file_message += f"Round #{round_number}: {self.candidates[candidate]} was eliminated with {amount_1s[candidate]} 1's\n"
                    break

                else:
                    # Only consider candidates that would have been eliminated this round for the tie breaker
                    for i in range(amount_per_rank.size()):
                        if amount_per_rank[i] != min_votes:
                            to_be_eliminated.remove(i)

            # If for every rank there is a tie, remove the candidate with the greatest id number
            if not eliminated_candidate:
                candidate = max(to_be_eliminated)

                self.eliminated.add(candidate)

                # Modify the ballots where the candidate being removed has a rank value of 1
                tempSet = Set()
                for el in self.ballots[candidate]:
                    el.eliminate(candidate)
                    tempSet.add(el)
                self.ballots[candidate] = tempSet

                file_message += f"Round #{round_number}: {self.candidates[candidate]} was eliminated with {amount_1s[candidate]} 1's\n"

            round_number += 1

        with open("results.txt", "w+") as fp:
            fp.write(file_message)
            print(file_message)



if __name__ == "__main__":
    example = Election("candidates.csv", "ballots.csv")
    example.determineWinner()
