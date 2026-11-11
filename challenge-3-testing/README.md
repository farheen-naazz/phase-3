# CHALLENGE 3 - AUTOMATED TESTING

Marks: 15

## INCIDENT

The inventory application is calculating incorrect
customer order totals after applying discounts.

The automated testing team has reported failures.

Your responsibility is to diagnose the defect and restore
correct application behavior.

## FILES

pricing.py
tests/test_pricing.py

## STEP 1 - INSPECT THE APPLICATION

Open pricing.py.

Understand how the final order price is calculated.

## STEP 2 - RUN THE AUTOMATED TESTS

Open a terminal inside challenge-3-testing.

Run:

python -m unittest discover -s tests -v

Some tests are expected to fail.

## STEP 3 - INVESTIGATE

Read the expected values in test_pricing.py.

Compare expected results with the actual application output.

Identify the incorrect calculation.

## STEP 4 - FIX THE APPLICATION

Correct the pricing logic in pricing.py.

Do not:
- Delete automated tests.
- Change expected test values.
- Bypass test execution.

## STEP 5 - VALIDATE

Run:

python -m unittest discover -s tests -v

All five tests should pass.

## SUBMISSION

Submit:
1. Root cause.
2. Incorrect calculation.
3. Corrected formula.
4. Passing test output.
5. Commit hash of your fix.

## COMPLETION

FLAG: Not required for this challenge.
Your working code and passing test evidence are your submission.