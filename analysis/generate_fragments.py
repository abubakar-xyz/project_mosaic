"""
generate_fragments.py — Fragment generation pipeline for Project MOSAIC.

Runs each evasion_trial script with the GFP wild-type sequence as input,
parses the output (handling each script's unique I/O format), and writes
clean fragment files. Does NOT modify the evasion trial scripts.

Usage (from project root):
    python analysis/generate_fragments.py
"""
import sys
import subprocess
import re
import os

# Resolve paths relative to project root
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(PROJECT_ROOT, 'data')
TRIALS_DIR = os.path.join(PROJECT_ROOT, 'evasion_trials')
FRAGMENTS_DIR = os.path.join(PROJECT_ROOT, 'fragments')

with open(os.path.join(DATA_DIR, 'gfp_wildtype.txt'), 'r') as f:
    sequence = f.read().replace('\n', '').replace('\r', '').strip()

for i in range(1, 10):
    script = os.path.join(TRIALS_DIR, f'evasion_trial{i}.py')
    out_file = os.path.join(FRAGMENTS_DIR, f'fragments_trial{i}.txt')

    print(f"Processing evasion_trial{i}.py...")

    if i == 9:
        # Trial 9 has no __main__ block; import and call directly
        sys.path.insert(0, TRIALS_DIR)
        import evasion_trial9
        fragments = evasion_trial9.process_string(sequence)
        sys.path.pop(0)
        with open(out_file, 'w') as f:
            for frag in fragments:
                f.write(frag + '\n')
        continue

    # For 1-8, run as a subprocess
    process = subprocess.Popen(
        [sys.executable, script],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    stdout, stderr = process.communicate(input=sequence + '\n')

    # Process the stdout to extract only fragments
    fragments = []

    # Different parsing based on the script's known output format
    if i in [1, 3, 4, 6, 7]:
        # They just print fragments line by line
        for line in stdout.splitlines():
            line = line.strip()
            if line:
                fragments.append(line)
    elif i == 2:
        # Fragment {i}: {fragment}
        for line in stdout.splitlines():
            m = re.search(r'Fragment \d+: (.*)', line)
            if m:
                fragments.append(m.group(1).strip())
    elif i == 5:
        # Fragment {i} (150 chars): {fragment}
        for line in stdout.splitlines():
            m = re.search(r'Fragment \d+ \(\d+ chars\): (.*)', line)
            if m:
                fragments.append(m.group(1).strip())
    elif i == 8:
        # Fragment {idx}:
        # {fragment}
        # Note: Line 0 is "Enter the string to obfuscate: Fragment 1:" so we
        # must check 'Fragment' anywhere in the line, not just startswith.
        lines = stdout.splitlines()
        for idx, line in enumerate(lines):
            line_stripped = line.strip()
            if 'Fragment' in line_stripped:
                if idx + 1 < len(lines):
                    frag = lines[idx+1].strip()
                    if frag:
                        fragments.append(frag)

    with open(out_file, 'w') as f:
        for frag in fragments:
            f.write(frag + '\n')

print("Done generating fragments.")
