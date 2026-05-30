%global source0_hash 12490fb660ba5fb34df8c06a0f62b4f9cbd11a584fc3f6eceda0a99124e8596f

%global _hardened_build 1

Summary: Network diagnostic tool combining 'traceroute' and 'ping'
Name: mtr
Version: 0.95
Release: 14%{?dist}
Epoch: 2
License: GPL-2.0-only
URL: https://www.bitwizard.nl/mtr/
Source0:        https://github.com/traviscross/mtr/archive/v%{version}/%{name}-%{version}.tar.gz
Source1: net-x%{name}.desktop
# https://github.com/traviscross/mtr/issues/469
Patch0: https://github.com/traviscross/mtr/commit/5908af4c19188cb17b62f23368b6ef462831a0cb.patch#/mtr-0.95-snprintf-sizes.patch
# https://github.com/traviscross/mtr/issues/232, https://github.com/traviscross/mtr/pull/484
Patch1: https://github.com/traviscross/mtr/commit/74d312d7e67d002e184b37c7f278597ab06bf8e7.patch#/mtr-0.95-socket-binding.patch

BuildRequires: gcc make ncurses-devel libcap-devel jansson-devel
BuildRequires: autoconf automake libtool git

%description
MTR combines the functionality of the 'traceroute' and 'ping' programs
in a single network diagnostic tool.

When MTR is started, it investigates the network connection between the
host MTR runs on and the user-specified destination host. Afterwards it
determines the address of each network hop between the machines and sends
a sequence of ICMP echo requests to each one to determine the quality of
the link to each machine. While doing this, it prints running statistics
about each machine.

MTR provides two user interfaces: an ncurses interface, useful for the
command line, e.g. for SSH sessions; and a GTK interface for X (provided
in the mtr-gtk package).

%package gtk
Summary: GTK interface for MTR
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: gtk3-devel desktop-file-utils

%description gtk
MTR combines the functionality of the 'traceroute' and 'ping' programs
in a single network diagnostic tool. The mtr-gtk package provides the
GTK interface for MTR.

When MTR is started, it investigates the network connection between the
host MTR runs on and the user-specified destination host. Afterwards it
determines the address of each network hop between the machines and sends
a sequence of ICMP echo requests to each one to determine the quality of
the link to each machine. While doing this, it prints running statistics
about each machine.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q
%patch -P0 -p1 -b .snprintf-sizes
%patch -P1 -p1 -b .socket-binding

%build
./bootstrap.sh
%configure --with-gtk
%make_build && mv -f mtr xmtr && make distclean
%configure --without-gtk
%make_build

%install
%make_install
install -D -p -m 0755 xmtr %{buildroot}%{_bindir}/xmtr
install -D -p -m 0644 img/mtr_icon.xpm %{buildroot}%{_datadir}/pixmaps/mtr_icon.xpm
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

%files
%license COPYING
%doc AUTHORS FORMATS NEWS README.md SECURITY
%{_sbindir}/%{name}
%attr(0755,root,root) %caps(cap_net_raw=pe) %{_sbindir}/%{name}-packet
%{_mandir}/man8/%{name}.8*
%{_mandir}/man8/%{name}-packet.8*
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/completions/%{name}

%files gtk
%{_bindir}/xmtr
%{_datadir}/pixmaps/mtr_icon.xpm
%{_datadir}/applications/net-x%{name}.desktop

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.95-14
- Prepare for Oreon 11 (RP1)
