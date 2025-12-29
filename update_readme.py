from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
README = ROOT / "README.md"

DAY_PATTERN = re.compile(r"Day (\d+)")


def get_days():
    days = []

    for d in ROOT.iterdir():
        if d.is_dir():
            match = DAY_PATTERN.fullmatch(d.name)
            if match:
                summary = d / "summary.md"
                if summary.exists():
                    days.append((int(match.group(1)), d))

    if not days:
        raise RuntimeError("No Day folders with summary.md found")

    # küçükten büyüğe → sonra ters çevireceğiz
    return sorted(days)


def build_daily_progress(days):
    # büyükten küçüğe (en güncel üstte)
    days_desc = list(reversed(days))

    lines = []
    lines.append("## 📅 Daily Progress\n")

    # 🔹 En güncel gün
    latest_day, latest_dir = days_desc[0]
    lines.append(f"### Day {latest_day}\n")
    lines.append(f"- 📄 [Open Summary](./{latest_dir.name}/summary.md)")
    lines.append(f"- 📂 [Open Folder](./{latest_dir.name})\n")

    # 🔹 Eğer sadece 1 gün varsa → üçgen yok
    if len(days_desc) == 1:
        return "\n".join(lines), latest_day

    # 🔹 Önceki günler → kapalı üçgen
    lines.append("---\n")
    lines.append("<details>")
    lines.append("<summary><strong>📚 Previous Days</strong></summary>\n")
    lines.append("<br>\n")

    for day, d in days_desc[1:]:
        lines.append(f"### Day {day}")
        lines.append(f"- 📄 [Open Summary](./{d.name}/summary.md)")
        lines.append(f"- 📂 [Open Folder](./{d.name})\n")

    lines.append("</details>\n")

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
