  FROM alpine:3.16
  
  RUN apk add --no-cache git go=1.18.7-r0 vim bash build-base gcompat
  
  ENV GOROOT /usr/lib/go
  ENV GOPATH /go
  ENV PATH /go/bin:$PATH
  ENV EDITOR vim
  # ENV KEG_CURRENT=zet keg "$@"

  # Install keg
  RUN go install github.com/rwxrob/keg/cmd/keg@latest

  # Set the default working directory
  WORKDIR zet
  # Configure Git
  RUN git config --global user.email "reg1nt1z@gmail.com" && \
      git config --global user.name "AugustasV" && \
      git config --global credential.helper store

  # Copy the repository into the container
  COPY . /zet
  CMD ["sh"]
