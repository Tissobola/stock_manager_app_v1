class ErrorReader:
    def read(error):
        if len(error) == 0:
            return None
        exception = Exception()
        output = ''
        result = []
        for i, parameter in enumerate(error):
            output += parameter+": "+str(error[parameter])
            result.append(output)
            output = ''
        exception.args = tuple(i for i in result)
        return exception
    
_inst = ErrorReader
read = _inst.read