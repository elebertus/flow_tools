# Flow Tools

Python cli utility for calculating simple FDM tuning values. I end up using a python repl to calculate these regularly so why not write some python.

## Building
```git clone https://github.com/elebertus/flow_tools
cd flow_tools
python -m venv venv
. venv/bin/activate
pip install .
```

### Example
```
$ flow_tools --help
Usage: flow_tools [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  e-steps  Used to calculate e-steps tuning.
  ratio    Used to calculate the flow modifier using the orca slicer flow...

$ flow_tools e-steps 120 18.41 691.50
new e-steps value: 680.6772
 680.6772 = 691.50 * (100 / (120 - 18.41)

$  flow_tools ratio 1 5
new flow value: 1.05
1.05 = 1 * (100 + 5) / 100
```
