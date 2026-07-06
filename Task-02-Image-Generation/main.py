import os
from diffusers import StableDiffusionPipeline
import torch

print("="*60)
print("🖼️ IMAGE GENERATION USING STABLE DIFFUSION")
print("="*60)

# Output folder
os.makedirs("outputs", exist_ok=True)

# Load Model
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16
)

pipe = pipe.to("cuda")

# User Prompt
prompt = input("Enter your prompt : ")

print("\nGenerating image...")
image = pipe(prompt).images[0]

# Save Image
image.save("outputs/generated_image.png")

print("\n✅ Image Generated Successfully!")
print("Saved in outputs/generated_image.png")
