# seafowl-dagster-demo

An example project demonstrating how to submit data to Seafowl from a dagster job.

# Getting started
This demo builds on the official [hello dagster demo](https://docs.dagster.io/getting-started/hello-dagster).

## Seafowl setup

To try the code in this project, you will need access to a [Seafowl](https://seafowl.io/) database instance. The easiest solution is to run seafowl locally after [downloading the release from GitHub](https://github.com/splitgraph/seafowl/releases/latest). The following shell commands install Seafowl version 0.4.1 for x86\_64-based macs:
```bash
curl -O -L 'https://github.com/splitgraph/seafowl/releases/download/v0.4.1/seafowl-v0.4.1-x86_64-apple-darwin.tar.gz'
tar -xzvf seafowl-v0.4.1-x86_64-apple-darwin.tar.gz
./seafowl
```

## Python setup

You will also need a python installation containing [dagster](https://dagster.io/) and the [python seafowl client](https://github.com/splitgraph/seafowl/tree/main/examples/clients/python).

The following commands create such a virtualenv for you:

```bash
python3 -m venv venv
. venv/bin/activate
pip install -e 'git+https://git@github.com/splitgraph/seafowl.git@main#egg=seafowl[pandas]&subdirectory=examples/clients/python'
pip install dagster dagit
```

# Starting dagster

```bash
# be sure to active the virtualenv first
. venv/bin/activate
dagster dev -f demo.py
```

# Querying Seafowl
```bash
# be sure to active the virtualenv first
. venv/bin/activate
# also, make sure 'seafowl' is running
PASSWORD="iHBHflYfEaMpX4j7Du0z6vFNS6w2BMaX" ENDPOINT="http://127.0.0.1:8080/q" python -m seafowl "SELECT * FROM hn"
```
