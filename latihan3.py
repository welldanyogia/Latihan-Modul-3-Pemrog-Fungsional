random_list = [195, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

float_values = list(filter(lambda x: isinstance(x, float), random_list))
int_values = list(filter(lambda x: isinstance(x, int), random_list))
string_values = list(filter(lambda x: isinstance(x, str), random_list))


def map_int_to_dict(value):
    satuan = value % 10
    puluhan = (value // 10) % 10
    ratusan = value // 100
    return {"ratusan": ratusan, "puluhan": puluhan, "satuan": satuan}


int_mapped = list(map(map_int_to_dict, int_values))

print("Data Float :", tuple(float_values))
print("Data Int :")
for item in int_mapped:
    print(item)
print("Data String :", [s.lower() for s in string_values])
