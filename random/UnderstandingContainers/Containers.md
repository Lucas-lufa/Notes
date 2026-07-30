# Containers

## podman

### Mac

==> Caveats
In order to run containers locally, podman depends on a Linux kernel.
One can be started manually using `podman machine` from this package.
To start a podman VM automatically at login, also install the cask
"podman-desktop".

## vs code

### cs50

https://cs50.readthedocs.io/cs50.dev/
- Download CS50’s latest .devcontainer.json file from https://cs50.dev/.devcontainer.json, saving it in folder.
- Download, install, and start Docker on your computer.
- Download and install VS Code itself on your computer.
- Install VS Code’s Dev Containers extension.
- Open VS Code’s command palette, as via Ctrl+Shift+P on Linux, ⇧⌘P on macOS, and Ctrl+Shift+P on Windows, select >Dev Containers - Open Folder in Container…, and open folder.

- Alternatively, select >Dev Containers: Install devcontainer CLI, and then, in VS Code’s terminal window, cd to folder and execute devcontainer open .


Once the container finishes building and starting, you should find that foo is mounted within the container at /workspaces/folder.