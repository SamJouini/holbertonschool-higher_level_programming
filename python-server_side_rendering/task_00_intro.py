import os


def generate_invitations(template, attendees):
    # Check input types
    if not isinstance(template, str):
        return ("Template must be a string")

    if not isinstance(attendees, list) or \
            not all(isinstance(a, dict) for a in attendees):
        return ("Attendees must be a list of dictionaries")

    # Handle empty inputs
    if not template:
        return ("Template is empty, no output files generated.")

    if not attendees:
        return ("No data provided, no output files generated.")

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Replace placeholders with attendee data,
        # using 'N/A' for missing values
        invitation = template.format(
            name=attendee.get("name", "N/A") or "N/A",
            event_title=attendee.get("event_title", "N/A") or "N/A",
            event_date=attendee.get("event_date", "N/A") or "N/A",
            event_location=attendee.get("event_location", "N/A") or "N/A"
        )

        # Generate output file
        filename = "output_{}.txt".format(index)
        with open(filename, 'w') as file:
            file.write(invitation)

        print("Generated invitation for {} in\
             {}".format(attendee.get('name', 'N/A'), filename))
