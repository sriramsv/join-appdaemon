# join-appdaemon
Appdaemon App to receive joaoapps join events into homeassistant

## Installation
* Download the root directory from inside the apps directory here to your local apps directory, then add the configuration to enable the JoinListener module.
* Add `python-join-api==0.0.7` to requirements.txt for installing the `pyjoin` module

## App Configuration:

``` yaml
joinListener:
  class: JoinListener
  module: joinListener
  join_api_key: !secret join_api_key 
  port: 1822
  device_name: appdaemon
```

key | optional | type | default | description
-- | -- | -- | -- | --
`module` | False | string | | The module name of the app.
`class` | False | string | | The name of the Class.
`join_api_key` | False | string | | Join App API key
`port` | False | integer | | Port to start Listener
`device_name` | False | string | | Device Identifier in Join

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
