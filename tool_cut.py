cn_file = open('resources/scene_poetry.txt', 'r')
result_file = open('chinese/scene_poetry.txt', 'w')

poetry_lines = cn_file.readlines()

for line in poetry_lines:
    cn_poetry = line.split('——')[0]
    cn_poetry += '\n'
    result_file.write(cn_poetry)

