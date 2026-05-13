from datetime import date


class UIHelpers:
    def __init__(self, page):
        self.page = page

    def convert_true_to_enable(self, status):
        if status is True or status == "true":
            return "Enabled"
        elif status is False or status == "false":
            return "Disabled"
        return status

    def get_current_date(self):
        today = date.today()
        return str(today.isoformat())
