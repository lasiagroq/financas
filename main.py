from datetime import datetime

contas = [
    {"nome": "Aluguel", "vencimento": "2026-03-25"},
    {"nome": "Internet", "vencimento": "2026-03-22"},
    {"nome": "Luz", "vencimento": "2026-03-20"},
]

hoje = datetime.today()

print("📊 Verificando contas...\n")

for conta in contas:
    data_venc = datetime.strptime(conta["vencimento"], "%Y-%m-%d")
    dias = (data_venc - hoje).days

    if dias < 0:
        print(f"❌ {conta['nome']} está VENCIDA!")
    elif dias <= 2:
        print(f"⚠️ {conta['nome']} vence em {dias} dias!")
    else:
        print(f"✅ {conta['nome']} está ok")
