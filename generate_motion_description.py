import random
import re

BASIC_MOTIONS_FILE = "basic_motions.txt"
PACE_CATEGORIES = [
    "static",
    "slow",
    "medium",
    "fast"
]


def load_basic_motions(path):
    """Parse the basic_motions.txt file into a dictionary.
    Returns {part_name: [motion1, motion2, ...], ...}
    """
    motions = {}
    current_part = None
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.endswith(":"):
                current_part = line[:-1]
                motions[current_part] = []
            else:
                # assume a numbered list or bullet not needed
                # remove leading number/"," or dash
                cleaned = re.sub(r"^\d+\.\s*", "", line)
                cleaned = re.sub(r"^[-]\s*", "", cleaned)
                motions[current_part].append(cleaned)
    return motions


def random_description(motions_dict):
    """Generate a random description string picking one motion per part with random pace."""
    parts = list(motions_dict.keys())
    lines = []
    for part in parts:
        choices = motions_dict[part]
        if not choices:
            continue
        motion = random.choice(choices)
        pace = random.choice(PACE_CATEGORIES)
        lines.append(f"{part}: {motion} (pace: {pace})")
    return "\n".join(lines)


def main():
    motions = load_basic_motions(BASIC_MOTIONS_FILE)
    desc = random_description(motions)
    print("Random motion description:\n")
    print(desc)


if __name__ == "__main__":
    main()
