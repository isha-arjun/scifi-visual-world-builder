# 🪐 Sci-Fi Visual World-Builder AI

A automated python script designed for sci-fi retro indie platformer game development. This project hooks directly into the **Google Gemini API** to instantly generate rich, atmospheric lore profiles, environmental designs, and faction data for fictional game worlds.

---

## 🚀 Features
* **Dynamic Content Engine**: Generates specialized world attributes instantly based on user input parameters.
* **Structured Lore Markdown**: Outputs complete copy-pasteable files ready to use inside a game manual or dev log.
* **100% Free Stack**: Built utilizing pure Python, standard network requests, and the free Google AI Studio access tier.

## 🛠️ Technology Stack
* **Language**: Python 3
* **AI Engine**: Google Gemini API (`gemini-2.5-flash`)
* **Libraries**: `requests`, `json`

## ⚙️ How It Works
The script accepts basic user inputs (Planet Name, Climate/Environment Type, and Dominant Faction) and structures a highly descriptive context instruction prompt. It passes this securely to the cloud models to generate an structured layout with environment details, ecosystem assets, and hidden historical secrets.

## 📦 Local Setup Instructions
1. Clone this project repository folder to your local device.
2. Acquire a free API Key from [Google AI Studio](https://google.com).
3. Open `world_builder.py` and assign your key to the `API_KEY` string variable.
4. Execute the script using any terminal window:
```bash
python world_builder.py
```
