# seafowl-dagster-demo
An example project demonstrating how to submit data to Seafowl from a dagster job.

# Getting started
To try the code in this project, you will need access to a [Seafowl](https://seafowl.io/) database instance.

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
