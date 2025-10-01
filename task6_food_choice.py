items = {
  "pizza": {"cost": 50, "calories": 300},
  "hamburger": {"cost": 40, "calories": 250},
  "hot-dog": {"cost": 30, "calories": 200},
  "pepsi": {"cost": 10, "calories": 100},
  "cola": {"cost": 15, "calories": 220},
  "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"]/x[1]["cost"], reverse=True)
    total_cost, total_cal = 0, 0
    chosen = []
    for name, data in sorted_items:
        if total_cost + data["cost"] <= budget:
            chosen.append(name)
            total_cost += data["cost"]
            total_cal += data["calories"]
    return chosen, total_cal

def dynamic_programming(budget):
    dp = [0]*(budget+1)
    chosen = [[] for _ in range(budget+1)]
    for name, data in items.items():
        cost, cal = data["cost"], data["calories"]
        for b in range(budget, cost-1, -1):
            if dp[b-cost]+cal > dp[b]:
                dp[b] = dp[b-cost]+cal
                chosen[b] = chosen[b-cost]+[name]
    return chosen[budget], dp[budget]

if __name__ == "__main__":
    print("Greedy:", greedy_algorithm(100))
    print("DP:", dynamic_programming(100))
