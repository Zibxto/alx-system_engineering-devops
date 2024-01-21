![500 error page](https://github.com/zibxto/alx-system_engineering-devops/0x19-postmortem/500_error.jpg)


## Issue Summary

- **Duration:**
  - Start Time: January 21, 2024, 14:30 UTC
  - End Time: January 21, 2024, 16:30 UTC
- **Impact:**
  - Web application outage
  - 25% decrease in user engagement
- **Root Cause:**
  - An unexpected spike in database connections surpassed the configured limit, causing a cascading failure.

## Timeline

- **Detection:**
  - January 21, 2024, 14:30 UTC
  - Automated monitoring alerts triggered due to increased server errors.
- **Actions Taken:**
  - Immediate investigation into web server logs and database metrics.
  - Initial assumption: DDoS attack due to sudden traffic surge.
- **Misleading Paths:**
  - Explored network configurations and firewalls.
  - Investigated recent code deployments.
- **Escalation:**
  - Incident escalated to senior engineering team after 30 minutes.
- **Resolution:**
  - Identified root cause as database connection limit exceeded.
  - Temporary fix: Adjusted database connection pool size.
  - Long-term fix: Database optimizations and infrastructure scaling.

## Root Cause and Resolution

- **Root Cause:**
  - Database connection pool set too low, leading to maxed-out connections during peak usage.
- **Resolution:**
  - Short-term: Adjusted database connection pool size.
  - Long-term: Implemented database optimizations and upgraded infrastructure.

## Corrective and Preventative Measures

- **Improvements/Fixes:**
  - Optimize database queries and indexing.
  - Review connection pool configurations for critical services.
  - Enhance monitoring alerts for abnormal traffic or connections.
  - Develop incident response plan.

- **Tasks:**
  - Patch database server software.
  - Conduct post-mortem meeting with engineering team.
  - Establish regular incident response training sessions.
  - Implement automated scaling for critical components.
