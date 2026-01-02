from diffusers import StableDiffusionPipeline
import torch

def generate_photo(prompt: str, output_path: str = "generated_photo.png"):
    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
    )
    if torch.cuda.is_available():
        pipe = pipe.to("cuda")
    else:
        print("Warning: No GPU found. Image generation will be much slower on CPU.")
    image = pipe(prompt).images[0]
    image.save(output_path)
    print(f"Image saved to {output_path}")

if __name__ == "__main__":
    user_prompt = input("Enter your photo prompt: ")
    generate_photo(user_prompt)