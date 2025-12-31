api_keys = {
    "key_1": "sk-abcdef1234567890abcdef1234567890abcdef12",
    "key_2": "sk-1234567890abcdef1234567890abcdef12345678",
    "key_3": "sk-abcdefabcdefabcdefabcdefabcdefabcdef12",
    "key_4": "sk-7890abcdef7890abcdef7890abcdef7890abcd",
    "key_5": "sk-1234abcd1234abcd1234abcd1234abcd1234abcd",
    "key_6": "sk-abcd1234abcd1234abcd1234abcd1234abcd1234",
    "key_7": "sk-5678efgh5678efgh5678efgh5678efgh5678efgh",
    "key_8": "sk-efgh5678efgh5678efgh5678efgh5678efgh5678",
    "key_9": "sk-ijkl1234ijkl1234ijkl1234ijkl1234ijkl1234",
    "key_10": "sk-mnop5678mnop5678mnop5678mnop5678mnop5678",
    "key_11": "sk-qrst1234qrst1234qrst1234qrst1234qrst1234",
    "key_12": "sk-uvwx5678uvwx5678uvwx5678uvwx5678uvwx5678",
    "key_13": "sk-1234ijkl1234ijkl1234ijkl1234ijkl1234ijkl",
    "key_14": "sk-5678mnop5678mnop5678mnop5678mnop5678mnop",
    "key_15": "sk-qrst5678qrst5678qrst5678qrst5678qrst5678",
    "key_16": "sk-uvwx1234uvwx1234uvwx1234uvwx1234uvwx1234",
    "key_17": "sk-1234abcd5678efgh1234abcd5678efgh1234abcd",
    "key_18": "sk-5678ijkl1234mnop5678ijkl1234mnop5678ijkl",
    "key_19": "sk-abcdqrstefghuvwxabcdqrstefghuvwxabcdqrst",
    "key_20": "sk-ijklmnop1234qrstijklmnop1234qrstijklmnop",
    "key_21": "sk-1234uvwx5678abcd1234uvwx5678abcd1234uvwx",
    "key_22": "sk-efghijkl5678mnopabcd1234efghijkl5678mnop",
    "key_23": "sk-mnopqrstuvwxabcdmnopqrstuvwxabcdmnopqrst",
    "key_24": "sk-ijklmnopqrstuvwxijklmnopqrstuvwxijklmnop",
    "key_25": "sk-abcd1234efgh5678abcd1234efgh5678abcd1234",
    "key_26": "sk-1234ijklmnop5678ijklmnop1234ijklmnop5678",
    "key_27": "sk-qrstefghuvwxabcdqrstefghuvwxabcdqrstefgh",
    "key_28": "sk-uvwxijklmnop1234uvwxijklmnop1234uvwxijkl",
    "key_29": "sk-abcd5678efgh1234abcd5678efgh1234abcd5678",
    "key_30": "sk-ijklmnopqrstuvwxijklmnopqrstuvwxijklmnop",
    "key_31": "sk-1234qrstuvwxabcd1234qrstuvwxabcd1234qrst",
    "key_32": "sk-efghijklmnop5678efghijklmnop5678efghijkl",
    "key_33": "sk-mnopabcd1234efghmnopabcd1234efghmnopabcd",
    "key_34": "sk-ijklqrst5678uvwxijklqrst5678uvwxijklqrst",
    "key_35": "sk-1234ijkl5678mnop1234ijkl5678mnop1234ijkl",
    "key_36": "sk-abcdqrstefgh5678abcdqrstefgh5678abcdqrst",
    "key_37": "sk-ijklmnopuvwx1234ijklmnopuvwx1234ijklmnop",
    "key_38": "sk-efgh5678abcd1234efgh5678abcd1234efgh5678",
    "key_39": "sk-mnopqrstijkl5678mnopqrstijkl5678mnopqrst",
    "key_40": "sk-1234uvwxabcd5678uvwxabcd1234uvwxabcd5678",
    "key_41": "sk-ijklmnop5678efghijklmnop5678efghijklmnop",
    "key_42": "sk-abcd1234qrstuvwxabcd1234qrstuvwxabcd1234",
    "key_43": "sk-1234efgh5678ijkl1234efgh5678ijkl1234efgh",
    "key_44": "sk-5678mnopqrstuvwx5678mnopqrstuvwx5678mnop",
    "key_45": "sk-abcdijkl1234uvwxabcdijkl1234uvwxabcdijkl",
    "key_46": "sk-ijklmnopabcd5678ijklmnopabcd5678ijklmnop",
    "key_47": "sk-1234efghqrstuvwx1234efghqrstuvwx1234efgh",
    "key_48": "sk-5678ijklmnopabcd5678ijklmnopabcd5678ijkl",
    "key_49": "sk-abcd1234efgh5678abcd1234efgh5678abcd1234",
    "key_50": "sk-ijklmnopqrstuvwxijklmnopqrstuvwxijklmnop"
}
from openai import OpenAI
from openai import AuthenticationError, RateLimitError, OpenAIError


def chat_with_rotation(prompt: str):
    for name, api_key in api_keys.items():
        try:
            print(f"Trying {name}...")

            client = OpenAI(api_key=api_key)

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ]
            )

            return response.choices[0].message.content

        except AuthenticationError:
            print(f"❌ {name} failed: Invalid API key")
        except RateLimitError:
            print(f"⚠️ {name} rate-limited, trying next key")
        except OpenAIError as e:
            print(f"⚠️ {name} error: {e}")

    return "All API keys failed."

# ---- Run chat ----
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    reply = chat_with_rotation(user_input)
    print("Assistant:", reply)

