# pre-commit-config-updater

This library acts as a pre-commit hook configuration updater.

If you include it in your pre-commit hook, the configuration files found within this repo will be downloaded locally.
Thus if you track these configurations in git, then pre-commit step will fail and force a re-run with the new versions.

## Usage

First make sure `pre-commit` is installed somewhere in your python environment:

    pip install pre-commit

To add pre-commit hooks to your repo locally run:

    pre-commit install

To have a new repo use these configurations, you must do a one-time copy of the `.pre-commit-config.yaml` found here
to your repo.
