import os
import sys
import hashlib


def file_hash(filename):
    h = hashlib.sha256()
    with open(filename, 'rb', buffering=0) as f:
        for b in iter(lambda: f.read(128 * 1024), b''):
            h.update(b)
    return h.hexdigest()


def dup_files(main_folder):
    seen_hashes = {}
    dire_stack = [main_folder]
    duplicates = []

    while dire_stack:
        current_path = dire_stack.pop()
        if os.path.isdir(current_path):
            for path in os.listdir(current_path):
                full_path = os.path.join(current_path, path)
                dire_stack.append(full_path)
        else:
            file_hsh = file_hash(current_path)
            clet = os.path.getmtime(current_path)
            if file_hsh in seen_hashes:
                elet, ep = seen_hashes[file_hsh]
                if clet > elet:
                    duplicates.append((current_path, ep))
                else:
                    duplicates.append((ep, current_path))
                    seen_hashes[file_hsh] = (clet, current_path)
            else:
                seen_hashes[file_hsh] = (clet, current_path)
    return duplicates

if __name__ == '__main__':
    print(dup_files("//home//yashwanth//Desktop//Main"))
