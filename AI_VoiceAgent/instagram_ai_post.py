import torch
from diffusers import StableDiffusionPipeline
from TTS.api import TTS
from moviepy.editor import ImageClip, AudioFileClip
from PIL import Image

# --------- CONFIGURATION ---------
prompt = "Huge shoutout to @timcookbuilds for completing their first coding project!  Amazing what a supportive community can help you achieve. Keep building and inspiring!"
#text = "Feeling the tech love Had an amazing time connecting with incredible minds at the event. Thanks for sharing your passion, @maryjane_tech"
text = "What an amazing vibe at the event! It was incredible meeting so many fellow tech enthusiasts passionate about growth and innovation. Thanks for the inspiration, @maryjane_tech!"
#text = "Huge shouttout to @timcookbuilds for completing their first coding project!  Amazing what a supportive community can help you achieve. Keep building and inspiring!"
speaker_audio_path = "sally_derivative.wav"  # Your cloned voice sample
image_output_path = "maryJaneTech.png"
#audio_output_path = "output_audio.wav"
audio_output_path = "output_audioMary.wav"
video_output_path = "final_instagram_post.mp4"

# --------- 1. Generate Image using Stable Diffusion ---------
# print("🖼️ Generating image...")
# #pipe = StableDiffusionPipeline.from_pretrained("stabilityai/sd-turbo", torch_dtype=torch.float32)
# pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
# pipe.to("cpu")  # Use CPU for MacBook

# image = pipe(prompt).images[0]
# image.save(image_output_path)

# --------- 2. Generate Cloned Voice using Coqui XTTS ---------
print("🎤 Generating voice...")
tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2")
tts.tts_to_file(
    text=text,
    speaker_wav=speaker_audio_path,
    language="en",
    file_path=audio_output_path
)

# --------- 3. Combine Image + Audio into Video ---------
print("🎞️ Creating video post...")
image_clip = ImageClip(image_output_path).set_duration(5)
audio_clip = AudioFileClip(audio_output_path)
video = image_clip.set_audio(audio_clip)
video.write_videofile(video_output_path, fps=24)

print("✅ Instagram-ready video created:", video_output_path)
