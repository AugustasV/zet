# Devcontainer/Devpod with Alpine image fix

Sometimes I use DevPod for local development environment inside container, with VSCode web interface. By default it doesnt work with Alpine images.
Solution is to add extra packages inside docker image

`apk add bash build-base gcompat git`

Source: [Minimal alpine container with VSCode fails with missing bash](https://github.com/loft-sh/devpod/issues/557#issuecomment-1661652920)
