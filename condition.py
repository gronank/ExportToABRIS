import re

class Condition:
    property:str=''
    pattern=None
    def __init__(self, condition):
        if condition is not None:
            self.property = condition["property"]
            self.pattern =re.compile(condition["pattern"])

    def match(self,feature):
        if self.pattern:
            value = feature.properties[self.property]
            return self.pattern.match(value) is not None
        else:
            return True

class NameParser:
    property:str=''
    pattern=None
    replace:str=''
    def __init__(self, condition):
        if condition is None:
            return
        self.property = condition.get("property")
        self.pattern = re.compile(condition.get("pattern"))
        self.replace = condition["replace"]

    def parse(self,feature):
        if self.pattern is None:
            return replace
        value = feature.properties[self.property]
        match = self.pattern.sub(self.replace, value)
        return match

