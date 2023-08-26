# lap record in seconds
lap_record = 140

cyclist_qty = int(input("Cantidad de ciclistas: "))

racers = []

for i in range(0, cyclist_qty):
    racer_name = input("Nombre del corredor: ")
    racer_time = int(input("Tiempo en segundos de la vuelta: "))
    if racer_time < lap_record:
        new_record = True
        print("Nuevo record!")
        lap_record = racer_time
    else:
        new_record = False

    racers.append({"name": racer_name, "time": racer_time, "record": new_record})

# get min time
min_time = min([x["time"] for x in racers])
# filter winner by time
winner = [x for x in racers if x["time"] == min_time][0]

# prints the winner info
print(f'El ganador de la carrera es {winner["name"]} con un tiempo de {winner["time"]}')

# get the average speed

times = [x["time"] for x in racers]
average = sum(times) / len(times)
print("El tiempo promedio de la vuelta es de", average)
