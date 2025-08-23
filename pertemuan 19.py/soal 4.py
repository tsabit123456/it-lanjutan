import re

kalimat = "Kucing, kuda, dan burung adalah hewan peliharaan."
kata_berakhiran_g = re.findall(r'\b\w*g\b', kalimat)
print(kata_berakhiran_g)  # Output: ['Kucing', 'kuda', 'burung']
