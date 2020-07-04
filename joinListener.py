import appdaemon.plugins.hass.hassapi as hass
import threading,json
from pyjoin import Listener


class JoinListener(hass.Hass):
    def initialize(self):
        self.api_key = self.args.get("join_api_key")
        self.device_name = self.args.get("device_name")
        self.listener = Listener(name=self.device_name,port=1822, api_key=self.api_key)
        self.listener.add_callback(self.on_event)
        self.t=None
        self.run()

    def run(self):
        if self.t:
            self.t.stop()
        self.t=StoppableThread(target=self.flaskThread)
        self.t.setDaemon(True)
        self.t.start()

    def flaskThread(self):
        try:
            self.listener.run()
        except OSError:
            self.log("Server already running")

    def on_event(self, data):
        data = data["json"]
        data=json.loads(data)
        data=data["push"]
        text = data["text"]
        args = self.getargs(text)
        if len(args)>0:
            data["args"]=args
        self.log(data)
        self.fire_event("join_event",**data)
    
    def getargs(self,text):
        args = {}
        if "=:=" not in text:
            return []
        t = text.split("=:=")
        return t[1:]

    def terminate(self):
        self.t.stop()

class StoppableThread(threading.Thread):

    def __init__(self,  *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()