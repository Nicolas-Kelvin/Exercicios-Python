nome = 'Kelvin'
cores = {'limpa': '\033[m',
         'azul' : '\033[34m',
         'azulclaro' : '\033[36m',
         'amarelo' : '\033[33m',
         'pretobranco' : '\033[7;30m'}
print('Óla! Muito prazer em te conhecer, {}{}{}!!'.format(cores['azulclaro'],nome, cores['limpa']))