# Predict API

## Endpoint
`POST` `/predict`

## Description
This API endpoint accepts input values and returns the prediction.

## Detail API
### Data Description
| **Variable** | **Type** | **Description**                                                                                                                                                               |
|--------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Humidity`    | integer   | The humidity percentage measured when sensor recording.                                                                                                                               |
| `Pressure`    | integer   | The pressure value (in hPa) measured when sensor recording.                                                                                             |
| `PM1`       | integer  | The concentration of particulate matter with a diameter of 1 micrometers or less (in µm), measured when sensor recording.                                   |
| `TVOC`       | integer  | The Total Volatile Organic Compounts (in parts per billion), measured when sensor recording.                                     |
| `H2`        | integer  | The hydrogen molecule measured when sensor recording.                                                                                               |
| `Ethanol`         | integer  | The concentration of ethanol gas measured when sensor recording.                                                                                               |

### Request
```json
{
    "Humidity": 57.36,
    "Pressure": 939.735,
    "PM1": 0.0,
    "TVOC": 0,
    "H2": 12306,
    "Ethanol": 18520
}
```

### Response
```json
{
    "Fire Alarm": "Tidak ada api"
}
```