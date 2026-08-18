# Data Sources

Pick **one** domain in `SCENARIOS.md`, then use only that domain's folder
below — delete the other 3 from your own repo once you've chosen (see
`README.md`). Every file here is real data (or, for `professional_services`,
clearly-labeled synthetic data) — nothing was invented to make an example
come out cleanly. Every table below is already linkable by a real foreign
key; your job is to design the schema that expresses that link correctly,
not to fix broken data (that's Module 2's territory, not this one's).

## finance_insurance — FEMA NFIP flood insurance (South Carolina)

**Source:** OpenFEMA API v3, `NfipPolicies` and `NfipClaims` datasets
(`https://www.fema.gov/api/open/v3/NfipPolicies`,
`.../v3/NfipClaims`), filtered to South Carolina. **License:** U.S.
Government Work, public domain under 17 U.S.C. §105; usage governed by
OpenFEMA's Terms & Conditions (`fema.gov/about/openfema/terms-conditions`).
Pulled live from the API, not a static download.

- `communities.csv` (131 rows) — one row per NFIP-rated community:
  `community_number`, `community_name`, `state`.
- `policies.csv` (4,000 rows) — `policy_id`, `community_number` (FK),
  `policy_effective_date`, `policy_termination_date`, `policy_cost`,
  `total_building_coverage`, `total_contents_coverage`, `rated_flood_zone`,
  `occupancy_type`, `zip_code`.
- `claims.csv` (3,000 rows) — `claim_id`, `community_number` (FK),
  `date_of_loss`, `cause_of_damage`, `occupancy_type`,
  `amount_paid_building`, `amount_paid_contents`, `building_damage_amount`,
  `net_building_payment`, `zip_code`.

**Real wrinkle worth knowing before you design your schema:** FEMA does
**not** publish a policyholder-level or individual-claim-to-individual-
policy link (redacted under the Privacy Act of 1974) — there's no real way
to build a `policyholders` table that actually joins to both. The real,
verifiable link between `policies` and `claims` is at the **community**
grain: both tables carry `community_number`, which is what
`communities.csv` exists for. Design your schema around that real
relationship, not an individual-policyholder one.

**Also real:** `cause_of_damage` is FEMA's own numeric/letter code, given
as-is — the dataset doesn't publish a code lookup table alongside it, and
none is invented here. 36 claims have no code at all (blank in the source).
`amount_paid_building`/`amount_paid_contents`/`building_damage_amount` are
genuinely missing on several hundred claims — real nulls, not something
scrubbed out. `date_of_loss` spans back to 1978 (filtered by state only,
not by year) — expect a wide real date range, not a single tidy year.

## public_sector — NYC 311 service requests

**Source:** NYC Open Data, "311 Service Requests from 2010 to Present"
(Socrata dataset `erm2-nwe9`,
`https://data.cityofnewyork.us/resource/erm2-nwe9.json`), the **most recent
~6,000 requests** as of when this project was built (spans roughly the
prior 12 hours of citywide 311 activity — NYC 311 volume is high). **License:**
NYC Open Data Law — public domain city government data.

- `agencies.csv` (13 rows) — `agency_code`, `agency_name` (NYPD, HPD,
  DOHMH, DOT, DSNY, and others — the real set of agencies that appear in
  this sample, not the full citywide list).
- `service_requests.csv` (6,000 rows) — `request_id`, `created_date`,
  `closed_date`, `agency_code` (FK), `complaint_type`, `descriptor`,
  `status`, `borough`.

**Real wrinkle:** because this sample is deliberately the most *recent*
activity (not a random historical slice), a genuinely large share —
**2,320 of 6,000 requests (about 39%)** — have no `closed_date` yet: they're
real, currently-open cases, not missing data. That's exactly what makes
"open-case backlog ranked by agency" a real question with a real answer
here, not a hypothetical.

## healthcare_operations — Synthea synthetic patient records

**Source:** Synthea (`synthea.mitre.org`), the open-source synthetic
patient generator maintained by MITRE — the sample pull used here is the
publicly published `synthea_sample_data_csv_nov2021.zip` from
`github.com/synthetichealth/synthea-sample-data`. **License:** the Synthea
generator itself is Apache License 2.0; every record is **entirely
synthetic** — no real patient's data is used or representable, which is
Synthea's whole purpose (there is no real, public, patient-level healthcare
dataset that could ethically stand in here — real patient records are
HIPAA-protected, which is exactly why a project like this can't use one).

- `patients.csv` (1,033 rows) — `patient_id`, `birthdate`, `deathdate`
  (**154 of 1,033 patients have one — the other 879 are alive as of the
  data, so this column is genuinely null on purpose, not missing**),
  `marital_status`, `race`, `ethnicity`, `gender`, `city`, `state`, `county`.
- `facilities.csv` (804 rows) — `facility_id`, `facility_name`, `city`,
  `state`, `zip_code`. (Synthea calls these "organizations" — healthcare
  systems/hospitals, not internal hospital departments; there's no real
  publicly-available internal-department-level breakdown, so this project
  uses "facility" as the department-like grouping instead. Said plainly in
  `SCENARIOS.md` too, not just here.)
- `encounters.csv` (5,000 rows, a random sample of Synthea's full
  61,460-row encounter set) — `encounter_id`, `start_time`, `stop_time`,
  `patient_id` (FK), `facility_id` (FK), `encounter_class` (wellness,
  ambulatory, outpatient, urgentcare, emergency, inpatient),
  `description`, `total_claim_cost`.

**Real wrinkle:** `start_time`/`stop_time` are genuine timestamps (not just
dates) generated across a patient's whole simulated lifetime — some go back
to the early 1900s for older synthetic patients. Computing length-of-stay
means subtracting two real timestamps, not just comparing dates.

## professional_services — synthetic (clearly labeled)

**No public billable-hours/client-engagement dataset exists** — a real
consulting firm's time-tracking data is exactly the kind of thing no
organization publishes. Generated with `numpy`/`pandas`, seed 42, documented
here rather than pretending it's real.

- `clients.csv` (60 rows) — `client_id`, `client_name`, `industry`,
  `region`. **2 of the 60 clients have zero engagements** — a real
  left-join case, not an error.
- `engagements.csv` (220 rows) — `engagement_id`, `client_id` (FK),
  `service_type`, `partner_assigned`, `hourly_rate` (varies by
  `service_type` — Management Consulting bills highest, Audit lowest, real
  ranges documented in-file), `start_date`, `end_date` (**27 engagements
  are still ongoing — `end_date` is blank on purpose**, not missing data).
- `time_entries.csv` (4,000 rows) — `time_entry_id`, `engagement_id` (FK),
  `entry_date`, `hours`, `billable`.

**Planted realism (documented, not hidden):** `hours` is drawn from a
right-skewed (lognormal) distribution, not a flat range — most entries are
small, a few are large. **6 rows have a negative `hours` value** (planted
data-entry errors — real time-tracking systems get these) and **160 rows
have a missing `hours` value** (~4%).
