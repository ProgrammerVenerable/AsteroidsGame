from constants import FILE

def load_score(file):
    with open(file) as f:
        file_contents = f.read()

    return file_contents

def change_score(current_score, file):
    with open(file, "w") as f:
        f.write(str(current_score))

def check_highscore(current_score, file):
    highscore = int(load_score(file))
    if current_score > highscore:
        return True

    return False
