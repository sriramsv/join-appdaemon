# join-appdaemon
Appdaemon App to receive joaoapps join events into homeassistant

Home Assistant Events will look like:


## Installation

* Drop the `joinListener.py` and `joinListener.yaml` into your appdaemon apps directory
* Add your Join API Key to your `secrets.yaml` and restart appdaemon
* You should see your `appdaemon` device appear in your list of devices in your join app or on https://joinjoaomgcd.appspot.com/ 
* Now send any text message from anywhere including tasker/nodered/browser and see your `join_event` appear on homeassistant


### Sample Event: 

``` json  
{
    "event_type": "join_event",
    "event": {
        "deviceNames": "appdaemon",
        "apikey": "<api-key>",
        "text": "hello=:=sriram=:=07",
        "senderId": "6c0baa3034514e9e963ba6743143f7cd",
        "id": "fca4ceb7-f153-43f0-8584-5ffadfa1e83f"
    }
}
```