from pathlib import Path
from urllib.parse import quote
import re

ROOT = Path(__file__).resolve().parent
README = ROOT / "README.md"

DAY_PATTERN = re.compile(r"Day (\d+)")
TITLE_PATTERN = re.compile(r"^(#{1,3})\s+(.*)", re.MULTILINE)


def extract_title(summary_path, day_number):
    """
    summary.md içinden ilk markdown başlığını alır.
    Yoksa 'Day X' döner.
    """
    try:
        content = summary_path.read_text(encoding="utf-8")
        match = TITLE_PATTERN.search(content)
        if match:
            return match.group(2).strip()
    except Exception:
        pass

    return f"Day {day_number}"


def get_days():
    days = []

    for d in ROOT.iterdir():
        if d.is_dir():
            match = DAY_PATTERN.fullmatch(d.name)
            if match:
                day_number = int(match.group(1))
                summary = d / "summary.md"
                if summary.exists():
                    title = extract_title(summary, day_number)
                    days.append((day_number, d, title))

    if not days:
        raise RuntimeError("No Day folders with summary.md found")

    return sorted(days)


def build_daily_progress(days):
    # En güncelden eskiye
    days_desc = list(reversed(days))

    lines = []
    lines.append("## 📅 Daily Progress\n")

    # 🔹 Latest day
    latest_day, latest_dir, latest_title = days_desc[0]
    encoded_latest = quote(latest_dir.name)

    lines.append(f"### {latest_title}")
    lines.append(f"- 📄 [Open Summary](./{encoded_latest}/summary.md)")
    lines.append(f"- 📂 [Open Folder](./{encoded_latest})")

    # 🔹 Tek gün varsa
    if len(days_desc) == 1:
        return "\n".join(lines), latest_day

    # 🔹 Separator (SADECE burada)
    lines.append("---")

    # 🔹 Previous days
    lines.append("<details>")
    lines.append("<summary><strong>📚 Previous Days</strong></summary>\n")

    for day, d, title in days_desc[1:]:
        encoded = quote(d.name)
        lines.append(f"### {title}")
        lines.append(f"- 📄 [Open Summary](./{encoded}/summary.md)")
        lines.append(f"- 📂 [Open Folder](./{encoded})")

    lines.append("</details>")

    return "\n".join(lines), latest_day


def update_progress_badge(readme_text, latest_day):
    return re.sub(
        r"!\[Progress\]\(https://img\.shields\.io/badge/Progress-[^)]*\)",
        f"![Progress](https://img.shields.io/badge/Progress-{latest_day}%2F100-brightgreen?style=for-the-badge)",
        readme_text,
    )


def main():
    days = get_days()
    daily_section, latest_day = build_daily_progress(days)

    readme = README.read_text(encoding="utf-8")
    readme = update_progress_badge(readme, latest_day)

    new_readme = re.sub(
        r"<!-- DAILY_PROGRESS_START -->.*?<!-- DAILY_PROGRESS_END -->",
        f"<!-- DAILY_PROGRESS_START -->\n{daily_section}\n<!-- DAILY_PROGRESS_END -->",
        readme,
        flags=re.S,
    )

    README.write_text(new_readme, encoding="utf-8")
    print(f"README updated successfully → Day {latest_day}")


if __name__ == "__main__":
    main()
