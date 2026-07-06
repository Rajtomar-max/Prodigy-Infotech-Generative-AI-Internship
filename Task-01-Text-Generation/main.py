from transformers import pipeline
import os

print("=" * 60)
print("🤖 GPT-2 TEXT GENERATION")
print("=" * 60)

# Load GPT-2 model
generator = pipeline(
    "text-generation",
    model="gpt2"
)

# User Input
prompt = input("\nEnter your prompt: ")

# Generate Text
result = generator(
    prompt,
    max_length=100,
    temperature=0.8,
    do_sample=True,
    num_return_sequences=1
)

generated_text = result[0]["generated_text"]

print("\nGenerated Text\n")
print("-" * 60)
print(generated_text)
print("-" * 60)

# Save Output
os.makedirs("outputs", exist_ok=True)

with open("outputs/generated_text.txt", "w", encoding="utf-8") as file:
    file.write(generated_text)

print("\n✅ Generated text saved successfully in outputs/generated_text.txt")
