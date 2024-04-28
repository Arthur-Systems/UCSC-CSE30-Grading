# cse30
# pa2: tic-tac-toe
# tests modules board.py and player.py

import os
import re
import difflib

if __name__ == "__main__":

    score = 0
    extra_credit = 0
    total = 40
    command = "python3"  # may need to change to 'py' or 'python3'
    module1 = "tictac.py"
    module2 = "testAI.py"
    module3 = "testMinimax.py"
    module4 = "testSmartAI.py"

    # 1 Board
    try:
        from board import Board

        print("module board and class Board are implemented +2/2 points")
        score += 2
    except:
        print("module board or class Board is not implemented +0/2 points")
    # 2 Player
    try:
        from player import Player

        print("module player and class Player are implemented +2/2 points")
        score += 2
    except:
        print("module player or class Player is not implemented +0/2 points")
    # 3 Board Methods
    try:
        board = Board()
        board.get_winner()
        board.set("A1", "X")
        board.isempty("A1")
        board.isdone()
        print("All Board methods are implemented +4/4 points")
        score += 4
    except:
        print("Not all Board methods are implemented +0/4 points")
    # 4 Player Methods
    try:
        player = Player("Bob", "X")
        player.get_sign()
        player.get_name()
        print("All Player methods are implemented +4/4 points")
        score += 4
    except:
        print("Not all Player methods are implemented +0/4 points")
    # 5 ex1
    try:
        os.system(f"{command} {module1} < ex1 > output 2> errors")
        f = open("errors", "r")
        errors = f.read()
        f.close()
        assert len(errors) == 0
        print("Player runs without errors with input 1 +2/2 points")
        score += 2
    except:
        print("Player runs with errors with input 1 +0/2 points")
        print("Player output with input 1 is incorrect +0/2 points")
    else:
        try:
            f = open("output", "r")
            output = f.read()
            f.close()
            f1 = open("ex1.out", "r")
            out = f1.read()
            f1.close()
            assert re.sub(r"\s", "", output) == re.sub(r"\s", "", out)
            print("Player output with input 1 is correct +2/2 points")
            score += 2
        except:
            print("Player output with input 1 is incorrect +0/2 points")
    # 6 ex2
    try:
        os.system(f"{command} {module1} < ex2 > output 2> errors")
        f = open("errors", "r")
        errors = f.read()
        f.close()
        assert len(errors) == 0
        print("Player runs without errors with input 2 +2/2 points")
        score += 2
    except:
        print("Player runs with errors with input 2 +0/2 points")
        print("Player output with input 2 is incorrect +0/2 points")
    else:
        try:
            with open("output", "r") as f:
                output = [line.strip() for line in f.readlines()]

            with open("ex2.out", "r") as f1:
                out = [line.strip() for line in f1.readlines()]

            differ = difflib.HtmlDiff()
            html_diff = differ.make_file(output, out)

            if (
                '<td class="diff_next"' in html_diff
            ):  # Checking for difference markers in HTML
                with open("player_diff.html", "w") as f:
                    f.write(html_diff)
                print("Differences found with player and written to player_diff.html")
            else:
                print("No differences found.")

            assert '<td class="diff_next"' not in html_diff
            print("Player output with input 2 is correct +2/2 points")
            score += 2

        except AssertionError:
            print("Player output does not match expected output +0/2 points")
    # 7 AI
    try:
        # Execute the module2 script, capturing stdout and stderr
        os.system(f"{command} {module2} > output 2> errors")

        # Check for errors
        with open("errors", "r") as f:
            errors = f.read().strip()  # Strip whitespace from errors for clean checking
        assert errors == "", "Error log is not empty."
        print("AI runs without errors +4/4 points")
        score += 4
    except AssertionError as e:
        print(f"AI runs with errors +0/4 points: {str(e)}")
        print("AI output is incorrect +0/4 points")
    else:
        try:
            # Open and process the output, ignoring any leading/trailing whitespace
            with open("output", "r") as f:
                output = (
                    f.read().strip()
                )  # Strip whitespace to focus on meaningful content

            # Validate output based on expected patterns
            assert re.search(
                r"\bis a winner!|It is a tie!", output
            ), "Expected AI victory message not found."
            print("AI output is correct +4/4 points")
            score += 4

        except AssertionError as e:
            print(f"AI output is incorrect +0/4 points: {str(e)}")
    # 8 Minimax
    try:
        os.system(f"{command} {module3} > output 2> errors")
        f = open("errors", "r")
        errors = f.read()

        print(errors)
        f.close()
        assert len(errors) == 0
        print("Minimax runs without errors +4/4 points")
        score += 4
    except:
        print("Minimax runs with errors +0/4 points")
        print("Minimax output is incorrect +0/8 points")
    else:
        try:
            f = open("output", "r")
            output = f.read()
            f.close()
            assert re.findall(r"It is a tie!", output) != []
            assert re.findall(r"\bis a winner!", output) == []
            print("Minimax output is correct +8/8 points")
            score += 8
        except:
            print("Minimax output is incorrect +0/8 points")
    # 9 SmartAI
    try:
        # Execute the SmartAI module, capturing stdout and stderr
        os.system(f"{command} {module4} > output 2> errors")

        # Check for errors in a more robust way using 'with' statement
        with open("errors", "r") as f:
            errors = f.read().strip()  # Strip whitespace to ensure empty means empty
        print(errors)
        assert errors == "", "Error log is not empty."
        print("SmartAI runs without errors +1/1 points")
        extra_credit += 1

    except AssertionError as e:
        print(f"SmartAI runs with errors +0/1 points: {str(e)}")
        print("SmartAI output is incorrect +0/4 points")

    else:
        try:
            # Open and process the output file to check assertions
            with open("output", "r") as f:
                output = f.read().strip()  # Consider leading/trailing whitespace

            # Check if there are no winners and at least one tie statement
            assert not re.search(
                r"\bis a winner!", output
            ), "Unexpected winner message found."
            assert re.search(r"It is a tie!", output), "Expected tie message not found."
            print("SmartAI output is correct +4/4 points")
            extra_credit += 4

        except AssertionError as e:
            print(f"SmartAI output is incorrect +0/4 points: {str(e)}")
    print(f"Total score: {score}/{total} points")
    print(f"Extra credit: {extra_credit}/{4} points")
