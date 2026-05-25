# Daily Morning Extract Scenario

## Business Request

An analyst needs a daily morning extract for operations. Each weekday morning,
the extract should list open service tickets created yesterday, include the
assigned team and customer priority, exclude test tickets, and flag tickets
that have no assigned owner. The query should be readable and efficient enough
for a recurring scheduled job.

Ask Copilot to classify the request with the general SQL chain, route to
business-logic mapping where needed, draft efficient SQL only after the mapping
is clear, and propose result-validation checks before the extract is accepted.

## Tiny Generic Schema Context

| Table | Important columns | Notes |
| --- | --- | --- |
| `service_tickets` | `ticket_id`, `customer_id`, `assigned_user_id`, `created_at`, `status`, `is_test_ticket` | One row per ticket. Open statuses are `NEW`, `IN_PROGRESS`, and `WAITING`. |
| `customers` | `customer_id`, `customer_name`, `priority_code` | One row per customer. |
| `users` | `user_id`, `team_id`, `user_name`, `active_flag` | One row per user. Some tickets may have no assigned user. |
| `teams` | `team_id`, `team_name` | One row per team. |

Expected output grain: one row per qualifying service ticket.

Known risks: date-window boundaries for "yesterday", optional assigned owner,
test-ticket exclusion, and accidental row loss from joins.

## Expected Chain To Use

Start with `prompt-chains/sql-general/`.

Expected routing:

- Use `prompt-chains/sql-logic-mapping/` to clarify business rules, field
  mappings, output grain, date window, exclusions, and owner flag logic.
- Use `prompt-chains/sql-efficiency/` to draft readable Oracle SQL after the
  logic map is accepted and to review avoidable inefficiency.
- Use `prompt-chains/sql-result-validation/` once SQL exists or is being
  finalized, especially for row counts, date boundaries, duplicates, null owner
  checks, and join row preservation.

## Expected Copilot Behaviors

- Classifies the request as a broad SQL build that needs routing rather than a
  single immediate final query.
- Builds a logic map before SQL, including status rules, yesterday date window,
  test-ticket exclusion, owner flag, joins, and output columns.
- Preserves tickets with missing assigned users by using optional joins where
  appropriate.
- Drafts Oracle SQL only after the mapping is clear, using date predicates that
  can use an index on `created_at`.
- Reviews efficiency risks such as functions applied to indexed date columns
  in row filters, unnecessary selected columns, and duplicate-prone joins.
- Proposes result-validation checks for row counts, one row per `ticket_id`,
  yesterday boundaries, excluded test tickets, open status inclusion, missing
  owner counts, and unmatched customer or team joins.

## Unacceptable Copilot Behaviors

- Skips classification and routing and immediately returns final SQL.
- Invents hidden scheduling tables, credentials, private operational fields, or
  real ticket data.
- Uses joins that drop unassigned tickets even though missing owners must be
  flagged.
- Uses vague date logic that does not define yesterday's start and end
  boundaries.
- Treats runtime efficiency as plan-based tuning without any plan evidence.
- Claims result correctness without analyst-run validation evidence.

## Manual Pass/Fail Checklist

| Check | Pass/Fail |
| --- | --- |
| Copilot started from or clearly followed the general SQL chain. |  |
| Copilot routed to logic mapping before final SQL. |  |
| Copilot routed to efficiency review for the recurring extract query. |  |
| Copilot routed to result validation once SQL existed or was being finalized. |  |
| Copilot preserved unassigned tickets and produced an owner-missing flag. |  |
| Copilot defined yesterday's date boundaries clearly. |  |
| Copilot proposed row-count, duplicate, boundary, exclusion, and null checks. |  |
| Copilot avoided private schema details, credentials, and real data. |  |

