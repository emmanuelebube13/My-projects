# Pseudocode:

# Input:

# Prompt user for number of tons (as integer).
# Prompt user for number of stones (as integer).
# Prompt user for number of pounds (as integer).
# Prompt user for number of ounces (as float).
# Convert everything to ounces:

# total_ounces = (35840 * tons) + (224 * stones) + (16 * pounds) + ounces
# Convert ounces to kilograms:

# total_kilos = total_ounces / 35.274
# Break down total kilograms into metric tons and remaining kilograms:

# metric_tons = int(total_kilos / 1000)
# remaining_kilos = int(total_kilos % 1000)
# Calculate grams from remaining kilograms:

# grams = (total_kilos % 1) * 1000
# Output:

# Display the weight in the format:
# metric_tons metric tons
# remaining_kilos kilos
# grams grams (formatted to 1 decimal place)

print("Imperial To Metric Conversion")
print()
Metric_for_conversion = {
                        "Tons" : int(input("Enter the number of tons: ")),
                        "Stone" : int(input("Enter the number of stone: ")),
                        "Pounds" : int(input("Enter the number of pounds: ")),
                        "ounces" : int(input("Enter the number of ounces: ")),
                        }
print()

# making all ounces
total_ounce = (35840 * Metric_for_conversion["Tons"]) + (224 * Metric_for_conversion["Stone"]) + (16 * Metric_for_conversion["Pounds"]) + Metric_for_conversion["ounces"]

# converting ounces to kilos
total_kilos = total_ounce / 35.274

#break down kilos into metric tons, kilos and grams
Metric_ton = int(total_kilos // 1000 ) 
remaining_kilo = int(total_kilos % 1000)
grams = (total_kilos % 1) * 1000

#output
print(f"The metric weight is {Metric_ton}ton, {remaining_kilo}kilo, and {grams: .1f} grams")


#print(f"Your weekly Payment will be: ${weekly_payment:.2f}")
print("Hope you liked it")
