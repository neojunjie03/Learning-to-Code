students = {
"Alice" : [80, 85, 90],
"Bob" : [78.2, 78.3, 78.4],
"Charlie" : [91.6, 91.7, 91.8]
}

for name, scores in students.items():
    average = sum(scores) / len(scores)
    print(f"{name}: {round(average, 1)}")