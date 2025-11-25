# Meeting Notes Examples

## Example 1: Standup from Transcript

### Input (Transcript)
```
Alice: Hey everyone, quick standup. I'll go first. Yesterday I finished the auth 
module refactor, finally. Today I'm starting on the payment integration. No blockers.

Bob: Nice! I'm still working on the dashboard components. Had some issues with the 
chart library yesterday but figured it out. Today continuing on that, should be 
done by end of day. Oh, I do need design review on the layout before I can finalize.

Carol: I was out yesterday. Today catching up on PRs and then starting the API 
documentation. Bob, I can do that design review after standup if you want.

Bob: Perfect, thanks Carol!

Alice: Great, anything else? No? Cool, back to work everyone.
```

### Output (Meeting Notes)
```markdown
# Daily Standup — Dec 10, 2024

**Attendees:** Alice, Bob, Carol

## Updates

### Alice
- Yesterday: Completed auth module refactor
- Today: Starting payment integration
- Blockers: None

### Bob
- Yesterday: Dashboard components, resolved chart library issues
- Today: Finishing dashboard (ETA: EOD)
- Blockers: Needs design review (Carol to help)

### Carol
- Yesterday: Out
- Today: PR reviews, then API documentation
- Blockers: None

## Action Items
- [ ] @carol: Design review for Bob's dashboard layout — After standup
```

---

## Example 2: Team Meeting from Notes

### Input (Raw Notes)
```
Product planning meeting
Dec 12, Sarah facilitating
Me, Sarah, Tom, Lisa present

Discussed Q1 roadmap
- Tom wants to prioritize mobile app
- Lisa concerned about resources
- Decided to do mobile MVP first, full version Q2

API deprecation timeline
- v1 sunset date: March 31
- Need to notify customers
- Tom volunteered to draft comms

Budget review pushed to next week - Lisa out

Next steps: Tom drafts customer email, Sarah updates roadmap doc
```

### Output (Meeting Notes)
```markdown
# Product Planning Meeting — Dec 12, 2024

**Attendees:** Sarah (facilitator), Tom, Lisa, [Author]  
**Duration:** ~45 min

## Discussion

### Q1 Roadmap
Tom proposed prioritizing mobile app development. Lisa raised concerns about 
resource constraints for a full build in Q1.

**Decision:** Mobile MVP in Q1, full version pushed to Q2.

### API v1 Deprecation
Timeline established for API v1 sunset.

**Decision:** Sunset date is March 31. Customer notification required.

### Budget Review
Deferred to next week (Lisa unavailable).

## Decisions Made
- Mobile: MVP in Q1, full version Q2
- API v1 sunset: March 31, 2024

## Action Items
- [ ] @tom: Draft customer notification email — Dec 15
- [ ] @sarah: Update roadmap document — Dec 13

## Next Meeting
Budget review next week (date TBD)
```

---

## Example 3: Extracting Action Items Only

### Input
```
Long meeting about various things. Key takeaways: 
Mike needs to fix the deployment pipeline by Friday.
The team agreed to switch to weekly releases starting January.
Anna will prepare the Q4 report and send to stakeholders by Dec 20.
We need someone to own the documentation refresh - to be decided in Slack.
Jake mentioned he'll look into the performance issues when he has time.
```

### Output (Action Items Only)
```markdown
## Action Items

**With Deadlines:**
- [ ] @mike: Fix deployment pipeline — Friday
- [ ] @anna: Prepare Q4 report and send to stakeholders — Dec 20

**Pending Assignment:**
- [ ] @TBD: Own documentation refresh — Decide in Slack

**No Deadline (Track):**
- [ ] @jake: Investigate performance issues — When available

**Team Commitment:**
- Switch to weekly releases starting January
```

---

## Quality Comparison

### ❌ Poor Notes
```
We talked about stuff. Bob said something about the API. 
There were concerns. We'll figure it out later.
```

**Problems:** Vague, no specifics, no actions, no owners

### ✅ Good Notes
```
## API Migration Discussion

Bob proposed migrating to GraphQL for better mobile performance.
Concerns raised about learning curve and timeline.

**Decision:** Spike investigation (2 days) before committing.

**Action:** @bob: Complete GraphQL spike — Dec 15
```

**Why it works:** Specific, actionable, owner assigned, deadline set
