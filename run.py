import fal

@fal.function(
    "virtualenv",
    requirements=["pyjokes"],
)
def tell_joke() -> str:
    import pyjokes

    joke = pyjokes.get_joke()
    return joke

print("Joke from the clouds: ", tell_joke())