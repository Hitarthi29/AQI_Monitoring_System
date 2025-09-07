import requests

class AQIDataFetcher:
    API_URL = 'https://api.data.gov.in/resource/3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69'
    API_KEY = '579b464db66ec23bdd000001eba3effc176b441a67309c9d2964943f'

    @staticmethod
    def fetch_data():
        params = {
            'api-key': AQIDataFetcher.API_KEY,
            'format': 'json',
            'limit': 3100,
            'filters[country]': 'India'
        }
        response = requests.get(AQIDataFetcher.API_URL, params=params)
        return response.json()

    @staticmethod
    def process_data(data):
        all_pollutants = ["PM10", "PM2.5", "NO2", "SO2", "CO", "OZONE", "NH3"]
        result = {}
        if isinstance(data, list):
            data = data[0]
        for record in data.get('records', []):
            city = record.get('city')
            pollutant = record.get('pollutant_id')
            avg_value = record.get('avg_value', '0')
            last_update = record.get('last_update')
            if city not in result:
                result[city] = {"city": city, **{p: '0' for p in all_pollutants}, "last_updated": last_update}
            result[city][pollutant] = avg_value
        output = []
        for entry in result.values():
            output.append((entry['city'], entry['PM10'], entry['PM2.5'], entry['NO2'], entry['SO2'], entry['CO'], entry['OZONE'], entry['NH3'], entry['last_updated']))
        return output
