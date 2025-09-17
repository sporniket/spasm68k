from spasm68k.models import LineOfCode, LineOfCodeLoader


def test_that_it_WILL_load_lines_of_codes():
    testSource = "tests/data/read_lines_of_codes.txt"
    expectedContent = [
        "Lorem ipsum dolor sit amet,\n",
        "consectetur adipiscing elit.\n",
        "Aliquam justo erat, fermentum in mi ut,\n",
        "venenatis tincidunt felis.\n",
    ]
    locs = LineOfCodeLoader().read(testSource)

    assert len(locs) == 4
    for i, loc in enumerate(locs):
        assert loc.sourceFile == testSource
        assert loc.lineNumber == i
        assert loc.content == expectedContent[i]
