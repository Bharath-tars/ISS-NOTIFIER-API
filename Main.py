import requests
import smtplib
import datetime as dt

My_email = "bharathworks2u@gmail.com"
My_pass = "yopdqyeooorhncxj"
MY_LAT = 51.507351
MY_LAN = 78.486671


def is_above():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    lat_1 = float(data["iss_position"]["latitude"])
    lan_1 = float(data["iss_position"]["longitude"])
    if lat_1 - 5 <= MY_LAT <= lat_1 + 5 and lan_1 - 5 <= MY_LAN <= lan_1 + 5:
        return True

para = {
    "lat": MY_LAT,
    "lng": MY_LAN,
    "formatted": 0
}


def time_sunset():
    responce = requests.get("https://api.sunrise-sunset.org/json", params=para)
    responce.raise_for_status()
    data = responce.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]
    sun_hour = int(sunrise.split("T")[1].split(":")[0])
    set_hour = int(sunset.split("T")[1].split(":")[0])
    cur = dt.datetime.now()
    hour = cur.hour
    if set_hour <= hour or hour >= sun_hour:
        return True


if is_above() and time_sunset():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=My_email, password=My_pass)
    connection.sendmail(from_addr=My_email, to_addrs="bharath.sudarsanam04@gmail.com",
                        msg="Subject:LOOK UP!\n\n\nLOOK UP THE ISS WATCHING YOU")
    connection.close()
