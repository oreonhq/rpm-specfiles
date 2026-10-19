%global source0_hash d6669cb6e67bb9653751a2b00e7f472816e96acfaf67018980f3c19862e9e40c
%global sys_name s_tui
Name:       s-tui
Version:    1.5.0
Release:        1%{?dist}
Summary:        Terminal-based CPU stress and monitoring utility
BuildArch:  noarch
License:    GPL-2.0-or-later
URL:        https://github.com/amanusk/s-tui
Source0:        https://github.com/amanusk/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Recommends: stress-ng
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-s-tui = %{version}-%{release}
# /oreon:deps
%description
Stress-Terminal UI, s-tui, monitors CPU temperature, frequency, power and
utilization in a graphical way from the terminal.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
for lib in %{buildroot}%{python3_sitelib}/%{sys_name}/{/,sources,sturwid}/*.py; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done
for lib in %{buildroot}%{python3_sitelib}/%{sys_name}/{/,sources,sturwid}/*.py; do
 sed '1{\@^#!/usr/bin/python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done
%oreon_autofiles main

%files

%changelog

%autochangelog
