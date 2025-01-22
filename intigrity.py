import os
import hashlib
import json

class FileIntegrityChecker:
    def __init__(self, directory, hash_file="file_hashes.json", hash_algorithm="sha256"):
        self.directory = directory
        self.hash_file = hash_file
        self.hash_algorithm = hash_algorithm
        self.hashes = {}

    def load_hashes(self):
        """Load hash values from the hash file."""
        if os.path.exists(self.hash_file):
            with open(self.hash_file, "r") as f:
                self.hashes = json.load(f)

    def save_hashes(self):
        """Save the current hash values to the hash file."""
        with open(self.hash_file, "w") as f:
            json.dump(self.hashes, f, indent=4)

    def calculate_hash(self, file_path):
        """Calculate the hash of a file using the specified algorithm."""
        hash_func = hashlib.new(self.hash_algorithm)
        with open(file_path, "rb") as f:
            while chunk := f.read(8192):
                hash_func.update(chunk)
        return hash_func.hexdigest()

    def scan_files(self):
        """Scan all files in the directory and compute their hashes."""
        for root, _, files in os.walk(self.directory):
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, self.directory)
                self.hashes[relative_path] = self.calculate_hash(file_path)

    def check_integrity(self):
        """Check for changes in file integrity."""
        self.load_hashes()
        current_hashes = {}
        changes = {
            "modified": [],
            "new": [],
            "deleted": []
        }

        for root, _, files in os.walk(self.directory):
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, self.directory)
                current_hashes[relative_path] = self.calculate_hash(file_path)

                if relative_path not in self.hashes:
                    changes["new"].append(relative_path)
                elif self.hashes[relative_path] != current_hashes[relative_path]:
                    changes["modified"].append(relative_path)

        for relative_path in self.hashes:
            if relative_path not in current_hashes:
                changes["deleted"].append(relative_path)

        self.hashes = current_hashes
        self.save_hashes()

        return changes

if __name__ == "__main__":
    directory_to_monitor = input("Enter the directory to monitor: ").strip()
    checker = FileIntegrityChecker(directory_to_monitor)

    print("\nScanning files and saving initial hashes...")
    checker.scan_files()
    checker.save_hashes()
    print("Initial scan complete. Hashes saved.\n")

    while True:
        action = input("Enter 'check' to monitor changes or 'exit' to quit: ").strip().lower()
        if action == "check":
            changes = checker.check_integrity()
            print("\nChanges detected:")
            print(f"Modified: {changes['modified']}")
            print(f"New: {changes['new']}")
            print(f"Deleted: {changes['deleted']}\n")
        elif action == "exit":
            print("Exiting the program.")
            break
        else:
            print("Invalid command. Try again.")

