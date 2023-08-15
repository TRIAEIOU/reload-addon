# Reload addon

Minimal [Anki](https://ankiweb.net) [addon]() ([source](https://github.com/TRIAEIOU/reload-addon)) for addon developers that allow selecting an addon and reload it from main window menu or shortcut (main window) to avoid having to restart Anki during addon development.

## Usage

1. Select addon from `Main window` → `Reload addon: select addon` or configured shortut (default `none`).
2. Reload the addon from `Main window` → `Reload <addon name>` or configured shortcut (default `Ctrl+R`)

Note that depending on how the addon is written reloading may or may not do what you expect/want. For instance if the addon initiation logic is hooked on, say, `main_window_did_init`, that logic wont run on reload.

## Configuration

In addon configuration:

- `Reload shortcut`: Shortcut to reload the selected addon
- `Select shortcut`: Shortcut to open select addon dialog
- `Internal state`: Addon internal state, do not edit
