import tiktoken
from typing import List


def encode(input: str, tokenizer)-> List[int]:
    return tokenizer.encode(input)

def decode(tokens: List[int], tokenizer)-> str:
    return tokenizer.decode(tokens)

if __name__ == "__main__":
    tokenizer =  tiktoken.encoding_for_model("gpt-4o")
    res  = encode("Ian ian",tokenizer)
    output = decode(res, tokenizer)
    print(output)
    print(res)