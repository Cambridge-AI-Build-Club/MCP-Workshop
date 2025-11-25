# Testing Prompts for Demo Skills

Use these prompts to test the demo skills during your workshop. Each section includes direct triggers, implicit triggers, and edge cases.

---

## Testing: code-review Skill

### Direct Triggers (Should definitely activate the skill)

**Test 1: Explicit code review request**
```
Can you review this Python code for me?

def get_user(id):
    query = f"SELECT * FROM users WHERE id = {id}"
    result = db.execute(query)
    return result[0]
```

**Expected behavior:**
- Skill activates
- Identifies SQL injection vulnerability
- Notes missing error handling
- Follows structured output format (Summary, Critical Issues, etc.)

---

**Test 2: Pull request review**
```
Review this PR diff:

- def connect():
-     return db.connect(timeout=30)
+ def connect():
+     return db.connect()
```

**Expected behavior:**
- Recognizes this as code review context
- Notes the removed timeout (potential issue)
- Asks about or flags the change's intent

---

**Test 3: Security-focused review**
```
Check this authentication code for security issues:

def login(username, password):
    user = db.query(f"SELECT * FROM users WHERE username='{username}'")
    if user and user.password == password:
        return create_token(user.id)
    return None
```

**Expected behavior:**
- Should reference SECURITY.md content
- Identifies: SQL injection, plain text password comparison
- Provides severity ratings

---

### Implicit Triggers (Should still activate)

**Test 4: "What do you think of this code?"**
```
What do you think of this implementation?

class UserService:
    def __init__(self):
        self.cache = {}
    
    def get_user(self, id):
        if id in self.cache:
            return self.cache[id]
        user = fetch_from_db(id)
        self.cache[id] = user
        return user
```

**Expected:** Should recognize as code review request

---

**Test 5: "Is this okay?"**
```
Is this JavaScript okay?

async function fetchData() {
    const response = await fetch(url);
    return response.json();
}
```

**Expected:** Reviews code, notes missing error handling

---

### Edge Cases

**Test 6: Multiple languages**
```
Review both of these:

Python:
items = []
for i in range(10):
    items.append(lambda: i)

JavaScript:
for (var i = 0; i < 10; i++) {
    setTimeout(() => console.log(i), 100);
}
```

**Expected:** Should reference PATTERNS.md, identify closure issues in both

---

**Test 7: Minimal code**
```
Review this: x = x + 1
```

**Expected:** Should still provide useful feedback (could use +=) without over-engineering the response

---

## Testing: meeting-notes Skill

### Direct Triggers

**Test 1: Standup transcript**
```
Turn this into meeting notes:

"Okay quick standup. I finished the API integration yesterday, today I'm working on tests. Sarah, you're up."
"Thanks. I'm still on the frontend refactor, hit a bug with state management. Might need help from Mike."
"I can look at it after standup. I was reviewing PRs yesterday, continuing today, no blockers."
"Great, let's sync at 2pm about that bug. Anything else? No? Back to work!"
```

**Expected behavior:**
- Recognizes standup format
- Uses standup template from TEMPLATES.md
- Extracts: Yesterday/Today/Blockers for each person
- Creates action item: sync at 2pm about bug

---

**Test 2: Formal meeting minutes**
```
Create board meeting minutes from this:

Meeting called to order at 9am by Chair Williams.
Present: Williams, Chen, Patel, Morrison. Absent: Baker.
Treasurer Chen presented Q3 financials showing 12% revenue growth.
Morrison moved to approve the budget. Chen seconded. Passed unanimously.
Williams proposed expanding to European markets in Q2.
Discussion about resource requirements. Tabled for next meeting.
Adjourned at 10:30am.
```

**Expected behavior:**
- Recognizes formal meeting format
- Uses board meeting template
- Properly formats motions with mover/seconder
- Notes tabled items

---

**Test 3: Extract action items only**
```
Just give me the action items from this:

We discussed the product launch. Marketing will prepare the press release by Friday. Engineering needs to finish the landing page - John's taking that. We should probably get legal review but nobody volunteered. Sarah mentioned she'd look into competitor pricing when she has time. The launch date is confirmed for Jan 15.
```

**Expected behavior:**
- Extracts action items in standard format
- Identifies: Marketing (press release, Friday), John (landing page)
- Flags: legal review (no owner), Sarah's task (no deadline)
- Notes the decision: launch date Jan 15

---

### Implicit Triggers

**Test 4: "Summarize this meeting"**
```
Summarize this meeting recording transcript:

[Long transcript about product planning...]
```

**Expected:** Should use meeting-notes skill, pick appropriate template

---

**Test 5: "What were the takeaways?"**
```
What were the key takeaways from this discussion?

Alice: I think we should switch to TypeScript.
Bob: That's a big change. What's the timeline?
Alice: Maybe 3 months? We'd need to update the build system first.
Bob: Okay, let's do a proof of concept first. I can lead that.
Alice: Perfect. Let's check in next week.
```

**Expected:** Extracts decisions and action items

---

### Edge Cases

**Test 6: Retrospective format**
```
Document our sprint retro:

What went well: deployments were smooth, good collaboration
What didn't: too many meetings, unclear requirements on the auth feature
Actions: reduce meetings to 3/week, PM to write better specs
Shoutout to Sarah for fixing the production bug at midnight
```

**Expected:** Uses retrospective template from TEMPLATES.md

---

**Test 7: Messy/informal notes**
```
Clean up my meeting notes:

talked about q4 goals
- revenue target 2M
- hire 3 engineers
- launch mobile app
john wants to delay mobile to q1, pushed back by sarah
decided: mobile stays in q4 but reduced scope
TODO: john to define mvp scope by wed
```

**Expected:** Structures properly, identifies decision and action item with deadline

---

## Skill Discovery Tests

These test whether Claude correctly identifies WHEN to use the skills.

**Test A: Should NOT trigger code-review**
```
Write a Python function that calculates factorial.
```
**Expected:** Writes code, doesn't review it unless asked

---

**Test B: Should NOT trigger meeting-notes**
```
What's the best way to run effective meetings?
```
**Expected:** Gives advice, doesn't try to create meeting notes

---

**Test C: Ambiguous - could be either**
```
Here's what happened in our code review meeting:
[Transcript discussing code changes]
```
**Expected:** Should prioritize meeting-notes (it's about documenting a meeting)

---

## Evaluation Rubric

For each test, score on:

| Criteria | Score (1-5) |
|----------|-------------|
| Skill correctly triggered | |
| Used appropriate template/format | |
| Extracted key information | |
| Output was actionable | |
| Appropriate level of detail | |

**Total: ___ / 25**

### Scoring Guide
- **23-25:** Skill working excellently
- **18-22:** Good, minor improvements needed
- **13-17:** Functional but needs iteration
- **Below 13:** Major issues, revisit skill design
