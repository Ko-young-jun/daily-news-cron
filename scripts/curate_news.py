name: Daily News Curation
on:
  schedule:
    - cron: '0 7 * * *'
    - cron: '0 12 * * *'
    - cron: '0 17 * * *'
jobs:
  curate-news:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: echo "Workflow test successful"
