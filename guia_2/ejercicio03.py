months = ["ene", "feb", "mar", "abr", "may", "jun"]

salary_per_month = []
for month in months:
    monthly_salary = float(input(f"Ingresá el salario de {month}: "))
    salary_per_month.append(monthly_salary)

print("Aguinaldo", max(salary_per_month) / 2)

lowest_salary = [x for x in salary_per_month if x == min(salary_per_month)][0]
print(f"Menor sueldo de {lowest_salary}")
print("Sueldo promedio", sum(salary_per_month) / len(salary_per_month))
