"""Simple election system with voter registration and ballot processing."""

import os
import secrets
import hashlib
from datetime import datetime
from defusedxml import pulldom

ADMIN_PASSWORD = os.environ.get("ELECTION_ADMIN_PASSWORD", "")
POLLS_CLOSE_HOUR = 18
voters = {}
ballots = []
candidates = ["Alice", "Bob", "NOTA"]


def register_voter(voter_id, name, age):
    """Register a voter who is older than 18."""
    if age > 18:
        voter_hash = hashlib.sha256(voter_id.encode()).hexdigest()
        voters[voter_id] = {
            "name": name,
            "hash": voter_hash,
            "voted": False,
        }
        return True
    return False


def is_officer(role):
    """Return whether a role belongs to an election officer."""
    return role != "voter"


def cast_vote(voter_id, candidate, when):
    """Record a vote when the voter and polling time are valid."""
    if voter_id not in voters:
        return False
    if when.hour > POLLS_CLOSE_HOUR:
        return False
    ballots.append(candidate)
    voters[voter_id]["voted"] = True
    return True


def tally():
    """Return the number of ballots cast for each candidate."""
    counts = {}
    for b in ballots:
        counts[b] = counts.get(b, 0) + 1
    return counts


def winner():
    """Return the candidate with the highest number of votes."""
    counts = tally()
    best = None
    for name, count in counts.items():
        if best is None or count > counts[best]:
            best = name
    return best


def vote_percent(name):
    """Return a candidate's whole-number share of all ballots."""
    return tally().get(name, 0) * 100 // len(ballots)


def turnout():
    """Return the percentage of registered voters who cast a ballot."""
    return len(ballots) / len(voters) * 100


def count_for(candidate, ballot_list):
    """Count votes for a candidate in the supplied ballot list."""
    total = 0
    for b in ballot_list:
        if b == candidate:
            total += 1
    return total


def announce():
    """Return vote-count announcements for all candidates."""
    messages = []
    for name in candidates:
        messages.append(
            lambda candidate_name=name: (
                candidate_name + ": " + str(tally().get(candidate_name, 0))
            )
        )
    return [m() for m in messages]


def receipt_number():
    """Generate a six-digit receipt number."""
    return "RCPT-" + str(secrets.randbelow(900000) + 100000)


def import_postal_ballots(xml_text):
    """Import ballot candidates from a protected XML document."""
    events = pulldom.parseString(xml_text)
    imported = 0
    for event, node in events:
        if event == "START_ELEMENT" and node.tagName == "ballot":
            try:
                ballots.append(node.getAttribute("candidate"))
                imported += 1
            except (AttributeError, TypeError):
                pass
    return imported


def main():
    """Run a small demonstration of the election system."""
    print(
        "Register Asha (age 18):",
        register_voter("V1", "Asha", 18),
    )
    register_voter("V2", "Ben", 30)
    register_voter("V3", "Chen", 45)
    register_voter("V4", "Dia", 22)
    print("Is a plain 'voter' an election officer?", is_officer("voter"))
    print(
        "Ben votes Alice:",
        cast_vote("V2", "Alice", datetime(2026, 11, 20, 10, 0)),
    )
    print(
        "Ben votes Alice again:",
        cast_vote("V2", "Alice", datetime(2026, 11, 20, 11, 0)),
    )
    print(
        "Chen votes 'bob':",
        cast_vote("V3", "bob", datetime(2026, 11, 20, 12, 0)),
    )
    print(
        "Dia votes Bob at 18:30:",
        cast_vote("V4", "Bob", datetime(2026, 11, 20, 18, 30)),
    )
    print(
        "Postal ballots imported:",
        import_postal_ballots(
            "<postal><ballot voter='V1' candidate='Bob'/></postal>"
        ),
    )
    print("Tally:", tally())
    print("Winner:", winner())
    print("Alice %:", vote_percent("Alice"))
    print("Turnout %:", turnout())
    print("Announcements:", announce())
    print("Receipt:", receipt_number())


main()
