FROM archlinux
RUN pacman --noconfirm -Syyu
RUN pacman --noconfirm -S base-devel
RUN pacman --noconfirm -S python3
RUN useradd builder
RUN pacman --noconfirm -S sudo
RUN echo "builder ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
RUN pacman --noconfirm -S rsync


