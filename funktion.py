def translate(text_key, lang):
    texts = {
        "uk": {
            "lang_name": "Українська",
            "deposit": "Сума вкладу",
            "years": "роки",
            "percent": "під",
            "monthly": "Сума щомісячних виплат",
            "uah": "грн",
            "enter_deposit": "Введіть суму вкладу (грн): ",
            "enter_years": "Введіть строк договору (лет): ",
            "enter_lang": "Введіть мову інтерфейсу (uk/en): ",
            "saved": "Дані збережено в файл"
        },
        "en": {
            "lang_name": "English",
            "deposit": "Deposit",
            "years": "years",
            "percent": "at",
            "monthly": "Monthly interest payments",
            "uah": "UAH",
            "enter_deposit": "Enter deposit amount (UAH): ",
            "enter_years": "Enter contract duration (years): ",
            "enter_lang": "Enter interface language (uk/en): ",
            "saved": "Data saved to file"
        }
    }
    return texts.get(lang, texts["uk"]).get(text_key, text_key)


def calculate_monthly_interest(deposit, years):
    if 0.5 <= years < 1:
        rate = 0.06
    elif years >= 1:
        rate = 0.08
    else:
        return 0
    return round(deposit * rate / 12)
