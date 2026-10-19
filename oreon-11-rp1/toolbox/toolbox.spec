%global source0_hash 0243bd995743ea73464426839ee80e2a13a8c529e3053292783f603b882dd125
%global __brp_check_rpaths %{nil}
Name:          toolbox
Version:       0.3
%global goipath github.com/containers/%{name}
%global toolbx_go 1.22
Release:        4%{?dist}
Summary:        Tool for interactive command line environments on Linux
License:       Apache-2.0
URL:           https://containertoolbx.org/
Source0:        https://github.com/containers/%{name}/releases/download/%{version}/%{name}-%{version}-vendored.tar.xz
Source1:       %{name}.conf
Patch100:      toolbox-Make-the-build-flags-match-Fedora.patch
Patch200:      toolbox-Make-the-build-flags-match-RHEL-9.patch
Patch201:      toolbox-Make-the-build-flags-match-RHEL-10.patch
Patch202:      toolbox-Add-migration-paths-for-coreos-toolbox-users.patch
Recommends:    p11-kit-server
Recommends:    skopeo
Requires:      containers-common
Requires:      flatpak-session-helper
Requires:      podman >= 1.6.4
Requires:      shadow-utils-subid%{?_isa} >= 4.16.0
# oreon:deps
BuildRequires:  gcc
BuildRequires:  go-md2man
BuildRequires:  golang
BuildRequires:  meson
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  shadow-utils-subid-devel
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Toolbx is a tool for Linux, which allows the use of interactive command line
environments for software development and troubleshooting the host operating
system, without having to install software on the host. It is built on top of
Podman and other standard container technologies from OCI.

Toolbx environments have seamless access to the user's home directory, the
Wayland and X11 sockets, networking (including Avahi), removable devices (like
USB sticks), systemd journal, SSH agent, D-Bus, ulimits, /dev and the udev
database, etc..

%package       tests
Summary:       Tests for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      coreutils
Requires:      diffutils
Requires:      glib2
Requires:      grep
Requires:      httpd-tools
Requires:      openssl
Requires:      python3
Requires:      skopeo
%description   tests
The %{name}-tests package contains system tests for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%gomkdir -s %{_builddir}/%{extractdir}/src -k

%build

export CGO_CFLAGS="%{optflags} -D_GNU_SOURCE -D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64"
%meson \
    -Dprofile_dir=%{_sysconfdir}/profile.d \
    -Dtmpfiles_dir=%{_tmpfilesdir} \
    -Dzsh_completions_dir=%{zsh_completions_dir}
%meson_build
%install
%meson_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n toolbox-tests -f %{oreon_filedir}/toolbox-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.3-4
- Prepare for Oreon 11 (RP1)
