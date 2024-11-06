import colaEspecial

ColaEspecial_1 = colaEspecial.ColaEspecial(10)
for person in ['Don', 'Ken', 'Ivan', 'Raj', 'Amir', 'Adi']:
    ColaEspecial_1.insert(person)

print('After inserting', len(ColaEspecial_1), 'persons on the queue, it contains:\n', ColaEspecial_1)

print('Is queue full?', ColaEspecial_1.isFull())

print('Removing items from the queue:')

while not ColaEspecial_1.isEmpty():
    print(ColaEspecial_1.remove(), end=' ')
print()
