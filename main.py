import pkg_resources
import subprocess
import sys
import re
from enum import Enum


required_modules = ["openai", "python-dotenv"]
installed_packages = pkg_resources.working_set
installed_packages_list = sorted(
    ["%s==%s" % (i.key, i.version) for i in installed_packages]
)

for module in required_modules:
    module_found = any([module in item for item in installed_packages_list])
    if not module_found:
        subprocess.check_call([sys.executable, "-m", "pip", "install", module])


from dotenv import load_dotenv

load_dotenv()
from openai import OpenAI
from enum import Enum
import os

client = OpenAI()

class Model(Enum):
    GPT_4 = "gpt-4"
    GPT_4_TURBO_PREVIEW = "gpt-4-turbo-preview"
    GPT_4_VISION_PREVIEW = "gpt-4-vision-preview"
    GPT_4_32K = "gpt-4-32k"
    GPT_3_5_TURBO = "gpt-3.5-turbo"
    GPT_3_5_TURBO_16K = "gpt-3.5-turbo-16k"

selected_text = sys.stdin.read()

prompt_text = "You are a helpful assistant."
prompt_text = "spellcheck"
match = re.search(r"\[(.*?)\]", selected_text)
if match:
    prompt_text = match.group(1)
    prompt_text = re.sub(r'[^a-z]', '', prompt_text.lower())

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "prompts", f"{prompt_text}.txt")

try:
    with open(file_path, "r") as file:
        prompt_text = file.read()
except FileNotFoundError:
    print(f"File not found: {file_path}")

response = client.chat.completions.create(
    model=Model.GPT_4.value,
    messages=[
        {"role": "system", "content": prompt_text},
        {"role": "user", "content": selected_text},
    ],
    temperature=0,
)

if response.choices and len(response.choices) > 0:
    print(response.choices[0].message.content)
