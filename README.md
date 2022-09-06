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

Get secret stars
```
      - name: print
        run: |
          echo $CANDY_SECURE
        env:
          CANDY_SECURE: ${{ secrets.IICS_USERNAME}}
```

There are several places where one can save secrets: org, env, repo. Repo worked for me. 

There are several places in code where one can get secrets: env of code, env of jobs. Env worked for me.
