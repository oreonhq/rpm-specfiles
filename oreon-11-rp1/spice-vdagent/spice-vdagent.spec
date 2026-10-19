%global source0_hash 63e0f9bd5597c4638acfd6f10d7a2354f599bd9df5b31e443270cacf07e16a40
Name:           spice-vdagent
Version:        0.23.0
Release:        2%{?dist}
Summary:        Agent for Spice guests
License:        GPL-3.0-or-later
URL:            https://spice-space.org/
Source0:        https://spice-space.org/download/releases/%{name}-%{version}.tar.bz2
%{?systemd_requires}
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  dbus-devel
BuildRequires:  desktop-file-utils
BuildRequires:  glib2-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libdrm-devel
BuildRequires:  libpciaccess-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  spice-protocol
BuildRequires:  systemd
BuildRequires:  systemd-devel
# /oreon:deps
%description
Spice agent for Linux guests offering the following features:

Features:
* Client mouse mode (no need to grab mouse by client, no mouse lag)
  this is handled by the daemon by feeding mouse events into the kernel
  via uinput. This will only work if the active X-session is running a
  spice-vdagent process so that its resolution can be determined.
* Automatic adjustment of the X-session resolution to the client resolution
* Support of copy and paste (text and images) between the active X-session
  and the client

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
#gpgv2 --quiet --keyring %%{SOURCE2} %%{SOURCE1} %%{SOURCE0}
%autosetup -p1
autoreconf -fi

%build

%configure --with-session-info=systemd --with-init-script=systemd
%make_build V=2
%install
%make_install V=2
%oreon_autofiles main

%post

%systemd_post spice-vdagentd.service spice-vdagentd.socket
%preun

%systemd_preun spice-vdagentd.service spice-vdagentd.socket
%postun

%systemd_postun_with_restart spice-vdagentd.service spice-vdagentd.socket
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.23.0-2
- Import
