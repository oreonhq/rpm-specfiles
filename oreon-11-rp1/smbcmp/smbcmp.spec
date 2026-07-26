%global source0_hash aa1b8b8b39e7fbee437318a08e120609d2e92b80faf094e263a73d861d68d227

#
# spec file for package smbcmp
#

Name:		smbcmp
Version:	0.1
Release:	25%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
Summary:	Small curses utility to diff, compare and debug SMB network traces
URL:		https://github.com/smbcmp/smbcmp
Group:		Development/Tools/Debuggers
Source0:	https://github.com/smbcmp/smbcmp/archive/v0.1/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python3-devel
BuildRequires:	python3 >= 3.4
BuildRequires:	python3-setuptools
Requires:	wireshark-cli

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

%autosetup -p1

%build
# Workaround as there is no -lboost_python3
sed -i 's|curses||' setup.py
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{python3_sitelib}/smbcmp/
%{python3_sitelib}/smbcmp*egg-info*

%files gui
%{_bindir}/%{name}-gui

%changelog
%autochangelog
