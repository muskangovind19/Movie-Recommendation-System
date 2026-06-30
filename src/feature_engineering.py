from src.utils import clean_text

def create_tags(df):

    df["tags"] = (
        df["listed_in"] + " " +
        df["description"] + " " +
        df["director"] + " " +
        df["cast"]
    )

    df["tags"] = df["tags"].apply(clean_text)

    return df