from funktion import calculate_monthly_interest, translate
import os


FILE_NAME = "MyData.txt"


def read_data():
    if not os.path.exists(FILE_NAME):
        return None

    try:
        data = {}
        with open(FILE_NAME, "r") as f:
            for line in f:
                key, val = line.strip().split("=")
                data[key] = val

        deposit = float(data["deposit"])
        years = float(data["years"])
        lang = data["lang"]
        return deposit, years, lang

    except Exception:
        return None


def save_data(deposit, years, lang):
    with open(FILE_NAME, "w") as f:
        f.write(f"deposit={deposit}\n")
        f.write(f"years={years}\n")
        f.write(f"lang={lang}\n")


def main():
    data = read_data()

    if data is None:
        deposit = float(input(translate("enter_deposit", "uk")))
        years = float(input(translate("enter_years", "uk")))
        lang = input(translate("enter_lang", "uk")).strip()

        save_data(deposit, years, lang)
        print(f"{translate('saved', lang)} [{FILE_NAME}]")
        return

    deposit, years, lang = data

    if lang not in ["uk", "en"]:
        lang = "uk"

    monthly = calculate_monthly_interest(deposit, years)

    print(f"{translate('lang_name', lang)}:")
    print(f"{translate('deposit', lang)} {deposit} {translate('uah', lang)} "
          f"{translate('years', lang)} {years} "
          f"{translate('percent', lang)} "
      f"{'8%' if years >=1 else '6%'} {translate('per_year', lang)}.")
    print(f"{translate('monthly', lang)}: {monthly} {translate('uah', lang)}.")


if __name__ == "__main__":
    main()
