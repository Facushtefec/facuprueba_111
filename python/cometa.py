print("----EL MUNDO DE CHARLY: confección de un cometa----")

#---ingreso---
bd = float(input("ingresa lado BD:"))
bc = float(input("ingresa lado BC:"))
ad = float(input("ingresa lado AD:"))
ac = float(input("ingresa lado AC:"))
diag_ab = float(input("ingresa diagonal AB:"))
diag_cd = float(input("ingresa diagonal CD:"))

# ---proceso---
varilla_cometa_cm = bd + bc + ad + ac + diag_ab + diag_cd
varilla_cometa_m = varilla_cometa_cm / 100

# 2. Calculamos papel (Área + 10%)
area_cuerpo = (diag_ab * diag_cd) / 2
papel_total_uno = area_cuerpo + (area_cuerpo * 0.10)

# 3. Multiplicamos por la cantidad pedida (10)
varilla_10 = varilla_cometa_m * 10
papel_10 = papel_total_uno * 10

# --- SALIDA ---
print(f"Para 10 cometas se necesitan {varilla_10} metros de varilla.")
print(f"Para 10 cometas se necesitan {papel_10} cm2 de papel.")