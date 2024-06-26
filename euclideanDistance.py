# Noktaların Tanımlanması
points = [(1, 2), (4, 6), (5, 9), (8, 3)]

# Öklid Mesafesi İçin Bir Fonksiyon
def euclideanDistance(point1, point2):
    return ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2) ** 0.5

# Mesafelerin Hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)
        print(f"Mesafe {points[i]} ve {points[j]} arasında: {distance}")

# Minimum Mesafenin Bulunması
min_distance = min(distances)
print("Minimum Mesafe:", min_distance)
