import hashlib
import os
import sys


def file_hash(filepath):
	"""Generate a hash for a file."""
	hasher = hashlib.sha256()
	with open(filepath, 'rb') as f:
		buf = f.read()
		hasher.update(buf)
	return hasher.hexdigest()


def scan_directories(directory_list):
	"""Scan directories for copied files based on file hashes."""
	hashes = {}
	copied_files = {}

	for directory in directory_list:
		for subdir, dirs, files in os.walk(directory):
			for file in files:
				filepath = os.path.join(subdir, file)
				filehash = file_hash(filepath)
				if filehash in hashes:
					copied_files.setdefault(filehash, []).append(filepath)
				else:
					hashes[filehash] = filepath

	return copied_files


def main():
	if len(sys.argv) < 2:
		print("Usage: python check_copies.py <directory1> <directory2> ...")
		sys.exit(1)

	directory_list = sys.argv[1:]
	copied_files = scan_directories(directory_list)

	if copied_files:
		print("Copied files found:")
		for hash_val, files in copied_files.items():
			print(f"Files with hash {hash_val}:")
			for f in files:
				print(f" - {f}")
	else:
		print("No copied files found.")


if __name__ == "__main__":
	main()
