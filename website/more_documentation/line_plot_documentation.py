from typing import Dict

from nicegui import ui


def main_demo() -> None:
    from datetime import datetime

    import numpy as np

    line_plot = ui.line_plot(n=2, limit=20, figsize=(3, 2), update_every=5) \
        .with_legend(['sin', 'cos'], loc='upper center', ncol=2)

    def update_line_plot() -> None:
        now = datetime.now()
        x = now.timestamp()
        y1 = np.sin(x)
        y2 = np.cos(x)
        line_plot.push([now], [[y1], [y2]])

    line_updates = ui.timer(0.1, update_line_plot, active=False)
    line_checkbox = ui.checkbox('active').bind_value(line_updates, 'active')

    # END OF DEMO
    def handle_change(msg: Dict) -> None:
        def turn_off() -> None:
            line_checkbox.set_value(False)
            ui.notify('Turning off that line plot to save resources on our live demo server. 😎')
        line_checkbox.value = msg['args']
        if line_checkbox.value:
            ui.timer(10.0, turn_off, once=True)
    line_checkbox.on('update:model-value', handle_change)
