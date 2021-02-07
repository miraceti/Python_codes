currency = lambda n : f"${n:,.2f}"
percent = lambda n : f"{n:.2%}"

percent1 = lambda n : f"{n:.1%}"

print(currency(99))

print(percent(0.005))
print(percent1(0.005))

s = "Normal"
print(":"+s.ljust(10)+":")
print(":"+s.rjust(10)+":")