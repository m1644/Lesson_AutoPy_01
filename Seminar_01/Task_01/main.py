from zeep import Client, Settings
import yaml


with open("config.yaml") as f:
    data = yaml.safe_load(f)
    wsdl = data["wsdl"]

settings = Settings(strict=False)
client = Client(wsdl=wsdl, settings=settings)

def check_words(word):
    box = client.service.checkText(word)
    if box:
        return box[0]['s']

if __name__ == "__main__":
    check_words("малако")
