from models import AssistantResponse
from openai import OpenAI
from prompts import get_assistant_prompt
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_KEY"))

transcript='''
Alright, here’s the plan for today — I’ve got a stand-up meeting first thing in the morning, so just make sure I have everything I need prepped for that. I need to give a quick update on the first ML project — the one where the model’s been outputting NaNs during training. It’s probably due to unstable gradients again, so I want to carve out at least an hour after the stand-up to dive into that. Also, remind me to run the updated preprocessing script for the second project; I made changes to improve performance and need to compare the runtime against the old version.
In the afternoon, there’s a cross-team sync to talk about model integration. Can you block off some buffer time before and after the meeting in case it runs over or I need to jot down action items? I also need to review two pull requests before end of day — one from Amy and one from Raj. If you could surface those for me around 3 or so, that’d be perfect. I want to get through both without having to stay online late again.
Outside of work, I’ve got a tennis game with Sam and Josh at 6 PM — please set a reminder for that around 5:30 so I can start wrapping up in time. After tennis, I’m planning to cook dinner at home — I’ve got ingredients for a stir fry, and I don’t want them going to waste. If I end up running behind, just nudge me so I don’t cave and order takeout again. Let’s try to keep things tight today — it’s a lot, but I think I can get through it with a little structure. 
'''

response = client.responses.parse(
    model="gpt-4.1",
    input=get_assistant_prompt(transcript),
    text_format=AssistantResponse
)

print(response.output_text)

example_response = {
  "summary": "Today is a structured and busy day with a mix of technical work and meetings, balanced by a planned evening of tennis and a homemade dinner. The client has prioritized clearing up urgent work issues—like debugging an ML project and reviewing key PRs—while also maintaining personal commitments. The tone is focused and determined, aiming for balance and efficiency.",
  "todos": [
    {
      "task": "Prepare materials for morning stand-up meeting",
      "priority": "high",
      "tag": "work"
    },
    {
      "task": "Give an update on ML project 1 during stand-up (NaN issue)",
      "priority": "high",
      "tag": "work"
    },
    {
      "task": "Investigate NaNs in ML project 1 (check for unstable gradients)",
      "priority": "high",
      "tag": "work"
    },
    {
      "task": "Run updated preprocessing script for ML project 2 and compare runtimes",
      "priority": "medium",
      "tag": "work"
    },
    {
      "task": "Attend cross-team sync on model integration",
      "priority": "high",
      "tag": "meeting"
    },
    {
      "task": "Review Amy’s pull request",
      "priority": "medium",
      "tag": "code review"
    },
    {
      "task": "Review Raj’s pull request",
      "priority": "medium",
      "tag": "code review"
    },
    {
      "task": "Play tennis with Sam and Josh",
      "priority": "medium",
      "tag": "personal"
    },
    {
      "task": "Cook stir fry at home for dinner",
      "priority": "low",
      "tag": "personal"
    }
  ],
  "calendar_events": [
    {
      "summary": "Morning Stand-Up Meeting",
      "dtstart": "09:00",
      "dtend": "09:30",
      "description": "Prepare and give update on ML project 1 (NaN issue)."
    },
    {
      "summary": "Debug ML project 1 NaNs",
      "dtstart": "09:30",
      "dtend": "10:30",
      "description": "Investigate unstable gradients and NaN outputs in model."
    },
    {
      "summary": "Run preprocessing script & compare runtimes (ML project 2)",
      "dtstart": "10:30",
      "dtend": "11:00",
      "description": "Test updated script and record performance."
    },
    {
      "summary": "Cross-Team Sync: Model Integration",
      "dtstart": "13:30",
      "dtend": "14:30",
      "description": "Participate in discussion; buffer time before and after for overflow and action items."
    },
    {
      "summary": "Buffer for meeting overflow or notes",
      "dtstart": "13:00",
      "dtend": "13:30",
      "description": "Prep for cross-team sync."
    },
    {
      "summary": "Buffer for follow-up after sync",
      "dtstart": "14:30",
      "dtend": "15:00",
      "description": "Capture action items and ensure no overrun."
    },
    {
      "summary": "Review Amy’s and Raj’s PRs",
      "dtstart": "15:00",
      "dtend": "16:00",
      "description": "Review and provide feedback on two pull requests."
    },
    {
      "summary": "Tennis with Sam & Josh",
      "dtstart": "18:00",
      "dtend": "19:30",
      "description": "Recreational tennis—wrap up work and arrive on time."
    },
    {
      "summary": "Cook Stir Fry Dinner",
      "dtstart": "20:00",
      "dtend": "20:30",
      "description": "Home-cooked meal to use ingredients on hand."
    }
  ],
  "reminders": [
    "Surface Amy’s and Raj’s PRs around 3 PM for review.",
    "Remind to run updated preprocessing script for project 2.",
    "Send tennis reminder at 5:30 PM.",
    "Nudge to start cooking dinner after tennis to avoid takeout.",
    "Capture action items from the cross-team sync."
  ]
}