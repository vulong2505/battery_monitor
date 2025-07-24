# Battery Monitor

A lightweight tool that monitors your laptop's battery and provides intelligent charging recommendations to maximize battery lifespan.

## Motivation

After burning through several laptop batteries, my motivation to build this tool is to protect my laptop's lithium battery from the two main causes of degradation:

- **Overcharging**: Staying plugged in at 100% for extended periods
- **Deep discharge**: Allowing the battery to remain at 0% for extended periods

Therefore, the tool helps tracks battery health metrics and provides timely notifications about when to plug or unplug my charger, helping me maintain optimal battery health over time.

## Features

- 🔋 Real-time battery monitoring
- 📊 Battery health data tracking
- 🔔 Smart charging/unplugging notifications
- ⚡ Lightweight and efficient operation
- TODO: 📈 Historical battery performance analytics
- TODO: 🤖 ML model prediction of battery health 

## How It Works

The tool continuously monitors your battery level and provides recommendations based on configurable thresholds:
- **Unplug reminder**: When battery reaches your defined upper threshold (e.g., 80-90%)
- **Plug reminder**: When battery drops to your defined lower threshold (e.g., 20-30%)
- **Data Logging**: Log battery health data for 

## Installation

```bash
git clone https://github.com/vulong2505/battery_monitor         # Clone repo
cd battery_monitor
python -m venv venv                                             # Virtual environment
source venv/bin/activate                                        # On Windows: venv\Scripts\activate
pip install -r requirements.txt
py main.py                                                      # Run program
```

## Configuration

TODO: Finish writing

## Usage

TODO: Finish writing

## Data Collection

The tool collects and stores the following battery health metrics:
- Timestamp
- Battery percentage over time
- Plugged status
- Window's prediction of seconds left on battery
- Net time left charging at 100%
- Time since last plug
- Time since last unplug

TODO: add more data analytics