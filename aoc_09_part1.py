from itertools import combinations

if __name__ == '__main__':
    # f = open('aoc_09_testdata_01.txt')
    f = open('aoc_09_data_01.txt')
    # coords = [(int(line.strip().split(',')[0]), int(line.strip().split(',')[1])) for line in f]
    temp_coords = [line.strip().split(',') for line in f]
    coords = [(int(line[0]), int(line[1])) for line in temp_coords]
    f.close()
    print(coords)

    max_area = 0
    for comb in combinations(coords, 2):
        coord1 , coord2 = comb
        area = (abs(coord1[0] - coord2[0]) + 1) * (abs(coord1[1] - coord2[1]) + 1)
        print(comb, area)
        max_area = max(max_area, area)
    print(max_area)
    # 4777967538

