from Queue import Queue

class Engine:
    def __init__(self, routines, trigger=None, parameters=dict()):
        self.queue = Queue()
        if trigger:
            self.queue.put(trigger)
        self.routines = routines
        self.parameters = parameters
      
    def list_events(self):
        for i, event in enumerate(self.queue.list):
            print("{}. ".format(i+1), event.type, event.parameters)
      
    def fetch_event(self, engines):
        event = self.queue.get()
        parameters_keys = [i for i in self.parameters.keys() if i in self.routines[event.type].__code__.co_varnames[:self.routines[event.type].__code__.co_argcount]]
        if len(parameters_keys) > 0:
            parameters = dict((key,value) for (key,value) in self.parameters.items() if key in parameters_keys)
            generated_events = self.routines[event.type](**{**parameters, **event.parameters})
        else:
            generated_events = self.routines[event.type](**{**event.parameters})
        if generated_events is not None:
            for next_event in generated_events:
                engines[next_event.engine].queue.put(next_event)
      
    def fetch_exhaustive(self, engines):
        while not self.queue.empty():
            self.fetch_event(engines)
      
    def fetch_and_list(self, engines):
        self.fetch_event(engines)
        self.list_events()