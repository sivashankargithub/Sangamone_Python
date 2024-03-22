from openai import OpenAI
client = OpenAI(api_key="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")

response = client.images.generate(
  model="dall-e-3",
  prompt="mango fruit",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)
