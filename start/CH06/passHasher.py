#!/usr/bin/env python3
# Script that hashes a password
#By Harel Boyenge

# Sample data
# Password: Password01
# Salt: G.DTW7g9s5U7KYf5
# SHA-512 result: $6$G.DTW7g9s5U7KYf5$xTXAbS1Q30hfd10VDbkSh5adZMxbqRUMOyNyKopfFpMvD.Vf/CcoEBn/TUYcfJ1jAaEiJPBf/PoCLFq7U7Q7p.

import argparse
import os
import sys

# try to import passlib and give a helpful error if missing
try:
    from passlib.hash import sha512_crypt
except Exception as e:
    print("[ERROR] passlib is required but not installed.")
    print("Install it with: python3 -m pip install --user passlib")
    # if running inside a venv just do: pip install passlib
    raise

def parse_args():
    p = argparse.ArgumentParser(description="Simple SHA512 shadow dictionary cracker")
    p.add_argument("shadow", nargs="?", default="shadow", help="path to shadow file (default: shadow)")
    p.add_argument("wordlist", nargs="?", default="top1000.txt", help="path to wordlist (default: top1000.txt)")
    return p.parse_args()

def load_shadow_lines(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return [line.rstrip("\n\r") for line in f if line.strip()]

def load_wordlist(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return [w.rstrip("\n\r") for w in f if w.strip()]

def extract_user_and_hash(shadow_line):
    parts = shadow_line.split(":")
    if len(parts) < 2:
        return None, None
    user = parts[0]
    pwdfield = parts[1]
    # skip locked/disabled accounts
    if pwdfield in ("!", "*", "!!") or pwdfield.strip() == "":
        return user, None
    return user, pwdfield

def crack(shadow_path, wordlist_path):
    if not os.path.isfile(shadow_path):
        raise FileNotFoundError(f"shadow file not found: {shadow_path}")
    if not os.path.isfile(wordlist_path):
        raise FileNotFoundError(f"wordlist not found: {wordlist_path}")

    shadows = load_shadow_lines(shadow_path)
    words = load_wordlist(wordlist_path)
    cracked = []

    print(f"[+] shadow lines: {len(shadows)} | wordlist candidates: {len(words)}")

    for line in shadows:
        user, pwfield = extract_user_and_hash(line)
        if not user or not pwfield:
            continue
        print(f"[*] Trying user: {user}")
        for candidate in words:
            try:
                if sha512_crypt.verify(candidate, pwfield):
                    print(f"[CRACKED] {user} -> {candidate}")
                    cracked.append((user, candidate))
                    break
            except Exception:
                # malformed hash or unsupported - skip
                continue

    # save results
    out_path = "cracked.txt"
    with open(out_path, "w", encoding="utf-8") as out:
        for u, pw in cracked:
            out.write(f"{u}:{pw}\n")
    print(f"[+] done. cracked {len(cracked)} users. saved -> {out_path}")
    return out_path

if __name__ == "__main__":
    args = parse_args()
    try:
        cracked_file = crack(args.shadow, args.wordlist)
    except FileNotFoundError as e:
        print("[ERROR]", e)
        print("Make sure you run this from the folder where the shadow file and the wordlist are, or pass full paths.")
        sys.exit(1)
