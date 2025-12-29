import os
import re

README_FILE = "README.md"

START_MARKER = "<!-- DAILY_PROGRESS_START -->"
END_MARKER = "<!-- DAILY_PROGRESS_END -->"


def get_latest_day():
    days = []

    for folder in os.listdir("."):
        match = re.match(r"[Dd]ay[\s\-_]?(\d+)", folder)
        if match:
            day_num = int(match.group(1))
            summary_path = os.path.join(folder, "summary.md")

            if os.path.exists(summary_path):
                days.append((day_num, summary_path))

    if not days:
        raise RuntimeError("No Day folders with summary.md found")

    return max(days, key=lambda x: x[0])


def update_daily_progress(content, summary):
    pattern = re.compile(
        f"{START_MARKER}[\\s\\S]*?{END_MARKER}",
        re.MULTILINE
    )

    return pattern.sub(
        f"{START_MARKER}\n{summary}\n\n---\n{END_MARKER}",
        content
    )


def update_progress_badge(content, day):
    return re.sub(
        r"Progress-\d+?\d%2F100",
        f"Progress-{day}%2F100",
        content
    )


def update_current_day_text(content, day):
    return re.sub(
        r"\*\*Day \d+ / 100\*\*",
        f"**Day {day} / 100**",
        content
    )


def main():
    day, summary_path = get_latest_day()

    with open(summary_path, "r", encoding="utf-8") as f:
        summary = f.read().strip()

    with open(README_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    content = update_daily_progress(content, summary)
    content = update_progress_badge(content, day)
    content = update_current_day_text(content, day)

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"README updated successfully (Day {day}).")


if __name__ == "__main__":
    main()
