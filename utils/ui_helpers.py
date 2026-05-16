from datetime import datetime
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

    def convert_to_12_hour(self, time_24h: str) -> str:
        """
        Converts a 24-hour time string (HH:MM) to a 12-hour format with AM/PM.

        Args:
            time_24h (str): The time in 24-hour format (e.g., "13:37").

        Returns:
            str: The time in 12-hour format (e.g., "1:37 PM").
        """
        # Parse the 24-hour string into a datetime object
        time_obj = datetime.strptime(time_24h, "%H:%M")

        # Format it back to a 12-hour string (%I is 12-hour clock, %p is AM/PM)
        time_12h = time_obj.strftime("%I:%M %p")

        # Optional: Remove the leading zero from single-digit hours (e.g., "01:37 PM" -> "1:37 PM")
        if time_12h.startswith("0"):
            time_12h = time_12h[1:]

        return time_12h

    def convert_date(self, date_str: str) -> str:
        """
        Converts a date string from yyyy-mm-dd to dd-mm-yyyy.
        """
        # Parse the string into a valid datetime object
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")

        # Format the datetime object back into the new string format
        return date_obj.strftime("%d-%m-%Y")
