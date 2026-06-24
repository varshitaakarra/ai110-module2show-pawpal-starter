# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**
- CORE actions: add pet under the profile, give a rundown of the pet's daily schedule so the app doesn't disrupt it if the pet is already grown and be able to add pet tasks. 

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?
- Classes: 
Pet: 
-Attributes: name, species, age
-Methods: describe()
Owner:
-Attributes: name, available_minutes
-Methods: has_time_for_task()
Task:
-Attributes: title, duration_mins, priority, category 
-Methods: is_high_priority(), repr()
Schedule: 
-Attributes: pet, owner, tasks
-Methods: add_task(), remove_task(), total_duration(), fits_in_budget()
Scheduler:
-Attributes: none
-Methods: ort_by_priority(), filter_to_time_budget(), build_plan(), explain()

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
