"""One Emoji, One Dream Vacation — entry program.

Writes exactly one emoji to /output/entry.txt (no trailing newline).

Final entry: U+1F5FB MOUNT FUJI (🗻).

Revision history (judged against the kit's brief, most important first):
- Pass 1: 🗻 MOUNT FUJI. One named, iconic place: a stranger sees the
  postcard instantly (snow-capped peak), it points at ONE particular dream
  trip (Japan, dawn at Fuji) rather than any holiday, and it reads clearly
  at small size across cultures. Surprise: it is a place, not a generic
  beach/plane, so it beats the obvious holiday picks on specificity.
- Pass 2 challenger: 🌋 VOLCANO (U+1F30B). More surprising and vivid, but
  it reads as disaster as easily as vacation, so it is weaker on criterion 1
  (plainly names a dream vacation) and criterion 2 (the postcard is lava,
  not a place you book). Rejected; reverted to pass 1.

Losers considered and rejected without a run: 🏖️ beach with umbrella and
🏝️ desert island (the two most generic holiday emojis — the field of 42
will be full of them; they lose on specificity and wit), ✈️ airplane
(a means of travel, not a destination; no postcard), 🌅 sunrise over sea
(pretty but generic — could be any coast, any morning).
"""
import os

EMOJI = "\U0001f5fb"  # MOUNT FUJI

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)

if __name__ == "__main__":
    main()
