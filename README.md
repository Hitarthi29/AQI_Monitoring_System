# AQI Monitoring System

## Overview
This project collects real-time Air Quality Index (AQI) data for Indian cities and stores it in a MySQL database, and enables visualization in PowerBI. It is designed to analyze historical AQI trends, visualize city-wise air quality, and provide predictive insights for public health awareness. Future enhancements include automated alerts (email/SMS) when AQI crosses unhealthy zones.

## Features
- Fetches AQI data from a public API
- Stores city-wise AQI and pollutant data in MySQL
- Easily integrates with PowerBI for dashboards
- Modular, human-friendly code structure
- Ready for future alerting features

## Project Structure
```
AQI_monitoring_System/
│
├── main.py         # Entry point, coordinates data flow
├── model.py        # Database logic (MySQL)
├── controller.py   # API fetching and data processing
├── README.md       # Project documentation
└── collectAQIData.py # (Original script, now refactored)
```

## Setup Instructions
1. **Clone the repository**
2. **Install Python dependencies**
   ```powershell
   pip install requests mysql-connector-python
   ```
3. **Configure MySQL**
   - Create a database named `AQI` in your MySQL server.
   - Update credentials in `main.py` if needed.
4. **Run the script**
   ```powershell
   python main.py
   ```
5. **Connect PowerBI**
   - Use MySQL connector in PowerBI to visualize data from the `india_aqi` table.

## How It Works
- `main.py` fetches AQI data using `controller.py`, processes it, and stores it in MySQL via `model.py`.
- Data includes city, pollutant levels (PM10, PM2.5, NO2, SO2, CO, OZONE, NH3), and last updated timestamp.Use PowerBI to see User-friendly dashboard & Predictive analytics.

## Future Enhancements
- Automated alerts (email/SMS) for unhealthy AQI levels
- More Predictive analytics for air quality trends
- Mobile notifications

## Contributing
Pull requests and suggestions are welcome! For major changes, please open an issue first.

## License
MIT License

## Author
Hitarthi Bhatt
