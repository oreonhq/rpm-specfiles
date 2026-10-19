%global source0_hash 23044e87a62a18fe929e66725b637271b0ec72528f79f3e9381b036768a36af5
Name:           powerstat
Version:        0.04.6
Release:        1%{?dist}
Summary:        Measures the power consumption of a machine
License:        GPL-2.0-or-later
URL:            https://github.com/ColinIanKing/powerstat
Source0:        https://github.com/ColinIanKing/%{name}/archive/V%{version}/%{name}-V%{version}.tar.gz
Patch:          01-preserve-timestamp-copy-man.patch
ExclusiveArch:  %{ix86} x86_64
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
Powerstat measures the power consumption of a machine using the
battery stats or the Intel RAPL interface. The output is like
vmstat but also shows power consumption statistics. At the end
of a run, powerstat will calculate the average, standard
deviation and min/max of the gathered data.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build
%install
%make_install
%oreon_autofiles main

%check

%{buildroot}%{_bindir}/powerstat -h
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
