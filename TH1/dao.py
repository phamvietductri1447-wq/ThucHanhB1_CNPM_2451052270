import json


def load_categories():
    with open ("data/cate.json",encoding="utf-8") as f:
        return json.load(f)


if __name__=="__main__":
    print(load_categories())