%global source0_hash b59998e0e7f2b683d04999d968ef29f9b9933cdb2c85ffc83cf1505bc3efccf1

%global goipath github.com/snapcore/snapd

Summary:        Tools to interact with snaps and the snap store
Name:           snapd
Version:        2.75.2
Release:        1%{?dist}
License:        GPL-3.0-only
URL:            https://snapcraft.io/
Source0:        https://github.com/canonical/snapd/releases/download/%{version}/%{name}_%{version}.vendor.tar.xz

BuildRequires:  golang
BuildRequires:  systemd-devel
BuildRequires:  squashfs-tools

Requires:       squashfs-tools
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
snapd provides support for the "snap" package format, running snapd as a
background service which communicates over a UNIX socket, and the "snap"
command line tool used to install, refresh and remove snap packages.
Used by plasma-discover to browse and install snaps.

Note: this initial import ships the snapd daemon and the snap/snapctl CLI
tools built straight from the vendored Go sources. snap-confine and the
rest of the cmd/ C-based sandboxing helpers (which have their own
autotools build under cmd/) are not built yet; snaps that require strict
confinement will need that follow-up before they can run unconfined-free.
Track this in a dedicated spec update rather than silently disabling
confinement checks at runtime.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-%{version}

%build
export GOFLAGS="-mod=vendor"
export GO111MODULE=on
export GOPATH=%{_builddir}/go
mkdir -p "$GOPATH/src/github.com/snapcore"
ln -sfn "$(pwd)" "$GOPATH/src/github.com/snapcore/snapd"
version="%{version}"
go build -buildmode=pie -ldflags "-X %{goipath}/cmd/snap.Version=${version} -X %{goipath}/cmd/snapd.Version=${version}" -o bin/snapd ./cmd/snapd
go build -buildmode=pie -ldflags "-X %{goipath}/cmd/snap.Version=${version}" -o bin/snap ./cmd/snap
go build -buildmode=pie -o bin/snapctl ./cmd/snapctl

%install
install -D -p -m 0755 bin/snapd %{buildroot}%{_libexecdir}/snapd/snapd
install -D -p -m 0755 bin/snap %{buildroot}%{_bindir}/snap
install -D -p -m 0755 bin/snapctl %{buildroot}%{_libexecdir}/snapd/snapctl
ln -s %{_libexecdir}/snapd/snapctl %{buildroot}%{_bindir}/snapctl

install -d -m 0755 %{buildroot}%{_sharedstatedir}/snapd/snaps
install -d -m 0755 %{buildroot}%{_sharedstatedir}/snapd/snap
install -d -m 0755 %{buildroot}%{_sharedstatedir}/snapd/desktop/applications
install -d -m 0755 %{buildroot}%{_sysconfdir}/systemd/system

install -D -p -m 0644 /dev/stdin %{buildroot}%{_unitdir}/snapd.socket <<'EOF'
[Unit]
Description=Socket activation for snappy daemon

[Socket]
ListenStream=/run/snapd.socket
SocketMode=0666

[Install]
WantedBy=sockets.target
EOF

install -D -p -m 0644 /dev/stdin %{buildroot}%{_unitdir}/snapd.service <<EOF
[Unit]
Description=Snap Daemon
Requires=snapd.socket

[Service]
Type=notify
ExecStart=%{_libexecdir}/snapd/snapd
Restart=on-abnormal

[Install]
WantedBy=multi-user.target
Also=snapd.socket
EOF

%post
%systemd_post snapd.socket snapd.service

%preun
%systemd_preun snapd.socket snapd.service

%postun
%systemd_postun_with_restart snapd.socket snapd.service

%files
%license COPYING
%doc README.md
%{_bindir}/snap
%{_bindir}/snapctl
%{_libexecdir}/snapd/
%dir %{_sharedstatedir}/snapd
%dir %{_sharedstatedir}/snapd/snaps
%dir %{_sharedstatedir}/snapd/snap
%dir %{_sharedstatedir}/snapd/desktop
%dir %{_sharedstatedir}/snapd/desktop/applications
%{_unitdir}/snapd.socket
%{_unitdir}/snapd.service

%changelog
%autochangelog
