%global source0_hash 73e6aef3fb6c8b482acb5b5e2b8fa7794045c4f2420276f035ce76c5beae632d
%global _hardened_build 1
Summary:        Network diagnostic tool combining 'traceroute' and 'ping'
Name: mtr
Version: 0.96
Release:        1%{?dist}
Epoch: 2
License: GPL-2.0-only
URL: https://www.bitwizard.nl/mtr/
Source0:        https://github.com/traviscross/mtr/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: net-x%{name}.desktop
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  gtk3-devel
BuildRequires:  jansson-devel
BuildRequires:  libcap-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  ncurses-devel
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mtr-gtk -f %{oreon_filedir}/mtr-gtk.list

%changelog

%autochangelog
