Name:           spice-vdagent
Version:        0.23.0
Release:        2%{?dist}
Summary:        Agent for Spice guests
License:        GPL-3.0-or-later
URL:            https://spice-space.org/
Source0:        https://spice-space.org/download/releases/%{name}-%{version}.tar.bz2
# oreon url source checksums begin
%global source0_sha256 63e0f9bd5597c4638acfd6f10d7a2354f599bd9df5b31e443270cacf07e16a40
%global source0_file spice-vdagent-0.23.0.tar.bz2
# oreon url source checksums end
#Source1:        https://spice-space.org/download/releases/%{name}-%{version}.tar.bz2.sig
#Source2:        victortoso-E37A484F.keyring

BuildRequires: make
BuildRequires:  systemd-devel
BuildRequires:  glib2-devel >= 2.50
BuildRequires:  spice-protocol >= 0.14.3
BuildRequires:  libpciaccess-devel libXrandr-devel libXinerama-devel
BuildRequires:  libXfixes-devel systemd desktop-file-utils libtool
BuildRequires:  alsa-lib-devel dbus-devel libdrm-devel
# For autoreconf, needed after clipboard patch series
BuildRequires:  automake autoconf
#BuildRequires:  gnupg2
%{?systemd_requires}

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/spice-vdagent-0.23.0.tar.bz2; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "63e0f9bd5597c4638acfd6f10d7a2354f599bd9df5b31e443270cacf07e16a40" || { echo "oreon: Source0 SHA256 mismatch for spice-vdagent-0.23.0.tar.bz2" >&2; exit 1; })
# oreon verify url source checksums end
#gpgv2 --quiet --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%autosetup -p1
autoreconf -fi


%build
%configure --with-session-info=systemd --with-init-script=systemd
%make_build V=2


%install
%make_install V=2


%post
%systemd_post spice-vdagentd.service spice-vdagentd.socket

%preun
%systemd_preun spice-vdagentd.service spice-vdagentd.socket

%postun
%systemd_postun_with_restart spice-vdagentd.service spice-vdagentd.socket


%files
%doc COPYING CHANGELOG.md README.md
/usr/lib/udev/rules.d/70-spice-vdagentd.rules
%{_unitdir}/spice-vdagentd.service
%{_unitdir}/spice-vdagentd.socket
%{_prefix}/lib/tmpfiles.d/spice-vdagentd.conf
%{_userunitdir}/spice-vdagent.service
%{_userunitdir}/graphical-session.target.wants/spice-vdagent.service
%{_bindir}/spice-vdagent
%{_sbindir}/spice-vdagentd
%{_sysconfdir}/xdg/autostart/spice-vdagent.desktop
%{_mandir}/man1/%{name}*.1*


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.23.0-2
- Import
