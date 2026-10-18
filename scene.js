// Quick content edits. New apps and calendar details also require editing index.html.
const SCENE = {
  "autoStartDelayMs": 5000,
  "notification": {
    "title": "Your flight is delayed",
    "body": "UA 2385 to Los Angeles now arrives at 4:50 PM, 2 hours later than scheduled."
  },
  "thoughts": {
    "initial": {
      "title": "I’ll check what this affects.",
      "body": "Your flight is now arriving two hours later."
    },
    "conflict": {
      "title": "Your pickup needs to move.",
      "body": "3:15 PM pickup · 4:50 PM arrival. I’ll prepare an update for Alex."
    },
    "sending": {
      "title": "Sending Alex the new pickup time.",
      "body": "Requesting a 5:15 PM pickup to match your new arrival."
    }
  },
  "message": "Hi Alex, my flight is delayed by two hours. Could you pick me up at 5:15 PM instead?",
  "report": {
    "title": "Your flight is delayed by two hours.",
    "body": "UA 2385 now arrives at LAX at 4:50 PM. Your pickup was set for 3:15 PM, so I messaged Alex to request 5:15 PM instead.",
    "arrival": "4:50 PM",
    "pickup": "5:15 PM · Alex"
  },
  "steps": [
    "Reading the flight notification",
    "Unlocking your phone",
    "Opening Calendar",
    "Checking the pickup details",
    "Opening Messages",
    "Finding Alex’s conversation",
    "Writing the pickup update",
    "Sending the message to Alex"
  ]
};
