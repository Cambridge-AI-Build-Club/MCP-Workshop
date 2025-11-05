from datetime import datetime
from typing import List, Dict

from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("EventCalendar")

# In-memory storage for events
# Each event is a dict: {"title": str, "date": str, "description": str}
events: List[Dict] = []


@mcp.tool()
def add_event(title: str, date: str, description: str = "") -> str:
    """Add an event to the calendar.

    Args:
        title: Event title
        date: Date in YYYY-MM-DD format (e.g., 2025-11-08 for November 8th, 2025)
        description: Optional event description
    """
    try:
        # Validate date format
        datetime.strptime(date, "%Y-%m-%d")
        events.append({"title": title, "date": date, "description": description})
        return f"Event '{title}' added for {date}."
    except ValueError:
        return "Invalid date format. Use YYYY-MM-DD (e.g., 2025-11-08)."


@mcp.tool()
def view_events() -> str:
    """View all events in the calendar.

    Returns all scheduled events sorted by date.
    """
    if not events:
        return "No events scheduled."
    result = "Calendar Events:\n"
    for event in sorted(events, key=lambda x: x["date"]):
        desc = f" - {event['description']}" if event['description'] else ""
        result += f"- {event['date']}: {event['title']}{desc}\n"
    return result


@mcp.tool()
def delete_event(title: str) -> str:
    """Delete an event from the calendar by title.

    Args:
        title: Title of the event to delete (case-insensitive)
    """
    initial_length = len(events)
    events[:] = [e for e in events if e["title"].lower() != title.lower()]
    if len(events) < initial_length:
        return f"Event '{title}' deleted."
    else:
        return f"No event found with title '{title}'."


@mcp.prompt()
def summarize_events() -> str:
    """Generate a summary of all upcoming events.

    Returns a formatted summary of all scheduled events sorted by date.
    """
    if not events:
        return "No events scheduled."
    summary = "Upcoming Events Summary:\n"
    for e in sorted(events, key=lambda x: x["date"]):
        summary += f"- {e['date']}: {e['title']}"
        if e['description']:
            summary += f" ({e['description']})"
        summary += "\n"
    return summary


if __name__ == "__main__":
    mcp.run()
