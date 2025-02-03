from django.core.management.base import BaseCommand
import stocks.utils
class Command(BaseCommand):
    help = "Fetch latest S&P 500 stock data"

    def handle(self, *args, **kwargs):
        stocks.utils.fetch_sp500_data()
        self.stdout.write(self.style.SUCCESS('Successfully updated stock data'))
