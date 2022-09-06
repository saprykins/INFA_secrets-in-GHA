# INFA_secrets-in-GHA

It's created to check option of password store in GitHub Actions

Basic echo command, py-script launcher
```
jobs:
  connect:
    name: connection check
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Login to development
        run: |
            python ./scripts/infa_login.py   
      - name: print
        run: |
            echo "testing"
```
