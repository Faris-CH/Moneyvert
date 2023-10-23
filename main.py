import kivy
from kivy.app import App
from Datascrape import get_value
from kivy.uix.floatlayout import FloatLayout

kivy.require("1.9.0")

class UI(FloatLayout):
    def __init__(self):
        FloatLayout.__init__(self)

    def generate_convert(self) -> None:
        if self.is_num(self.input.text):
            self.converted.text = str(self.convert_money(float(self.input.text)))

    def reverse(self) -> None:
        temp = ""
        temp_back = ""
        temp_text = ""
        temp += self.btn.text
        temp_back += self.btn.background_normal
        temp_text += self.converted.text
        self.btn.text = self.btn2.text
        self.btn.background_normal = self.btn2.background_normal
        self.btn2.text = temp
        self.btn2.background_normal = temp_back
        if self.converted.text != "-":
            self.converted.text = self.input.text
            self.input.text = temp_text

    def change_to_cad(self) -> None:
        self.btn.background_normal = "cadflag.jpeg"
        self.btn.text = "CAD"

    def change_to_usd(self) -> None:
        self.btn.text = "USD"
        self.btn.background_normal = "flag.png"

    def change_to_lira(self) -> None:
        self.btn.text = "TRY"
        self.btn.background_normal = "turkeyflag.png"

    def change_to_cad2(self) -> None:
        self.btn2.text = "CAD"
        self.btn2.background_normal = "cadflag.jpeg"

    def change_to_usd2(self) -> None:
        self.btn2.text = "USD"
        self.btn2.background_normal = "flag.png"

    def change_to_lira2(self) -> None:
        self.btn2.text = "TRY"
        self.btn2.background_normal = "turkeyflag.png"

    def is_num(self, string: str) -> bool:
        """
        Check if str is num.
        """
        try:
            float(string)
            return True
        except ValueError:
            return False

    def reset(self, instance) -> None:
        """
        Reset the amount inputted and the converted amount.
        """
        self.amount.text = ""

    def convert_money(self, userinput: float) -> float:
        """
        Convert from lira to CAD.
        """
        if self.btn.text == "Lira":
            self.btn.text = "TRY"
        if self.btn2.text == "Lira":
            self.btn2.text = "TRY"
        amount = userinput * get_value(self.btn.text, self.btn2.text)
        if self.btn.text == "TRY":
            self.btn.text = "Lira"
        if self.btn2.text == "TRY":
            self.btn2.text = "Lira"
        return round(amount, 2)


class CurrencyApp(App):

    def build(self):
        """
        Build The App
        """
        return UI()


if __name__ == "__main__":
    CurrencyApp().run()

