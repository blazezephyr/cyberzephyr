import time
import sys
import logging

logger = logging.getLogger(__name__)

def monthName(num):
	try:
		if not isinstance(num, int) or num < 1 or num > 12:
			raise ValueError(f"Invalid month number: {num}")
		
		months = {
			1: "January",
			2: "February",
			3: "March",
			4: "April",
			5: "May",
			6: "June",
			7: "July",
			8: "August",
			9: "September",
			10: "October",
			11: "November",
			12: "December"
		}
		return months.get(num, "Unknown")
	except Exception as e:
		logger.error(f"Error in monthName: {e}")
		print(f"[!] Error: Invalid month - {e}")
		time.sleep(2)
		print(" Exiting...")
		sys.exit(1)