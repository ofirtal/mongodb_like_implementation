math_operators = ['eq', 'gt', 'gte', 'lt', 'lte', 'ne']
range_operators = ['nin', 'in']
and_or = ['and', 'or']
operators_dict = {'gt': lambda x, y: x > int(y),
                  'eq': lambda x, y: x == int(y),
                  'ne': lambda x, y: x != int(y),
                  'eqstr': lambda x, y: x == str(y),
                  'nestr': lambda x, y: x != str(y),
                  'gte': lambda x, y: x >= int(y),
                  'lt': lambda x, y: x < int(y),
                  'lte': lambda x, y: x >= int(y),
                  'nin': lambda x, y: x not in range(y[0], y[1]),
                  'in': lambda x, y: x in range(y[0], y[1])}

