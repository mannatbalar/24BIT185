def sum_avg(m1, m2, m3, m4, m5):
    
    total = m1 + m2 + m3 + m4 + m5
    average = total / 5
    return total, average


marks = [85, 90, 78, 88, 92]
total, average = sum_avg(*marks)

print(f"Marks: {marks}")
print(f"Total: {total}")
print(f"Average: {average}")
