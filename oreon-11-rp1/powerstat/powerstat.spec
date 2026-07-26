%global source0_hash 23044e87a62a18fe929e66725b637271b0ec72528f79f3e9381b036768a36af5

Name:           powerstat
Version:        0.04.05
Release:        3%{?dist}
Summary:        Measures the power consumption of a machine

License:        GPL-2.0-or-later
URL:            https://github.com/ColinIanKing/powerstat
Source:         %{url}/archive/V%{version}/%{name}-V%{version}.tar.gz
# Preserve timestamp of powerstat file and let build system
# compress man page
Patch:          01-preserve-timestamp-copy-man.patch

BuildRequires:  gcc
BuildRequires:  make
# RAPL not available on other architectures
ExclusiveArch:  %{ix86} x86_64

%description
Powerstat measures the power consumption of a machine using the
battery stats or the Intel RAPL interface. The output is like
vmstat but also shows power consumption statistics. At the end
of a run, powerstat will calculate the average, standard
deviation and min/max of the gathered data.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
# Preserve timestamp
%make_build

%install
%make_install

%check
# Smoke test binary works, no tests available
%{buildroot}%{_bindir}/powerstat -h

%files
%doc README.md
%license COPYING
%{_bindir}/powerstat
%{_mandir}/man8/powerstat.8*
%{bash_completions_dir}/powerstat

%changelog
%autochangelog
