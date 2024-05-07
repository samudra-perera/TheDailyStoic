import { format } from "date-fns";

function formatDate(date: Date): string {
  const dayOfMonth = parseInt(format(date, "d"), 10);
  let suffix = "th";

  const j = dayOfMonth % 10;
  const k = dayOfMonth % 100;

  if (j === 1 && k !== 11) {
    suffix = "st";
  } else if (j === 2 && k !== 12) {
    suffix = "nd";
  } else if (j === 3 && k !== 13) {
    suffix = "rd";
  }

  return `${format(date, "MMMM")}_${dayOfMonth}${suffix}`;
}

export default formatDate;
