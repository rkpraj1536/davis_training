# Question 6: Voting System with Duplicate Check

votes = ["A", "B", "A", "C", "B", "A"]
vote_count = {}
seen = set()

for vote in votes:
    if vote not in seen:
        seen.add(vote)
        vote_count[vote] = vote_count.get(vote, 0) + 1

winner = max(vote_count, key=vote_count.get)
print(vote_count)
print("Winner:", winner)
