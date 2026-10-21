from pathlib import Path

BASE = Path(__file__).parent



def load_settings(path):
    result = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line == "" or line.startswith("#"):
                continue
            pair = line.split("=", 1)
            result[pair[0]] = pair[1]
    return result

if __name__ == "__main__":
    s = load_settings(BASE / "settings.txt")
    print(s == {"domain": "test.ru", "min_length": "8", "max_length": "20"})
    print(int(s["min_length"]) == 8)