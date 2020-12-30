#!/usr/bin/env python
# -*- coding: utf-8 -*-
from DoublyLinkedList import DoublyLinkedList
from Set import Set
from Ballot import Ballot

class Election:
    def __init__(self, candidates_file, ballots_file):
        self.eliminated = Set()

        # Parse candidates_file

        # Read data from file and store in DoublyLinkedList
        candidate_data = None
        with open(candidates_file, "r") as fp:
            candidate_data = DoublyLinkedList(fp.readlines())

        self.candidates = DoublyLinkedList(str)
        self.candidates.append("")

        self.candidates = DoublyLinkedList([None] + [info.split(",")[0] for info in candidate_data])

        # Parse ballots file
        ballots_data = None

        with open("ballots.csv", "r") as fp:
            ballots_data = DoublyLinkedList(fp.readlines())

        ballots = DoublyLinkedList([Ballot(line) for line in ballots_data])

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
        # Allocate the necessary space for the ballot sets
        self.ballots = DoublyLinkedList([Set() for i in range(self.candidates.size())])

        # Store ballots in the corresponding set where the candidate has a rank value of 1
        for ballot in ballots:
            if ballot.isInvalid():
                continue

            # Otherwise, we can process it and store it accordingly
            candidate = ballot.getCandidateByRank(1)
            if 0 < candidate and candidate < self.candidates.size():
                self.ballots[candidate].add(ballot)

    # Calculate the amount of votes a candidate received for a specific rank
    def calculate_amount_votes(self, considered_candidates, rank):
        amount_votes = DoublyLinkedList([0]*(self.candidates.size()))

        # Iterate through all the candidates
        for candidate in range(1, self.candidates.size()):
            # Iterate through subsets inside the candidates
            for ballot in self.ballots[candidate]:
                c = ballot.getCandidateByRank(rank)
                # Add to counter that this candidate had one vote for this rank
                if c > 0 and c in considered_candidates and not ballot.isInvalid():
                    amount_votes[c] += 1

        # Convert all 0's to None so the candidate's votes won't be considered later
        for i in range(amount_votes.size()):
            if amount_votes[i] == 0 and i not in considered_candidates:
                amount_votes[i] = None

        return amount_votes


    def determineWinner(self):
        file_message = f"Ballots Received: {self.ballots_received}\n"
        file_message += f"Blank Ballots: {self.blank_ballots}\n"
        file_message += f"Invalid Ballots: {self.invalid_ballots}\n"

        # This will help by using set operations in order to find which candidates will still be considered
        all_candidates = Set()
        for i in range(1, self.candidates.size()):
            all_candidates.add(i)

        round_number = 1
        winner_found = False

        while not winner_found:
            considered_candidates = all_candidates - self.eliminated

            # Phase 1: Check if candidate has more than 50% of 1s
            amount_1s = self.calculate_amount_votes(considered_candidates, 1)

            temp = amount_1s[:]
            temp.remove_all(None)
            total = sum(temp)

            for i in range(1, amount_1s.size()):
                if amount_1s[i] is not None and total // 2 < amount_1s[i]:
                    #  breakpoint()
                    print(f"Winner: {self.candidates[i]} wins with {amount_1s[i]} 1's")
                    file_message += f"Winner: {self.candidates[i]} wins with {amount_1s[i]} 1's\n"
                    winner_found = True
                    break

            if winner_found:
                break

            # Phase 2: Check which candidate will be eliminated

            # Prepare a list of candidates that are still being considered for being eliminated
            to_be_eliminated = DoublyLinkedList(range(1, self.candidates.size()))

            for el in self.eliminated:
                to_be_eliminated.remove(el)

            # Iterate through all k ranks until candidate is eliminated (will stop early if possible)
            for rank in range(1, self.candidates.size()):
                amount_per_rank = self.calculate_amount_votes(to_be_eliminated, rank)

                # Once the amount of votes per rank is determined, eliminate candidate with least
                # amount of votes

                # !!0th index!!
                considered_amounts = DoublyLinkedList()
                for candidate in to_be_eliminated:
                    considered_amounts.append(amount_per_rank[candidate])
                min_votes = min(considered_amounts)


                # If there are no repetitions as to which candidate has the least amount of votes
                # ... Eliminate!
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

                    print(f"Round #{round_number}: {self.candidates[candidate]} was eliminated with {amount_1s[candidate]} 1's")
                    file_message += f"Round #{round_number}: {self.candidates[candidate]} was eliminated with {amount_1s[candidate]} 1's\n"
                    break

                else:
                    # Only consider candidates that would have been eliminated this round for the tie breaker
                    for i in range(amount_per_rank.size()):
                        if amount_per_rank[i] != min_votes:
                            to_be_eliminated.remove(i)

            # If for every rank there is a tie, remove the candidate with the greatest id number
            if not eliminated_candidate:
                candidate = max(considered_candidates)

                self.eliminated.add(candidate)

                # Modify the ballots where the candidate being removed has a rank value of 1
                tempSet = Set()
                for el in self.ballots[candidate]:
                    el.eliminate(candidate)
                    tempSet.add(el)
                self.ballots[candidate] = tempSet

                eliminated_candidate = True

                print(f"Round #{round_number}: {self.candidates[candidate]} was eliminated with {amount_1s[candidate]} 1's")
                file_message += f"Round #{round_number}: {self.candidates[candidate]} was eliminated with {amount_1s[candidate]} 1's\n"

            round_number += 1

        with open("results.txt", "w+") as fp:
            fp.write(file_message)

                    



if __name__ == "__main__":
    example = Election("candidates.csv", "ballots.csv")
    example.determineWinner()
