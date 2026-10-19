%global source0_hash cd7c6cbbe511241941784bc40561f25ab1410b7218aa4f8cc1131125bd904ae5
Name:           blivet-gui
Version:        2.6.0
Release:        1%{?dist}
Summary:        Graphical tool for storage configuration
License:        GPL-2.0-or-later
URL:            https://github.com/storaged-project/blivet-gui
Source0:        http://github.com/storaged-project/blivet-gui/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       %{name}-runtime = %{version}-%{release}
# oreon:deps
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
blivet-gui is a GTK-based utility for inspecting and modifying storage layout,
including partitions, filesystems, LVM, RAID, and encrypted devices.

%package runtime
Summary:        Runtime files for blivet-gui
Requires:       python3-blivet >= 1:3.13.0
Requires:       python3-gobject-base
Requires:       python3-pid
Requires:       python3-pyparted
Requires:       gtk3
Requires:       polkit
%description runtime
Runtime files for blivet-gui, including Python modules, daemon, UI assets,
translations, policy files, and desktop integration data.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%py3_build
make -C po
%install
%py3_install
RPM_BUILD_ROOT=%{buildroot} make -C po install
%oreon_autofiles blivet-gui-runtime usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n blivet-gui-runtime -f %{oreon_filedir}/blivet-gui-runtime.list
