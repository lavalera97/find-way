import itertools


def get_all_variations(points: list) -> list:
    # Выбираем все возможные вариации наших точек так, чтобы начало и конец совпадали
    # Getting all variations of our points to start and finish at the same position
    start_end_point = points[0]
    correct_paths = ([i for i in set(list(itertools.permutations(points)))
                      if i[0] == start_end_point and i[-1] == start_end_point])
    return correct_paths


def get_shortest_path(paths: list) -> dict:
    # Находим кратчайший путь и для удобства всю информацию располагаем в словаре
    # Using func to find shortest path and return our result as a dict
    shortest_path = {
        'path': 0,
        'distance': 0,
        'points': {}
    }
    for path in paths:
        current_path = {
            'path': path,
            'distance': 0,
            'points': {}
        }
        for point in range(0, len(path) - 1):
            current_point = path[point]
            next_point = path[point + 1]
            length = ((next_point[0] - current_point[0]) ** 2 + (next_point[1] - current_point[1]) ** 2) ** 0.5
            current_path['distance'] += length
            current_path['points'][f'{point + 1}'] = current_path['distance']
        if current_path['distance'] < shortest_path['distance'] or shortest_path['distance'] == 0:
            shortest_path = current_path
    return shortest_path


def show_way(path: dict) -> str:
    # Возвращаем наш путь в виде строки / Show our results in a string
    path_points = [f"{path['path'][i]}[{path['points'][str(i)]}]" for i in range(1, len(path['path']))]
    represent_path = ' -> '.join(path_points)
    result = f"{path['path'][0]} -> {represent_path} = {path['distance']}"
    return result


if __name__ == '__main__':
    # Те точки, через которые нам нужно пройти / There are points that we have to visit
    points = [(0, 2), (2, 5), (5, 2), (6, 6), (8, 3), (0, 2)]
    paths = get_all_variations(points)
    shortest_path = get_shortest_path(paths)
    print(show_way(shortest_path))
