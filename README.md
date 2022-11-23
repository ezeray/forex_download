# Forex Download - Personal Project

## Intro

This is a personal project to test out some ideas by putting them into practice, in particular about process design and architecture.

## Design

The process at this time aims to extract the available currency exchange rates from YahooFinance, and insert them into a PostgreSQL database in an incremental manner. Additionally, the process will do some transformations on these rates to make sure they all follow the same structure, using the USD as the baseline.

With the extraction the process will also collect metadata to ensure control of the process, e.g., ensuring that download links are still available, if new currencies show up in YF, etc.

Finally, this will be deployed in a docker container.

## Timeline Estimate

- 2022-11-23 - 2022-11-25: finalize design, aprox. 3 hours total
- 2022-11-28 - 2022-12-02: code, aprox. 8 hours total
- 2022-12-05 - 2022-12-10: QA and review

