import anthropic


def main():
    # Reads the API key from the ANTHROPIC_API_KEY environment variable.
    client = anthropic.Anthropic()

    response = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": "Say a friendly hello to the world."}
        ],
    )

    # response.content is a list of content blocks; print the text ones.
    for block in response.content:
        if block.type == "text":
            print(block.text)


if __name__ == "__main__":
    main()
