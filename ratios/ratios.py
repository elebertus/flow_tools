import click


class FlowCli:
    pass


flow_cli = click.make_pass_decorator(FlowCli, ensure=True)


@click.group()
@flow_cli
@click.pass_context
def cli(ctx, flow_cli_base):
    ctx.obj = FlowTools()


class FlowTools(FlowCli):
    def __init__(self) -> None:
        super().__init__()
        pass

    @cli.command(
        "ratio",
        help="Used to calculate the flow modifier"
        " using the orca slicer flow calibration tool",
    )
    @click.argument("current_value")
    @click.argument("modifier")
    @flow_cli
    def ratio_modifier(self, current_value: int, modifier: int) -> None:
        new_flow: float = round(float(current_value) * (100 + float(modifier)) / 100, 4)
        click.echo(
            f"new flow value: {new_flow} \n{new_flow} = {current_value} * (100 + {modifier}) / 100"
        )

    @cli.command(
        "e-steps",
        help=("Used to calculate e-steps tuning. Measurement of a given length of filament"
        " (typically 120mm), print 100mm, and measure the remaining. The value is then calculated"
        " with the current e-steps"),
    )
    @click.argument("measured_value")
    @click.argument("remaining_value")
    @click.argument("current_steps")
    @flow_cli
    def e_steps(
        self, measured_value: int, remaining_value: int, current_steps: int
    ) -> None:
        new_steps: float = round(float(current_steps) * (
            100 / round( (float(measured_value) - float(remaining_value)) , 4)
        ), 4)
        click.echo(
            f"new e-steps value: {new_steps}\n {new_steps} = {current_steps} * (100 / ({measured_value} - {remaining_value})"
        )
