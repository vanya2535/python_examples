class QueryBuilder:

    def __init__(self):
        self.select_resut = ''
        self.where_result = ''
        self.fron_result = ''

    def fron(self, *args: str):
        get = args
        self.fron_result = self.fron_result.join(elem + ', ' for elem in get)
        return self
    
    def where(self, *args: str):
        get = args
        self.where_result = self.where_result.join(elem + ', ' for elem in get)
        return self

    def select(self, *args: str):
        get = args
        self.select_resut = self.select_resut.join(elem + ', ' for elem in get)
        return self

    def _clean(self):
        if self.fron_result[len(self.fron_result) - 2] == ',':
            self.fron_result = self.fron_result[:len(self.fron_result) - 2]
        if self.select_resut[len(self.select_resut) - 2] == ',':
            self.select_resut = self.select_resut[:len(self.select_resut) - 2]
        if self.where_result[len(self.where_result) - 2] == ',':
            self.where_result = self.where_result[:len(self.where_result) - 2]

    '''def _clean(self):
        res = [self.fron_result, self.select_resut, self.where_result]
        for index, elem in enumerate(res):
            if elem[len(elem) - 2] == ',':
                print(res[index], elem[:len(elem) - 2])
                res[index] = elem[:len(elem) - 2]''' # not working xD

    def build(self):
        self._clean()
        return 'FROM ' + self.fron_result + ' SELECT ' + self.select_resut + ' WHERE ' + self.where_result 

sql = QueryBuilder().where('id < 3').fron('users').select('id').select('name', 'email').build()
print(sql)
