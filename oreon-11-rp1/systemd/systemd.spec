%global source0_hash 100fc873b848b9b0297d8a705e8e2ed326256c8483d9960ee1ffe264c8a5c3e3
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: systemd
Version: 262.1
Release: 2%{?dist}
Summary: System and service manager
License: LGPL-2.1-or-later AND GPL-2.0-or-later
URL: https://systemd.io/
Source0: https://github.com/systemd/systemd/archive/refs/tags/v%{version}.tar.gz
Requires: systemd-libs%{?_isa} = %{version}-%{release}
Requires: systemd-udev%{?_isa} = %{version}-%{release}
%if %{without bootstrap} && !0%{?bootstrap}
Requires: systemd-pam%{?_isa} = %{version}-%{release}
%endif

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: glibc-devel
BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: pkgconf
BuildRequires: patchelf
BuildRequires: gperf
BuildRequires: python3
BuildRequires: libcap-devel
BuildRequires: libxcrypt-devel
BuildRequires: libmount-devel
BuildRequires: libblkid-devel
BuildRequires: libselinux-devel
BuildRequires: libacl-devel
BuildRequires: openssl-devel
BuildRequires: zlib-devel
BuildRequires: bzip2-devel
BuildRequires: xz-devel
BuildRequires: lz4-devel
BuildRequires: libzstd-devel
BuildRequires: libarchive-devel
BuildRequires: pcre2-devel
BuildRequires: libseccomp-devel
BuildRequires: audit-libs-devel
BuildRequires: libmicrohttpd-devel
BuildRequires: libcurl-devel
BuildRequires: libidn2-devel
BuildRequires: libgcrypt-devel
BuildRequires: gnutls-devel
BuildRequires: p11-kit-devel
BuildRequires: elfutils-devel
BuildRequires: python3-jinja2
BuildRequires: libfdisk-devel
BuildRequires: gettext
BuildRequires: kmod-devel
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: dbus-devel
BuildRequires: glib2-devel
BuildRequires: cryptsetup-devel
BuildRequires: pam-devel
BuildRequires: libpwquality-devel
%endif

%description
systemd is the system and service manager.

%package libs
Summary: Libraries for systemd

%description libs
Libraries for systemd.

%package pam
Summary: systemd PAM modules
Requires: systemd%{?_isa} = %{version}-%{release}

%description pam
systemd PAM modules.

%package rpm-macros
Summary: Macros for systemd units
BuildArch: noarch

%description rpm-macros
Macros for systemd units.

%package udev
Summary: udev and related system services
Requires: systemd%{?_isa} = %{version}-%{release}

%description udev
udev and related system services.

%package container
Summary: Tools for containers and VMs
Requires: systemd%{?_isa} = %{version}-%{release}

%description container
Tools for containers and VMs.

%package networkd
Summary: System daemon that manages network configuration
Requires: systemd%{?_isa} = %{version}-%{release}

%description networkd
System daemon that manages network configuration.

%package resolved
Summary: Network name resolution manager
Requires: systemd%{?_isa} = %{version}-%{release}

%description resolved
Network name resolution manager.

%package journal-remote
Summary: Tools to send journal events over the network
Requires: systemd%{?_isa} = %{version}-%{release}

%description journal-remote
Tools to send journal events over the network.

%package devel
Summary: Development headers for systemd
Requires: systemd-libs%{?_isa} = %{version}-%{release}

%description devel
systemd is the system and service manager.

%prep
%oreon_sha256
%autosetup -n systemd-%{version} -p1
sed -i 's/EDEADLOCK|EWOULDBLOCK|ENOTSUP/EDEADLOCK|EWOULDBLOCK|ENOTSUP|EFSBADCRC|EFSCORRUPTED/' src/basic/errno-to-name.awk
sed -i "s#command : \[ bpftool, 'btf', 'dump', 'file', '/sys/kernel/btf/vmlinux', 'format', 'c' \],#command : [ 'sh', '-c', '\"\$1\" btf dump file /sys/kernel/btf/vmlinux format c | sed \"/bpf_stream_vprintk/d\"', 'gen-vmlinux', bpftool ],#" meson.build

%build
%global sd_cyc %[(%{with bootstrap} || 0%{?bootstrap}) ? "disabled" : "enabled"]
%oreon_meson \
  -Dmode=release \
  -Dlog-message-verification=disabled \
  -Dtests=false \
  -Dfuzz-tests=false \
  -Dinstall-tests=false \
  -Dtranslations=true \
  -Defi=true \
  -Dtpm=false \
  -Dstatic-libsystemd=false \
  -Dstatic-libudev=false \
  -Dbpf-framework=disabled \
  -Dapparmor=disabled \
  -Daudit=enabled \
  -Dlibcryptsetup=%{sd_cyc} \
  -Dlibcryptsetup-plugins=%{sd_cyc} \
  -Dmicrohttpd=enabled \
  -Dlibcurl=enabled \
  -Dlibidn2=enabled \
  -Dqrencode=disabled \
  -Dgcrypt=enabled \
  -Dgnutls=enabled \
  -Dp11kit=enabled \
  -Dlibfido2=disabled \
  -Dtpm2=disabled \
  -Delfutils=enabled \
  -Dxkbcommon=disabled \
  -Dbootloader=disabled \
  -Dukify=disabled \
  -Dhomed=%{sd_cyc} \
  -Dremote=enabled \
  -Dimportd=enabled \
  -Dvmspawn=enabled \
  -Drepart=enabled \
  -Dsysupdate=enabled \
  -Dpolkit=disabled \
  -Dseccomp=enabled \
  -Dfdisk=enabled \
  -Dxenctrl=disabled \
  -Dpwquality=%{sd_cyc} \
  -Dpasswdqc=disabled \
  -Dpam=%{sd_cyc} \
  -Dsysupdated=enabled \
  -Ddns-over-tls=openssl \
  -Dnss-mymachines=enabled \
  -Dnss-resolve=enabled \
  -Dresolve=true \
  -Dselinux=enabled \
  -Dacl=enabled \
  -Dopenssl=enabled \
  -Dzlib=enabled \
  -Dbzip2=enabled \
  -Dxz=enabled \
  -Dlz4=enabled \
  -Dzstd=enabled \
  -Dlibarchive=enabled \
  -Ddbus=%{sd_cyc} \
  -Dglib=%{sd_cyc} \
  -Dpcre2=enabled \
  -Dblkid=enabled \
  -Dkmod=enabled
%oreon_meson_build

%install
%oreon_meson_install
rm -f %{buildroot}%{_libdir}/*.a
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f")
  [ -n "$r" ] || continue
  keep=
  oldifs=$IFS
  IFS=:
  for p in $r; do
    case "$p" in
      /usr/lib64/systemd|/usr/lib/systemd) keep="${keep:+$keep:}$p" ;;
    esac
  done
  IFS=$oldifs
  [ "$keep" = "$r" ] && continue
  chmod u+w "$f"
  if [ -n "$keep" ]; then
    patchelf --set-rpath "$keep" "$f"
  else
    patchelf --remove-rpath "$f"
  fi
done
%find_lang systemd

%files -f systemd.lang
%license LICENSE.GPL2 LICENSE.LGPL2.1
%dir %{_prefix}/lib/systemd
%dir %{_prefix}/lib/systemd/system
%dir %{_prefix}/lib/systemd/user
%dir %{_prefix}/lib/systemd/system-generators
%dir %{_prefix}/lib/systemd/user-generators
%dir %{_prefix}/lib/systemd/network
%dir %{_libdir}/systemd
%dir %{_sysconfdir}/systemd
%dir %{_datadir}/systemd
%dir %{_datadir}/doc/systemd
%config(noreplace) %{_sysconfdir}/X11/xinit/xinitrc.d/50-systemd-user.sh
%config(noreplace) %{_sysconfdir}/profile.d/70-systemd-shell-extra.sh
%config(noreplace) %{_sysconfdir}/profile.d/80-systemd-osc-context.sh
%config(noreplace) %{_sysconfdir}/ssh/ssh_config.d/20-systemd-ssh-proxy.conf
%config(noreplace) %{_sysconfdir}/ssh/sshd_config.d/20-systemd-userdb.conf
%config(noreplace) %{_sysconfdir}/systemd/journald.conf
%config(noreplace) %{_sysconfdir}/systemd/logind.conf
%config(noreplace) %{_sysconfdir}/systemd/system.conf
%config(noreplace) %{_sysconfdir}/systemd/user.conf
%config(noreplace) %{_sysconfdir}/xdg/systemd/user
%{_bindir}/busctl
%{_bindir}/halt
%{_bindir}/hostnamectl
%{_bindir}/init
%{_bindir}/journalctl
%{_bindir}/localectl
%{_bindir}/loginctl
%{_bindir}/mount.mstack
%{_bindir}/mount.storage
%{_bindir}/oomctl
%{_bindir}/poweroff
%{_bindir}/reboot
%{_bindir}/resolvectl
%{_bindir}/run0
%{_bindir}/shutdown
%{_bindir}/storagectl
%{_bindir}/systemctl
%{_bindir}/systemd-analyze
%{_bindir}/systemd-ask-password
%{_bindir}/systemd-cat
%{_bindir}/systemd-cgls
%{_bindir}/systemd-cgtop
%{_bindir}/systemd-confext
%{_bindir}/systemd-creds
%{_bindir}/systemd-delta
%{_bindir}/systemd-detect-virt
%{_bindir}/systemd-escape
%{_bindir}/systemd-firstboot
%{_bindir}/systemd-id128
%{_bindir}/systemd-inhibit
%{_bindir}/systemd-machine-id-setup
%{_bindir}/systemd-mount
%{_bindir}/systemd-mstack
%{_bindir}/systemd-mute-console
%{_bindir}/systemd-notify
%{_bindir}/systemd-path
%{_bindir}/systemd-pty-forward
%{_bindir}/systemd-run
%{_bindir}/systemd-socket-activate
%{_bindir}/systemd-stdio-bridge
%{_bindir}/systemd-sysext
%{_bindir}/systemd-sysusers
%{_bindir}/systemd-tmpfiles
%{_bindir}/systemd-tty-ask-password-agent
%{_bindir}/systemd-umount
%{_bindir}/systemd-vpick
%{_bindir}/timedatectl
%{_bindir}/userdbctl
%{_bindir}/varlinkctl
%{_prefix}/lib/environment.d/99-environment.conf
%{_prefix}/lib/systemd/catalog/
%{_prefix}/lib/systemd/import-pubring.pgp
%{_prefix}/lib/systemd/network/80-6rd-tunnel.link
%{_prefix}/lib/systemd/network/80-container-vb.link
%{_prefix}/lib/systemd/network/80-container-ve.link
%{_prefix}/lib/systemd/network/80-container-vz.link
%{_prefix}/lib/systemd/network/80-namespace-ns-tun.link
%{_prefix}/lib/systemd/network/80-namespace-ns.link
%{_prefix}/lib/systemd/network/80-vm-vt.link
%{_prefix}/lib/systemd/profile.d/
%{_prefix}/lib/systemd/resolv.conf
%{_prefix}/lib/systemd/ssh_config.d/
%{_prefix}/lib/systemd/sshd_config.d/
%{_prefix}/lib/systemd/system-generators/systemd-clonesetup-generator
%{_prefix}/lib/systemd/system-generators/systemd-debug-generator
%{_prefix}/lib/systemd/system-generators/systemd-factory-reset-generator
%{_prefix}/lib/systemd/system-generators/systemd-fstab-generator
%{_prefix}/lib/systemd/system-generators/systemd-getty-generator
%{_prefix}/lib/systemd/system-generators/systemd-run-generator
%{_prefix}/lib/systemd/system-generators/systemd-ssh-generator
%{_prefix}/lib/systemd/system-generators/systemd-system-update-generator
%{_prefix}/lib/systemd/system-preset/
%{_prefix}/lib/systemd/system/basic.target
%{_prefix}/lib/systemd/system/blockdev@.target
%{_prefix}/lib/systemd/system/bluetooth.target
%{_prefix}/lib/systemd/system/boot-complete.target
%{_prefix}/lib/systemd/system/breakpoint-pre-basic.service
%{_prefix}/lib/systemd/system/breakpoint-pre-mount.service
%{_prefix}/lib/systemd/system/breakpoint-pre-switch-root.service
%{_prefix}/lib/systemd/system/capsule.slice
%{_prefix}/lib/systemd/system/capsule@.service
%{_prefix}/lib/systemd/system/clonesetup.target
%{_prefix}/lib/systemd/system/console-getty.service
%{_prefix}/lib/systemd/system/container-getty@.service
%{_prefix}/lib/systemd/system/ctrl-alt-del.target
%{_prefix}/lib/systemd/system/dbus-org.freedesktop.hostname1.service
%{_prefix}/lib/systemd/system/dbus-org.freedesktop.locale1.service
%{_prefix}/lib/systemd/system/dbus-org.freedesktop.login1.service
%{_prefix}/lib/systemd/system/dbus-org.freedesktop.timedate1.service
%{_prefix}/lib/systemd/system/debug-shell.service
%{_prefix}/lib/systemd/system/default.target
%{_prefix}/lib/systemd/system/dev-hugepages.mount
%{_prefix}/lib/systemd/system/dev-mqueue.mount
%{_prefix}/lib/systemd/system/emergency.service
%{_prefix}/lib/systemd/system/emergency.target
%{_prefix}/lib/systemd/system/exit.target
%{_prefix}/lib/systemd/system/factory-reset-now.target
%{_prefix}/lib/systemd/system/factory-reset.target
%{_prefix}/lib/systemd/system/factory-reset.target.wants/
%{_prefix}/lib/systemd/system/final.target
%{_prefix}/lib/systemd/system/first-boot-complete.target
%{_prefix}/lib/systemd/system/getty-pre.target
%{_prefix}/lib/systemd/system/getty.target
%{_prefix}/lib/systemd/system/getty@.service
%{_prefix}/lib/systemd/system/graphical.target
%{_prefix}/lib/systemd/system/halt.target
%{_prefix}/lib/systemd/system/imports-pre.target
%{_prefix}/lib/systemd/system/imports.target
%{_prefix}/lib/systemd/system/kexec.target
%{_prefix}/lib/systemd/system/ldconfig.service
%{_prefix}/lib/systemd/system/local-fs-pre.target
%{_prefix}/lib/systemd/system/local-fs.target
%{_prefix}/lib/systemd/system/local-fs.target.wants/
%{_prefix}/lib/systemd/system/modprobe@.service
%{_prefix}/lib/systemd/system/multi-user.target
%{_prefix}/lib/systemd/system/multi-user.target.wants/
%{_prefix}/lib/systemd/system/network-online.target
%{_prefix}/lib/systemd/system/network-pre.target
%{_prefix}/lib/systemd/system/network.target
%{_prefix}/lib/systemd/system/nss-lookup.target
%{_prefix}/lib/systemd/system/nss-user-lookup.target
%{_prefix}/lib/systemd/system/paths.target
%{_prefix}/lib/systemd/system/poweroff.target
%{_prefix}/lib/systemd/system/printer.target
%{_prefix}/lib/systemd/system/reboot.target
%{_prefix}/lib/systemd/system/remote-fs-pre.target
%{_prefix}/lib/systemd/system/remote-fs.target
%{_prefix}/lib/systemd/system/rescue.service
%{_prefix}/lib/systemd/system/rescue.target
%{_prefix}/lib/systemd/system/rpcbind.target
%{_prefix}/lib/systemd/system/runlevel0.target
%{_prefix}/lib/systemd/system/runlevel1.target
%{_prefix}/lib/systemd/system/runlevel2.target
%{_prefix}/lib/systemd/system/runlevel3.target
%{_prefix}/lib/systemd/system/runlevel4.target
%{_prefix}/lib/systemd/system/runlevel5.target
%{_prefix}/lib/systemd/system/runlevel6.target
%{_prefix}/lib/systemd/system/serial-getty@.service
%{_prefix}/lib/systemd/system/shutdown.target
%{_prefix}/lib/systemd/system/sigpwr.target
%{_prefix}/lib/systemd/system/slices.target
%{_prefix}/lib/systemd/system/smartcard.target
%{_prefix}/lib/systemd/system/sockets.target
%{_prefix}/lib/systemd/system/sockets.target.wants/systemd-ask-password.socket
%{_prefix}/lib/systemd/system/sockets.target.wants/systemd-creds.socket
%{_prefix}/lib/systemd/system/sockets.target.wants/systemd-factory-reset.socket
%{_prefix}/lib/systemd/system/sockets.target.wants/systemd-hostnamed.socket
%{_prefix}/lib/systemd/system/sockets.target.wants/systemd-journalctl.socket
%{_prefix}/lib/systemd/system/sockets.target.wants/systemd-journald-dev-log.socket
%{_prefix}/lib/systemd/system/sockets.target.wants/systemd-journald.socket
%{_prefix}/lib/systemd/system/sockets.target.wants/systemd-logind-varlink.socket
%{_prefix}/lib/systemd/system/sockets.target.wants/systemd-mute-console.socket
%{_prefix}/lib/systemd/system/sockets.target.wants/systemd-storage-block.socket
%{_prefix}/lib/systemd/system/sockets.target.wants/systemd-storage-fs.socket
%{_prefix}/lib/systemd/system/sockets.target.wants/systemd-sysext.socket
%{_prefix}/lib/systemd/system/soft-reboot.target
%{_prefix}/lib/systemd/system/sound.target
%{_prefix}/lib/systemd/system/ssh-access.target
%{_prefix}/lib/systemd/system/storage-target-mode.target
%{_prefix}/lib/systemd/system/swap.target
%{_prefix}/lib/systemd/system/sys-fs-fuse-connections.mount
%{_prefix}/lib/systemd/system/sys-kernel-config.mount
%{_prefix}/lib/systemd/system/sys-kernel-debug.mount
%{_prefix}/lib/systemd/system/sys-kernel-tracing.mount
%{_prefix}/lib/systemd/system/sysinit.target
%{_prefix}/lib/systemd/system/sysinit.target.wants/clonesetup.target
%{_prefix}/lib/systemd/system/sysinit.target.wants/dev-hugepages.mount
%{_prefix}/lib/systemd/system/sysinit.target.wants/dev-mqueue.mount
%{_prefix}/lib/systemd/system/sysinit.target.wants/imports.target
%{_prefix}/lib/systemd/system/sysinit.target.wants/ldconfig.service
%{_prefix}/lib/systemd/system/sysinit.target.wants/sys-fs-fuse-connections.mount
%{_prefix}/lib/systemd/system/sysinit.target.wants/sys-kernel-config.mount
%{_prefix}/lib/systemd/system/sysinit.target.wants/sys-kernel-debug.mount
%{_prefix}/lib/systemd/system/sysinit.target.wants/sys-kernel-tracing.mount
%{_prefix}/lib/systemd/system/sysinit.target.wants/systemd-ask-password-console.path
%{_prefix}/lib/systemd/system/sysinit.target.wants/systemd-firstboot.service
%{_prefix}/lib/systemd/system/sysinit.target.wants/systemd-journal-catalog-update.service
%{_prefix}/lib/systemd/system/sysinit.target.wants/systemd-journal-flush.service
%{_prefix}/lib/systemd/system/sysinit.target.wants/systemd-journald.service
%{_prefix}/lib/systemd/system/sysinit.target.wants/systemd-machine-id-commit.service
%{_prefix}/lib/systemd/system/sysinit.target.wants/systemd-sysusers.service
%{_prefix}/lib/systemd/system/sysinit.target.wants/systemd-tmpfiles-setup.service
%{_prefix}/lib/systemd/system/sysinit.target.wants/systemd-update-done.service
%{_prefix}/lib/systemd/system/sysinit.target.wants/systemd-update-utmp.service
%{_prefix}/lib/systemd/system/syslog.socket
%{_prefix}/lib/systemd/system/system-install.target
%{_prefix}/lib/systemd/system/system-systemd\x2dmute\x2dconsole.slice
%{_prefix}/lib/systemd/system/system-update-cleanup.service
%{_prefix}/lib/systemd/system/system-update-pre.target
%{_prefix}/lib/systemd/system/system-update.target
%{_prefix}/lib/systemd/system/systemd-ask-password-console.path
%{_prefix}/lib/systemd/system/systemd-ask-password-console.service
%{_prefix}/lib/systemd/system/systemd-ask-password-wall.path
%{_prefix}/lib/systemd/system/systemd-ask-password-wall.service
%{_prefix}/lib/systemd/system/systemd-ask-password.socket
%{_prefix}/lib/systemd/system/systemd-ask-password@.service
%{_prefix}/lib/systemd/system/systemd-battery-check.service
%{_prefix}/lib/systemd/system/systemd-boot-check-no-failures.service
%{_prefix}/lib/systemd/system/systemd-confext-initrd.service
%{_prefix}/lib/systemd/system/systemd-confext-sysroot.service
%{_prefix}/lib/systemd/system/systemd-confext.service
%{_prefix}/lib/systemd/system/systemd-creds.socket
%{_prefix}/lib/systemd/system/systemd-creds@.service
%{_prefix}/lib/systemd/system/systemd-exit.service
%{_prefix}/lib/systemd/system/systemd-factory-reset-complete.service
%{_prefix}/lib/systemd/system/systemd-factory-reset-reboot.service
%{_prefix}/lib/systemd/system/systemd-factory-reset-request.service
%{_prefix}/lib/systemd/system/systemd-factory-reset.socket
%{_prefix}/lib/systemd/system/systemd-factory-reset@.service
%{_prefix}/lib/systemd/system/systemd-firstboot.service
%{_prefix}/lib/systemd/system/systemd-halt.service
%{_prefix}/lib/systemd/system/systemd-hostnamed.service
%{_prefix}/lib/systemd/system/systemd-hostnamed.socket
%{_prefix}/lib/systemd/system/systemd-journal-catalog-update.service
%{_prefix}/lib/systemd/system/systemd-journal-flush.service
%{_prefix}/lib/systemd/system/systemd-journalctl-metrics.socket
%{_prefix}/lib/systemd/system/systemd-journalctl-metrics@.service
%{_prefix}/lib/systemd/system/systemd-journalctl.socket
%{_prefix}/lib/systemd/system/systemd-journalctl@.service
%{_prefix}/lib/systemd/system/systemd-journald-audit.socket
%{_prefix}/lib/systemd/system/systemd-journald-dev-log.socket
%{_prefix}/lib/systemd/system/systemd-journald-sync@.service
%{_prefix}/lib/systemd/system/systemd-journald-varlink@.socket
%{_prefix}/lib/systemd/system/systemd-journald.service
%{_prefix}/lib/systemd/system/systemd-journald.socket
%{_prefix}/lib/systemd/system/systemd-journald@.service
%{_prefix}/lib/systemd/system/systemd-journald@.socket
%{_prefix}/lib/systemd/system/systemd-kexec.service
%{_prefix}/lib/systemd/system/systemd-localed.service
%{_prefix}/lib/systemd/system/systemd-logind-varlink.socket
%{_prefix}/lib/systemd/system/systemd-logind.service
%{_prefix}/lib/systemd/system/systemd-machine-id-commit.service
%{_prefix}/lib/systemd/system/systemd-machine-tag@.service
%{_prefix}/lib/systemd/system/systemd-mute-console.socket
%{_prefix}/lib/systemd/system/systemd-mute-console@.service
%{_prefix}/lib/systemd/system/systemd-poweroff.service
%{_prefix}/lib/systemd/system/systemd-reboot.service
%{_prefix}/lib/systemd/system/systemd-report-basic.socket
%{_prefix}/lib/systemd/system/systemd-report-basic@.service
%{_prefix}/lib/systemd/system/systemd-report-cgroup.socket
%{_prefix}/lib/systemd/system/systemd-report-cgroup@.service
%{_prefix}/lib/systemd/system/systemd-report-files.socket
%{_prefix}/lib/systemd/system/systemd-report-files@.service
%{_prefix}/lib/systemd/system/systemd-report-sign-plain.socket
%{_prefix}/lib/systemd/system/systemd-report-sign-plain@.service
%{_prefix}/lib/systemd/system/systemd-report-sign-tsm.socket
%{_prefix}/lib/systemd/system/systemd-report-sign-tsm@.service
%{_prefix}/lib/systemd/system/systemd-report.socket
%{_prefix}/lib/systemd/system/systemd-report@.service
%{_prefix}/lib/systemd/system/systemd-soft-reboot.service
%{_prefix}/lib/systemd/system/systemd-storage-block.socket
%{_prefix}/lib/systemd/system/systemd-storage-block@.service
%{_prefix}/lib/systemd/system/systemd-storage-fs.socket
%{_prefix}/lib/systemd/system/systemd-storage-fs@.service
%{_prefix}/lib/systemd/system/systemd-storagetm.service
%{_prefix}/lib/systemd/system/systemd-sysext-initrd.service
%{_prefix}/lib/systemd/system/systemd-sysext-sysroot.service
%{_prefix}/lib/systemd/system/systemd-sysext.service
%{_prefix}/lib/systemd/system/systemd-sysext.socket
%{_prefix}/lib/systemd/system/systemd-sysext@.service
%{_prefix}/lib/systemd/system/systemd-sysusers.service
%{_prefix}/lib/systemd/system/systemd-time-wait-sync.service
%{_prefix}/lib/systemd/system/systemd-timedated.service
%{_prefix}/lib/systemd/system/systemd-tmpfiles-clean.service
%{_prefix}/lib/systemd/system/systemd-tmpfiles-clean.timer
%{_prefix}/lib/systemd/system/systemd-tmpfiles-setup.service
%{_prefix}/lib/systemd/system/systemd-update-done.service
%{_prefix}/lib/systemd/system/systemd-update-utmp.service
%{_prefix}/lib/systemd/system/systemd-user-sessions.service
%{_prefix}/lib/systemd/system/systemd-userdb-load-credentials.service
%{_prefix}/lib/systemd/system/systemd-userdbd.service
%{_prefix}/lib/systemd/system/systemd-userdbd.socket
%{_prefix}/lib/systemd/system/systemd-validatefs@.service
%{_prefix}/lib/systemd/system/time-set.target
%{_prefix}/lib/systemd/system/time-sync.target
%{_prefix}/lib/systemd/system/timers.target
%{_prefix}/lib/systemd/system/timers.target.wants/
%{_prefix}/lib/systemd/system/tmp.mount
%{_prefix}/lib/systemd/system/umount.target
%{_prefix}/lib/systemd/system/usb-gadget.target
%{_prefix}/lib/systemd/system/user-.slice.d/
%{_prefix}/lib/systemd/system/user-runtime-dir@.service
%{_prefix}/lib/systemd/system/user.slice
%{_prefix}/lib/systemd/system/user@.service
%{_prefix}/lib/systemd/system/user@.service.d/
%{_prefix}/lib/systemd/system/user@0.service.d/
%{_prefix}/lib/systemd/systemd
%{_prefix}/lib/systemd/systemd-battery-check
%{_prefix}/lib/systemd/systemd-boot-check-no-failures
%{_prefix}/lib/systemd/systemd-clonesetup
%{_prefix}/lib/systemd/systemd-executor
%{_prefix}/lib/systemd/systemd-factory-reset
%{_prefix}/lib/systemd/systemd-hostnamed
%{_prefix}/lib/systemd/systemd-journald
%{_prefix}/lib/systemd/systemd-keyutil
%{_prefix}/lib/systemd/systemd-localed
%{_prefix}/lib/systemd/systemd-logind
%{_prefix}/lib/systemd/systemd-reply-password
%{_prefix}/lib/systemd/systemd-report
%{_prefix}/lib/systemd/systemd-report-basic
%{_prefix}/lib/systemd/systemd-report-cgroup
%{_prefix}/lib/systemd/systemd-report-files
%{_prefix}/lib/systemd/systemd-report-sign-plain
%{_prefix}/lib/systemd/systemd-report-sign-tsm
%{_prefix}/lib/systemd/systemd-sbsign
%{_prefix}/lib/systemd/systemd-shutdown
%{_prefix}/lib/systemd/systemd-socket-proxyd
%{_prefix}/lib/systemd/systemd-ssh-issue
%{_prefix}/lib/systemd/systemd-ssh-proxy
%{_prefix}/lib/systemd/systemd-storage-block
%{_prefix}/lib/systemd/systemd-storage-fs
%{_prefix}/lib/systemd/systemd-storagetm
%{_prefix}/lib/systemd/systemd-sulogin-shell
%{_prefix}/lib/systemd/systemd-sysroot-fstab-check
%{_prefix}/lib/systemd/systemd-time-wait-sync
%{_prefix}/lib/systemd/systemd-timedated
%{_prefix}/lib/systemd/systemd-update-done
%{_prefix}/lib/systemd/systemd-update-helper
%{_prefix}/lib/systemd/systemd-update-utmp
%{_prefix}/lib/systemd/systemd-user-runtime-dir
%{_prefix}/lib/systemd/systemd-user-sessions
%{_prefix}/lib/systemd/systemd-userdbd
%{_prefix}/lib/systemd/systemd-userwork
%{_prefix}/lib/systemd/systemd-validatefs
%{_prefix}/lib/systemd/systemd-xdg-autostart-condition
%{_prefix}/lib/systemd/user-environment-generators/
%{_prefix}/lib/systemd/user-generators/systemd-xdg-autostart-generator
%{_prefix}/lib/systemd/user-preset/
%{_prefix}/lib/systemd/user/app.slice
%{_prefix}/lib/systemd/user/background.slice
%{_prefix}/lib/systemd/user/basic.target
%{_prefix}/lib/systemd/user/bluetooth.target
%{_prefix}/lib/systemd/user/capsule@.target
%{_prefix}/lib/systemd/user/default.target
%{_prefix}/lib/systemd/user/exit.target
%{_prefix}/lib/systemd/user/graphical-session-pre.target
%{_prefix}/lib/systemd/user/graphical-session.target
%{_prefix}/lib/systemd/user/paths.target
%{_prefix}/lib/systemd/user/printer.target
%{_prefix}/lib/systemd/user/session.slice
%{_prefix}/lib/systemd/user/shutdown.target
%{_prefix}/lib/systemd/user/smartcard.target
%{_prefix}/lib/systemd/user/sockets.target
%{_prefix}/lib/systemd/user/sockets.target.wants/systemd-ask-password.socket
%{_prefix}/lib/systemd/user/sockets.target.wants/systemd-journalctl.socket
%{_prefix}/lib/systemd/user/sockets.target.wants/systemd-storage-fs.socket
%{_prefix}/lib/systemd/user/sound.target
%{_prefix}/lib/systemd/user/systemd-ask-password.socket
%{_prefix}/lib/systemd/user/systemd-ask-password@.service
%{_prefix}/lib/systemd/user/systemd-exit.service
%{_prefix}/lib/systemd/user/systemd-journalctl.socket
%{_prefix}/lib/systemd/user/systemd-journalctl@.service
%{_prefix}/lib/systemd/user/systemd-storage-fs.socket
%{_prefix}/lib/systemd/user/systemd-storage-fs@.service
%{_prefix}/lib/systemd/user/systemd-tmpfiles-clean.service
%{_prefix}/lib/systemd/user/systemd-tmpfiles-clean.timer
%{_prefix}/lib/systemd/user/systemd-tmpfiles-setup.service
%{_prefix}/lib/systemd/user/timers.target
%{_prefix}/lib/systemd/user/xdg-desktop-autostart.target
%{_prefix}/lib/sysusers.d/README
%{_prefix}/lib/sysusers.d/basic.conf
%{_prefix}/lib/sysusers.d/systemd-journal.conf
%{_prefix}/lib/sysusers.d/systemd-oom.conf
%{_prefix}/lib/tmpfiles.d/20-systemd-osc-context.conf
%{_prefix}/lib/tmpfiles.d/20-systemd-shell-extra.conf
%{_prefix}/lib/tmpfiles.d/20-systemd-ssh-generator.conf
%{_prefix}/lib/tmpfiles.d/20-systemd-stub.conf
%{_prefix}/lib/tmpfiles.d/20-systemd-userdb.conf
%{_prefix}/lib/tmpfiles.d/20-systemd-varlink.conf
%{_prefix}/lib/tmpfiles.d/README
%{_prefix}/lib/tmpfiles.d/credstore.conf
%{_prefix}/lib/tmpfiles.d/etc.conf
%{_prefix}/lib/tmpfiles.d/home.conf
%{_prefix}/lib/tmpfiles.d/journal-nocow.conf
%{_prefix}/lib/tmpfiles.d/legacy.conf
%{_prefix}/lib/tmpfiles.d/provision.conf
%{_prefix}/lib/tmpfiles.d/root.conf
%{_prefix}/lib/tmpfiles.d/static-nodes-permissions.conf
%{_prefix}/lib/tmpfiles.d/systemd-nologin.conf
%{_prefix}/lib/tmpfiles.d/systemd-tmp.conf
%{_prefix}/lib/tmpfiles.d/systemd.conf
%{_prefix}/lib/tmpfiles.d/tmp.conf
%{_prefix}/lib/tmpfiles.d/var.conf
%{_prefix}/lib/tmpfiles.d/x11.conf
%{_libdir}/libnss_myhostname.so.2
%{_libdir}/libnss_resolve.so.2
%{_libdir}/libnss_systemd.so.2
%{_libdir}/systemd/libsystemd-core-262.so
%{_datadir}/bash-completion/completions/busctl
%{_datadir}/bash-completion/completions/hostnamectl
%{_datadir}/bash-completion/completions/journalctl
%{_datadir}/bash-completion/completions/localectl
%{_datadir}/bash-completion/completions/loginctl
%{_datadir}/bash-completion/completions/oomctl
%{_datadir}/bash-completion/completions/resolvectl
%{_datadir}/bash-completion/completions/run0
%{_datadir}/bash-completion/completions/storagectl
%{_datadir}/bash-completion/completions/systemctl
%{_datadir}/bash-completion/completions/systemd-analyze
%{_datadir}/bash-completion/completions/systemd-cat
%{_datadir}/bash-completion/completions/systemd-cgls
%{_datadir}/bash-completion/completions/systemd-cgtop
%{_datadir}/bash-completion/completions/systemd-confext
%{_datadir}/bash-completion/completions/systemd-creds
%{_datadir}/bash-completion/completions/systemd-delta
%{_datadir}/bash-completion/completions/systemd-detect-virt
%{_datadir}/bash-completion/completions/systemd-id128
%{_datadir}/bash-completion/completions/systemd-path
%{_datadir}/bash-completion/completions/systemd-run
%{_datadir}/bash-completion/completions/systemd-sysext
%{_datadir}/bash-completion/completions/systemd-vpick
%{_datadir}/bash-completion/completions/timedatectl
%{_datadir}/bash-completion/completions/userdbctl
%{_datadir}/bash-completion/completions/varlinkctl
%{_datadir}/dbus-1/interfaces/org.freedesktop.LogControl1.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.hostname1.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.locale1.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.login1.Manager.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.login1.Seat.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.login1.Session.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.login1.User.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.oom1.Manager.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.systemd1.Automount.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.systemd1.Device.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.systemd1.Job.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.systemd1.Manager.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.systemd1.Mount.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.systemd1.Path.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.systemd1.Scope.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.systemd1.Service.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.systemd1.Slice.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.systemd1.Socket.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.systemd1.Swap.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.systemd1.Target.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.systemd1.Timer.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.systemd1.Unit.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.timedate1.xml
%{_datadir}/dbus-1/services/org.freedesktop.systemd1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.hostname1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.locale1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.login1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.oom1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.systemd1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.timedate1.service
%{_datadir}/dbus-1/system.d/org.freedesktop.hostname1.conf
%{_datadir}/dbus-1/system.d/org.freedesktop.locale1.conf
%{_datadir}/dbus-1/system.d/org.freedesktop.login1.conf
%{_datadir}/dbus-1/system.d/org.freedesktop.oom1.conf
%{_datadir}/dbus-1/system.d/org.freedesktop.systemd1.conf
%{_datadir}/dbus-1/system.d/org.freedesktop.timedate1.conf
%{_datadir}/doc/systemd/ENVIRONMENT.md
%{_datadir}/doc/systemd/LICENSE.GPL2
%{_datadir}/doc/systemd/LICENSE.LGPL2.1
%{_datadir}/doc/systemd/LICENSES/
%{_datadir}/doc/systemd/NEWS
%{_datadir}/doc/systemd/README
%{_datadir}/doc/systemd/README.logs
%{_datadir}/doc/systemd/TRANSIENT-SETTINGS.md
%{_datadir}/doc/systemd/UIDS-GIDS.md
%{_datadir}/factory/etc/issue
%{_datadir}/factory/etc/locale.conf
%{_datadir}/factory/etc/nsswitch.conf
%{_datadir}/mime/packages/io.systemd.xml
%{_datadir}/pkgconfig/systemd.pc
%{_datadir}/pkgconfig/udev.pc
%{_datadir}/polkit-1/actions/io.systemd.ask-password.policy
%{_datadir}/polkit-1/actions/io.systemd.credentials.policy
%{_datadir}/polkit-1/actions/io.systemd.mount-file-system.policy
%{_datadir}/polkit-1/actions/io.systemd.namespace-resource.policy
%{_datadir}/polkit-1/actions/io.systemd.storage.policy
%{_datadir}/polkit-1/actions/io.systemd.sysext.policy
%{_datadir}/polkit-1/actions/io.systemd.sysinstall.policy
%{_datadir}/polkit-1/actions/org.freedesktop.hostname1.policy
%{_datadir}/polkit-1/actions/org.freedesktop.locale1.policy
%{_datadir}/polkit-1/actions/org.freedesktop.login1.policy
%{_datadir}/polkit-1/actions/org.freedesktop.systemd1.policy
%{_datadir}/polkit-1/actions/org.freedesktop.timedate1.policy
%{_datadir}/polkit-1/rules.d/10-systemd-logind-root-ignore-inhibitors.rules.example
%{_datadir}/systemd/kbd-model-map
%{_datadir}/systemd/language-fallback-map
%{_datadir}/user-tmpfiles.d/20-systemd-varlink.conf
%{_datadir}/zsh/site-functions/_busctl
%{_datadir}/zsh/site-functions/_hostnamectl
%{_datadir}/zsh/site-functions/_journalctl
%{_datadir}/zsh/site-functions/_localectl
%{_datadir}/zsh/site-functions/_loginctl
%{_datadir}/zsh/site-functions/_oomctl
%{_datadir}/zsh/site-functions/_resolvectl
%{_datadir}/zsh/site-functions/_run0
%{_datadir}/zsh/site-functions/_sd_bus_address
%{_datadir}/zsh/site-functions/_sd_hosts_or_user_at_host
%{_datadir}/zsh/site-functions/_sd_machines
%{_datadir}/zsh/site-functions/_sd_outputmodes
%{_datadir}/zsh/site-functions/_sd_unit_files
%{_datadir}/zsh/site-functions/_storagectl
%{_datadir}/zsh/site-functions/_systemctl
%{_datadir}/zsh/site-functions/_systemd
%{_datadir}/zsh/site-functions/_systemd-analyze
%{_datadir}/zsh/site-functions/_systemd-delta
%{_datadir}/zsh/site-functions/_systemd-id128
%{_datadir}/zsh/site-functions/_systemd-inhibit
%{_datadir}/zsh/site-functions/_systemd-path
%{_datadir}/zsh/site-functions/_systemd-run
%{_datadir}/zsh/site-functions/_systemd-tmpfiles
%{_datadir}/zsh/site-functions/_timedatectl
%{_datadir}/zsh/site-functions/_userdbctl
%{_datadir}/zsh/site-functions/_varlinkctl
%if %{without bootstrap} && !0%{?bootstrap}
%{_bindir}/systemd-home-fallback-shell
%{_prefix}/lib/pam.d/systemd-run0
%{_prefix}/lib/pam.d/systemd-user
%{_prefix}/lib/systemd/systemd-homework
%{_datadir}/factory/etc/pam.d/
%endif
%{_libdir}/systemd/libsystemd-shared-262.so

%files libs
%license LICENSE.LGPL2.1
%{_libdir}/libsystemd.so.0
%{_libdir}/libsystemd.so.0.45.0
%{_libdir}/libudev.so.1
%{_libdir}/libudev.so.1.7.15

%if %{without bootstrap} && !0%{?bootstrap}
%files pam

%{_libdir}/security/pam_systemd.so
%{_libdir}/security/pam_systemd_home.so
%{_libdir}/security/pam_systemd_loadkey.so
%endif

%files rpm-macros
%{_prefix}/lib/rpm/macros.d/macros.systemd

%files udev
%dir %{_prefix}/lib/udev
%dir %{_sysconfdir}/udev
%config(noreplace) %{_sysconfdir}/systemd/coredump.conf
%config(noreplace) %{_sysconfdir}/systemd/oomd.conf
%config(noreplace) %{_sysconfdir}/systemd/pstore.conf
%config(noreplace) %{_sysconfdir}/systemd/sleep.conf
%config(noreplace) %{_sysconfdir}/systemd/timesyncd.conf
%config(noreplace) %{_sysconfdir}/udev/iocost.conf
%config(noreplace) %{_sysconfdir}/udev/udev.conf
%{_bindir}/bootctl
%{_bindir}/coredumpctl
%{_bindir}/kernel-install
%{_bindir}/systemd-ac-power
%{_bindir}/systemd-hwdb
%{_bindir}/systemd-repart
%{_bindir}/systemd-sysinstall
%{_bindir}/udevadm
%{_bindir}/updatectl
%{_prefix}/lib/kernel/install.conf
%{_prefix}/lib/kernel/install.d/50-depmod.install
%{_prefix}/lib/kernel/install.d/90-loaderentry.install
%{_prefix}/lib/kernel/install.d/90-uki-copy.install
%{_prefix}/lib/modprobe.d/README
%{_prefix}/lib/modprobe.d/systemd.conf
%{_prefix}/lib/sysctl.d/50-coredump.conf
%{_prefix}/lib/sysctl.d/50-default.conf
%{_prefix}/lib/sysctl.d/50-pid-max.conf
%{_prefix}/lib/sysctl.d/README
%{_prefix}/lib/systemd/initrd-preset/
%{_prefix}/lib/systemd/network/99-default.link
%{_prefix}/lib/systemd/ntp-units.d/
%{_prefix}/lib/systemd/repart/
%{_prefix}/lib/systemd/system-generators/systemd-gpt-auto-generator
%{_prefix}/lib/systemd/system-generators/systemd-hibernate-resume-generator
%{_prefix}/lib/systemd/system-generators/systemd-imds-generator
%{_prefix}/lib/systemd/system/breakpoint-pre-udev.service
%{_prefix}/lib/systemd/system/dbus-org.freedesktop.sysupdate1.service
%{_prefix}/lib/systemd/system/hibernate.target
%{_prefix}/lib/systemd/system/hybrid-sleep.target
%{_prefix}/lib/systemd/system/initrd-cleanup.service
%{_prefix}/lib/systemd/system/initrd-fs.target
%{_prefix}/lib/systemd/system/initrd-parse-etc.service
%{_prefix}/lib/systemd/system/initrd-root-device.target
%{_prefix}/lib/systemd/system/initrd-root-device.target.wants/
%{_prefix}/lib/systemd/system/initrd-root-fs.target
%{_prefix}/lib/systemd/system/initrd-root-fs.target.wants/
%{_prefix}/lib/systemd/system/initrd-switch-root.service
%{_prefix}/lib/systemd/system/initrd-switch-root.target
%{_prefix}/lib/systemd/system/initrd-udevadm-cleanup-db.service
%{_prefix}/lib/systemd/system/initrd-usr-fs.target
%{_prefix}/lib/systemd/system/initrd.target
%{_prefix}/lib/systemd/system/initrd.target.wants/
%{_prefix}/lib/systemd/system/kmod-static-nodes.service
%{_prefix}/lib/systemd/system/proc-sys-fs-binfmt_misc.automount
%{_prefix}/lib/systemd/system/proc-sys-fs-binfmt_misc.mount
%{_prefix}/lib/systemd/system/quotaon-root.service
%{_prefix}/lib/systemd/system/quotaon@.service
%{_prefix}/lib/systemd/system/sleep.target
%{_prefix}/lib/systemd/system/sockets.target.wants/systemd-coredump.socket
%{_prefix}/lib/systemd/system/sockets.target.wants/systemd-repart.socket
%{_prefix}/lib/systemd/system/sockets.target.wants/systemd-sysinstall.socket
%{_prefix}/lib/systemd/system/sockets.target.wants/systemd-sysupdate.socket
%{_prefix}/lib/systemd/system/sockets.target.wants/systemd-udevd-kernel.socket
%{_prefix}/lib/systemd/system/sockets.target.wants/systemd-udevd-varlink.socket
%{_prefix}/lib/systemd/system/suspend-then-hibernate.target
%{_prefix}/lib/systemd/system/suspend.target
%{_prefix}/lib/systemd/system/sysinit.target.wants/kmod-static-nodes.service
%{_prefix}/lib/systemd/system/sysinit.target.wants/proc-sys-fs-binfmt_misc.automount
%{_prefix}/lib/systemd/system/sysinit.target.wants/systemd-binfmt.service
%{_prefix}/lib/systemd/system/sysinit.target.wants/systemd-hibernate-clear.service
%{_prefix}/lib/systemd/system/sysinit.target.wants/systemd-hwdb-update.service
%{_prefix}/lib/systemd/system/sysinit.target.wants/systemd-modules-load.service
%{_prefix}/lib/systemd/system/sysinit.target.wants/systemd-random-seed.service
%{_prefix}/lib/systemd/system/sysinit.target.wants/systemd-repart.service
%{_prefix}/lib/systemd/system/sysinit.target.wants/systemd-sysctl.service
%{_prefix}/lib/systemd/system/sysinit.target.wants/systemd-tmpfiles-setup-dev-early.service
%{_prefix}/lib/systemd/system/sysinit.target.wants/systemd-tmpfiles-setup-dev.service
%{_prefix}/lib/systemd/system/sysinit.target.wants/systemd-udev-trigger.service
%{_prefix}/lib/systemd/system/sysinit.target.wants/systemd-udevd.service
%{_prefix}/lib/systemd/system/system-install.target.wants/
%{_prefix}/lib/systemd/system/system-update-pre.target.wants/
%{_prefix}/lib/systemd/system/systemd-backlight@.service
%{_prefix}/lib/systemd/system/systemd-binfmt.service
%{_prefix}/lib/systemd/system/systemd-coredump-register.service
%{_prefix}/lib/systemd/system/systemd-coredump.socket
%{_prefix}/lib/systemd/system/systemd-coredump@.service
%{_prefix}/lib/systemd/system/systemd-coredumpd.service
%{_prefix}/lib/systemd/system/systemd-fsck-root.service
%{_prefix}/lib/systemd/system/systemd-fsck@.service
%{_prefix}/lib/systemd/system/systemd-growfs-root.service
%{_prefix}/lib/systemd/system/systemd-growfs@.service
%{_prefix}/lib/systemd/system/systemd-hibernate-clear.service
%{_prefix}/lib/systemd/system/systemd-hibernate-resume.service
%{_prefix}/lib/systemd/system/systemd-hibernate.service
%{_prefix}/lib/systemd/system/systemd-hwdb-update.service
%{_prefix}/lib/systemd/system/systemd-hybrid-sleep.service
%{_prefix}/lib/systemd/system/systemd-imds-early-network.service
%{_prefix}/lib/systemd/system/systemd-imds-import.service
%{_prefix}/lib/systemd/system/systemd-imds-metrics.socket
%{_prefix}/lib/systemd/system/systemd-imds-metrics@.service
%{_prefix}/lib/systemd/system/systemd-imdsd.socket
%{_prefix}/lib/systemd/system/systemd-imdsd@.service
%{_prefix}/lib/systemd/system/systemd-loop@.service
%{_prefix}/lib/systemd/system/systemd-modules-load.service
%{_prefix}/lib/systemd/system/systemd-oomd.service
%{_prefix}/lib/systemd/system/systemd-oomd.socket
%{_prefix}/lib/systemd/system/systemd-pstore.service
%{_prefix}/lib/systemd/system/systemd-quotacheck-root.service
%{_prefix}/lib/systemd/system/systemd-quotacheck@.service
%{_prefix}/lib/systemd/system/systemd-random-seed.service
%{_prefix}/lib/systemd/system/systemd-remount-fs.service
%{_prefix}/lib/systemd/system/systemd-repart.service
%{_prefix}/lib/systemd/system/systemd-repart.socket
%{_prefix}/lib/systemd/system/systemd-repart@.service
%{_prefix}/lib/systemd/system/systemd-rfkill.service
%{_prefix}/lib/systemd/system/systemd-rfkill.socket
%{_prefix}/lib/systemd/system/systemd-suspend-then-hibernate.service
%{_prefix}/lib/systemd/system/systemd-suspend.service
%{_prefix}/lib/systemd/system/systemd-sysctl.service
%{_prefix}/lib/systemd/system/systemd-sysinstall.service
%{_prefix}/lib/systemd/system/systemd-sysinstall.socket
%{_prefix}/lib/systemd/system/systemd-sysinstall@.service
%{_prefix}/lib/systemd/system/systemd-sysupdate-auto-enable.service
%{_prefix}/lib/systemd/system/systemd-sysupdate-notify-sysext.socket
%{_prefix}/lib/systemd/system/systemd-sysupdate-notify-sysext@.service
%{_prefix}/lib/systemd/system/systemd-sysupdate-reboot.service
%{_prefix}/lib/systemd/system/systemd-sysupdate-reboot.timer
%{_prefix}/lib/systemd/system/systemd-sysupdate-update.service
%{_prefix}/lib/systemd/system/systemd-sysupdate-update.timer
%{_prefix}/lib/systemd/system/systemd-sysupdate.service
%{_prefix}/lib/systemd/system/systemd-sysupdate.socket
%{_prefix}/lib/systemd/system/systemd-sysupdate.timer
%{_prefix}/lib/systemd/system/systemd-sysupdate@.service
%{_prefix}/lib/systemd/system/systemd-sysupdated.service
%{_prefix}/lib/systemd/system/systemd-timesyncd.service
%{_prefix}/lib/systemd/system/systemd-tmpfiles-setup-dev-early.service
%{_prefix}/lib/systemd/system/systemd-tmpfiles-setup-dev.service
%{_prefix}/lib/systemd/system/systemd-udev-load-credentials.service
%{_prefix}/lib/systemd/system/systemd-udev-settle.service
%{_prefix}/lib/systemd/system/systemd-udev-trigger.service
%{_prefix}/lib/systemd/system/systemd-udevd-control.socket
%{_prefix}/lib/systemd/system/systemd-udevd-kernel.socket
%{_prefix}/lib/systemd/system/systemd-udevd-varlink.socket
%{_prefix}/lib/systemd/system/systemd-udevd.service
%{_prefix}/lib/systemd/system/systemd-vconsole-setup.service
%{_prefix}/lib/systemd/system/systemd-volatile-root.service
%{_prefix}/lib/systemd/system/tpm2.target
%{_prefix}/lib/systemd/systemd-backlight
%{_prefix}/lib/systemd/systemd-binfmt
%{_prefix}/lib/systemd/systemd-coredump
%{_prefix}/lib/systemd/systemd-fsck
%{_prefix}/lib/systemd/systemd-growfs
%{_prefix}/lib/systemd/systemd-hibernate-resume
%{_prefix}/lib/systemd/systemd-imds
%{_prefix}/lib/systemd/systemd-imdsd
%{_prefix}/lib/systemd/systemd-makefs
%{_prefix}/lib/systemd/systemd-modules-load
%{_prefix}/lib/systemd/systemd-oomd
%{_prefix}/lib/systemd/systemd-pstore
%{_prefix}/lib/systemd/systemd-quotacheck
%{_prefix}/lib/systemd/systemd-random-seed
%{_prefix}/lib/systemd/systemd-remount-fs
%{_prefix}/lib/systemd/systemd-rfkill
%{_prefix}/lib/systemd/systemd-sleep
%{_prefix}/lib/systemd/systemd-sysctl
%{_prefix}/lib/systemd/systemd-sysupdate
%{_prefix}/lib/systemd/systemd-sysupdated
%{_prefix}/lib/systemd/systemd-timesyncd
%{_prefix}/lib/systemd/systemd-udevd
%{_prefix}/lib/systemd/systemd-vconsole-setup
%{_prefix}/lib/systemd/systemd-volatile-root
%{_prefix}/lib/sysusers.d/systemd-coredump.conf
%{_prefix}/lib/sysusers.d/systemd-imds.conf
%{_prefix}/lib/sysusers.d/systemd-timesync.conf
%{_prefix}/lib/tmpfiles.d/systemd-pstore.conf
%{_prefix}/lib/udev/ata_id
%{_prefix}/lib/udev/cdrom_id
%{_prefix}/lib/udev/dmi_memory_id
%{_prefix}/lib/udev/fido_id
%{_prefix}/lib/udev/hwdb.d/
%{_prefix}/lib/udev/iocost
%{_prefix}/lib/udev/mtd_probe
%{_prefix}/lib/udev/rules.d/
%{_prefix}/lib/udev/scsi_id
%{_prefix}/lib/udev/v4l_id
%{_datadir}/bash-completion/completions/bootctl
%{_datadir}/bash-completion/completions/coredumpctl
%{_datadir}/bash-completion/completions/kernel-install
%{_datadir}/bash-completion/completions/systemd-hwdb
%{_datadir}/bash-completion/completions/systemd-sysinstall
%{_datadir}/bash-completion/completions/systemd-sysupdate
%{_datadir}/bash-completion/completions/udevadm
%{_datadir}/bash-completion/completions/updatectl
%{_datadir}/dbus-1/interfaces/org.freedesktop.sysupdate1.Job.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.sysupdate1.Manager.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.sysupdate1.Target.xml
%{_datadir}/dbus-1/system-services/org.freedesktop.sysupdate1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.timesync1.service
%{_datadir}/dbus-1/system.d/org.freedesktop.sysupdate1.conf
%{_datadir}/dbus-1/system.d/org.freedesktop.timesync1.conf
%{_datadir}/factory/etc/vconsole.conf
%{_datadir}/polkit-1/actions/io.systemd.imds.policy
%{_datadir}/polkit-1/actions/org.freedesktop.sysupdate1.policy
%{_datadir}/polkit-1/actions/org.freedesktop.timesync1.policy
%{_datadir}/zsh/site-functions/_bootctl
%{_datadir}/zsh/site-functions/_coredumpctl
%{_datadir}/zsh/site-functions/_kernel-install
%{_datadir}/zsh/site-functions/_systemd-hwdb
%{_datadir}/zsh/site-functions/_systemd-sysinstall
%{_datadir}/zsh/site-functions/_systemd-sysupdate
%{_datadir}/zsh/site-functions/_udevadm
%{_datadir}/zsh/site-functions/_updatectl
%if %{without bootstrap} && !0%{?bootstrap}
%config(noreplace) %{_sysconfdir}/systemd/homed.conf
%{_bindir}/homectl
%{_bindir}/systemd-cryptenroll
%{_bindir}/systemd-cryptsetup
%{_prefix}/lib/systemd/system-generators/systemd-cryptsetup-generator
%{_prefix}/lib/systemd/system-generators/systemd-integritysetup-generator
%{_prefix}/lib/systemd/system-generators/systemd-veritysetup-generator
%{_prefix}/lib/systemd/system/cryptsetup-pre.target
%{_prefix}/lib/systemd/system/cryptsetup.target
%{_prefix}/lib/systemd/system/integritysetup-pre.target
%{_prefix}/lib/systemd/system/integritysetup.target
%{_prefix}/lib/systemd/system/remote-cryptsetup.target
%{_prefix}/lib/systemd/system/remote-integritysetup.target
%{_prefix}/lib/systemd/system/remote-veritysetup.target
%{_prefix}/lib/systemd/system/sockets.target.wants/systemd-cryptenroll.socket
%{_prefix}/lib/systemd/system/sysinit.target.wants/cryptsetup.target
%{_prefix}/lib/systemd/system/sysinit.target.wants/integritysetup.target
%{_prefix}/lib/systemd/system/sysinit.target.wants/veritysetup.target
%{_prefix}/lib/systemd/system/system-systemd\x2dcryptsetup.slice
%{_prefix}/lib/systemd/system/system-systemd\x2dveritysetup.slice
%{_prefix}/lib/systemd/system/systemd-cryptenroll-firstboot.service
%{_prefix}/lib/systemd/system/systemd-cryptenroll.socket
%{_prefix}/lib/systemd/system/systemd-cryptenroll@.service
%{_prefix}/lib/systemd/system/systemd-homed-activate.service
%{_prefix}/lib/systemd/system/systemd-homed-firstboot.service
%{_prefix}/lib/systemd/system/systemd-homed.service
%{_prefix}/lib/systemd/system/veritysetup-pre.target
%{_prefix}/lib/systemd/system/veritysetup.target
%{_prefix}/lib/systemd/systemd-cryptsetup
%{_prefix}/lib/systemd/systemd-homed
%{_prefix}/lib/systemd/systemd-integritysetup
%{_prefix}/lib/systemd/systemd-veritysetup
%{_libdir}/cryptsetup/libcryptsetup-token-systemd-pkcs11.so
%{_datadir}/bash-completion/completions/homectl
%{_datadir}/bash-completion/completions/systemd-cryptenroll
%{_datadir}/dbus-1/interfaces/org.freedesktop.home1.Home.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.home1.Manager.xml
%{_datadir}/dbus-1/system-services/org.freedesktop.home1.service
%{_datadir}/dbus-1/system.d/org.freedesktop.home1.conf
%{_datadir}/polkit-1/actions/io.systemd.cryptenroll.policy
%{_datadir}/polkit-1/actions/org.freedesktop.home1.policy
%{_datadir}/zsh/site-functions/_systemd-cryptenroll
%endif

%files container
%{_bindir}/importctl
%{_bindir}/machinectl
%{_bindir}/mount.ddi
%{_bindir}/portablectl
%{_bindir}/systemd-dissect
%{_bindir}/systemd-nspawn
%{_bindir}/systemd-vmspawn
%{_prefix}/lib/systemd/oci-registry/
%{_prefix}/lib/systemd/portable/
%{_prefix}/lib/systemd/system-generators/systemd-import-generator
%{_prefix}/lib/systemd/system/dbus-org.freedesktop.import1.service
%{_prefix}/lib/systemd/system/dbus-org.freedesktop.machine1.service
%{_prefix}/lib/systemd/system/dbus-org.freedesktop.portable1.service
%{_prefix}/lib/systemd/system/machine.slice
%{_prefix}/lib/systemd/system/machines.target
%{_prefix}/lib/systemd/system/machines.target.wants/
%{_prefix}/lib/systemd/system/remote-fs.target.wants/
%{_prefix}/lib/systemd/system/sockets.target.wants/systemd-importd.socket
%{_prefix}/lib/systemd/system/sockets.target.wants/systemd-machined.socket
%{_prefix}/lib/systemd/system/systemd-importd.service
%{_prefix}/lib/systemd/system/systemd-importd.socket
%{_prefix}/lib/systemd/system/systemd-machined.service
%{_prefix}/lib/systemd/system/systemd-machined.socket
%{_prefix}/lib/systemd/system/systemd-mountfsd.service
%{_prefix}/lib/systemd/system/systemd-mountfsd.socket
%{_prefix}/lib/systemd/system/systemd-nspawn@.service
%{_prefix}/lib/systemd/system/systemd-nsresourced.service
%{_prefix}/lib/systemd/system/systemd-nsresourced.socket
%{_prefix}/lib/systemd/system/systemd-portabled.service
%{_prefix}/lib/systemd/system/systemd-vmspawn@.service
%{_prefix}/lib/systemd/system/var-lib-machines.mount
%{_prefix}/lib/systemd/systemd-export
%{_prefix}/lib/systemd/systemd-import
%{_prefix}/lib/systemd/systemd-import-fs
%{_prefix}/lib/systemd/systemd-importd
%{_prefix}/lib/systemd/systemd-machined
%{_prefix}/lib/systemd/systemd-mountfsd
%{_prefix}/lib/systemd/systemd-mountwork
%{_prefix}/lib/systemd/systemd-nsresourced
%{_prefix}/lib/systemd/systemd-nsresourcework
%{_prefix}/lib/systemd/systemd-portabled
%{_prefix}/lib/systemd/systemd-pull
%{_prefix}/lib/systemd/user/dbus-org.freedesktop.import1.service
%{_prefix}/lib/systemd/user/dbus-org.freedesktop.machine1.service
%{_prefix}/lib/systemd/user/dbus-org.freedesktop.portable1.service
%{_prefix}/lib/systemd/user/machine.slice
%{_prefix}/lib/systemd/user/machines.target
%{_prefix}/lib/systemd/user/portable/
%{_prefix}/lib/systemd/user/sockets.target.wants/systemd-importd.socket
%{_prefix}/lib/systemd/user/sockets.target.wants/systemd-machined.socket
%{_prefix}/lib/systemd/user/systemd-importd.service
%{_prefix}/lib/systemd/user/systemd-importd.socket
%{_prefix}/lib/systemd/user/systemd-machined.service
%{_prefix}/lib/systemd/user/systemd-machined.socket
%{_prefix}/lib/systemd/user/systemd-nspawn@.service
%{_prefix}/lib/systemd/user/systemd-portabled.service
%{_prefix}/lib/systemd/user/systemd-vmspawn@.service
%{_prefix}/lib/tmpfiles.d/portables.conf
%{_prefix}/lib/tmpfiles.d/systemd-nspawn.conf
%{_libdir}/libnss_mymachines.so.2
%{_datadir}/bash-completion/completions/importctl
%{_datadir}/bash-completion/completions/machinectl
%{_datadir}/bash-completion/completions/portablectl
%{_datadir}/bash-completion/completions/systemd-dissect
%{_datadir}/bash-completion/completions/systemd-nspawn
%{_datadir}/bash-completion/completions/systemd-vmspawn
%{_datadir}/dbus-1/interfaces/org.freedesktop.import1.Manager.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.import1.Transfer.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.machine1.Image.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.machine1.Machine.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.machine1.Manager.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portable1.Image.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portable1.Manager.xml
%{_datadir}/dbus-1/services/org.freedesktop.import1.service
%{_datadir}/dbus-1/services/org.freedesktop.machine1.service
%{_datadir}/dbus-1/services/org.freedesktop.portable1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.import1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.machine1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.portable1.service
%{_datadir}/dbus-1/system.d/org.freedesktop.import1.conf
%{_datadir}/dbus-1/system.d/org.freedesktop.machine1.conf
%{_datadir}/dbus-1/system.d/org.freedesktop.portable1.conf
%{_datadir}/polkit-1/actions/org.freedesktop.import1.policy
%{_datadir}/polkit-1/actions/org.freedesktop.machine1.policy
%{_datadir}/polkit-1/actions/org.freedesktop.portable1.policy
%{_datadir}/zsh/site-functions/_machinectl
%{_datadir}/zsh/site-functions/_systemd-nspawn

%files networkd
%config(noreplace) %{_sysconfdir}/systemd/networkd.conf
%{_bindir}/networkctl
%{_prefix}/lib/systemd/network/80-6rd-tunnel.network
%{_prefix}/lib/systemd/network/80-auto-link-local.network.example
%{_prefix}/lib/systemd/network/80-container-host0-tun.network
%{_prefix}/lib/systemd/network/80-container-host0.network
%{_prefix}/lib/systemd/network/80-container-vb.network
%{_prefix}/lib/systemd/network/80-container-ve.network
%{_prefix}/lib/systemd/network/80-container-vz.network
%{_prefix}/lib/systemd/network/80-namespace-ns-tun.network
%{_prefix}/lib/systemd/network/80-namespace-ns.network
%{_prefix}/lib/systemd/network/80-vm-vt.network
%{_prefix}/lib/systemd/network/80-wifi-adhoc.network
%{_prefix}/lib/systemd/network/80-wifi-ap.network.example
%{_prefix}/lib/systemd/network/80-wifi-station.network.example
%{_prefix}/lib/systemd/network/89-ethernet.network.example
%{_prefix}/lib/systemd/system/systemd-network-generator.service
%{_prefix}/lib/systemd/system/systemd-networkd-persistent-storage.service
%{_prefix}/lib/systemd/system/systemd-networkd-resolve-hook.socket
%{_prefix}/lib/systemd/system/systemd-networkd-varlink-metrics.socket
%{_prefix}/lib/systemd/system/systemd-networkd-varlink.socket
%{_prefix}/lib/systemd/system/systemd-networkd-wait-online.service
%{_prefix}/lib/systemd/system/systemd-networkd-wait-online@.service
%{_prefix}/lib/systemd/system/systemd-networkd.service
%{_prefix}/lib/systemd/system/systemd-networkd.socket
%{_prefix}/lib/systemd/systemd-network-generator
%{_prefix}/lib/systemd/systemd-networkd
%{_prefix}/lib/systemd/systemd-networkd-wait-online
%{_prefix}/lib/sysusers.d/systemd-network.conf
%{_prefix}/lib/tmpfiles.d/systemd-network.conf
%{_datadir}/bash-completion/completions/networkctl
%{_datadir}/dbus-1/interfaces/org.freedesktop.network1.DHCPServer.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.network1.DHCPv4Client.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.network1.DHCPv6Client.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.network1.Link.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.network1.Manager.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.network1.Network.xml
%{_datadir}/dbus-1/system-services/org.freedesktop.network1.service
%{_datadir}/dbus-1/system.d/org.freedesktop.network1.conf
%{_datadir}/polkit-1/actions/org.freedesktop.network1.policy
%{_datadir}/zsh/site-functions/_networkctl

%files resolved
%config(noreplace) %{_sysconfdir}/systemd/resolved.conf
%{_bindir}/resolvconf
%{_bindir}/systemd-resolve
%{_prefix}/lib/systemd/system/systemd-resolved-monitor.socket
%{_prefix}/lib/systemd/system/systemd-resolved-varlink.socket
%{_prefix}/lib/systemd/system/systemd-resolved.service
%{_prefix}/lib/systemd/systemd-resolved
%{_prefix}/lib/sysusers.d/systemd-resolve.conf
%{_prefix}/lib/tmpfiles.d/systemd-resolve.conf
%{_datadir}/bash-completion/completions/systemd-resolve
%{_datadir}/dbus-1/interfaces/org.freedesktop.resolve1.DnsDelegate.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.resolve1.DnssdService.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.resolve1.Link.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.resolve1.Manager.xml
%{_datadir}/dbus-1/system-services/org.freedesktop.resolve1.service
%{_datadir}/dbus-1/system.d/org.freedesktop.resolve1.conf
%{_datadir}/polkit-1/actions/org.freedesktop.resolve1.policy

%files journal-remote
%config(noreplace) %{_sysconfdir}/systemd/journal-remote.conf
%config(noreplace) %{_sysconfdir}/systemd/journal-upload.conf
%{_prefix}/lib/systemd/system/systemd-journal-gatewayd.service
%{_prefix}/lib/systemd/system/systemd-journal-gatewayd.socket
%{_prefix}/lib/systemd/system/systemd-journal-remote.service
%{_prefix}/lib/systemd/system/systemd-journal-remote.socket
%{_prefix}/lib/systemd/system/systemd-journal-upload.service
%{_prefix}/lib/systemd/systemd-journal-gatewayd
%{_prefix}/lib/systemd/systemd-journal-remote
%{_prefix}/lib/systemd/systemd-journal-upload
%{_prefix}/lib/sysusers.d/systemd-remote.conf
%{_datadir}/systemd/gatewayd/

%files devel
%{_includedir}/libudev.h
%{_includedir}/systemd/_sd-common.h
%{_includedir}/systemd/sd-bus-protocol.h
%{_includedir}/systemd/sd-bus-vtable.h
%{_includedir}/systemd/sd-bus.h
%{_includedir}/systemd/sd-daemon.h
%{_includedir}/systemd/sd-device.h
%{_includedir}/systemd/sd-dlopen.h
%{_includedir}/systemd/sd-event.h
%{_includedir}/systemd/sd-gpt.h
%{_includedir}/systemd/sd-hwdb.h
%{_includedir}/systemd/sd-id128.h
%{_includedir}/systemd/sd-journal.h
%{_includedir}/systemd/sd-json.h
%{_includedir}/systemd/sd-login.h
%{_includedir}/systemd/sd-messages.h
%{_includedir}/systemd/sd-path.h
%{_includedir}/systemd/sd-varlink-idl.h
%{_includedir}/systemd/sd-varlink.h
%{_libdir}/libsystemd.so
%{_libdir}/libudev.so
%{_libdir}/pkgconfig/libsystemd.pc
%{_libdir}/pkgconfig/libudev.pc

%changelog
* Tue Oct 27 2026 Oreon Packaging Team <packaging@oreonhq.com> - 259.10-1
- 259.10
