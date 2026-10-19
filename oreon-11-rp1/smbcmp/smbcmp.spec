%global source0_hash aa1b8b8b39e7fbee437318a08e120609d2e92b80faf094e263a73d861d68d227
Name:		smbcmp
Version:	0.1
Release:        25%{?dist}
License:	GPL-3.0-or-later
Summary:        Small curses utility to diff, compare and debug SMB network traces
URL:		https://github.com/smbcmp/smbcmp
Group:		Development/Tools/Debuggers
Source0:        https://github.com/smbcmp/smbcmp/archive/v0.1/%{name}-%{version}.tar.gz
BuildArch:	noarch
Requires:	wireshark-cli
# oreon:deps
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
Small curses utility to diff, compare and debug SMB network traces.

%package gui
Summary:	GUI version of smbcmp
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	python3-wxpython4
%description gui
smbcmp is a debug tool to diff and compare network captures aimed
towards SMB traffic. This is the GUI version of smbcmp based on the
wxWidget toolkit.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

sed -i 's|curses||' setup.py
%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n smbcmp-gui -f %{oreon_filedir}/smbcmp-gui.list

%changelog

%autochangelog
