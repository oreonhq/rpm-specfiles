%global source0_hash a81adcac025b08c7c933f028339c55a67d0da6c81845fe3d18fd4187010a63d4
Name:       pdd
Version:    1.7
Release:        1%{?dist}
Summary:        Tiny date, time diff calculator
License:    GPL-3.0-or-later
URL:        https://github.com/jarun/pdd
Source0:        https://github.com/jarun/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:     32.patch
BuildArch:  noarch
Requires: python3-dateutil
# oreon:deps
BuildRequires:  make
BuildRequires:  python3-dateutil
BuildRequires:  python3-devel
# /oreon:deps
%description
There are times you want to check how old you are (in years, months, days) or
how long you need to wait for the next flash sale... pdd (python3 date diff)
is a small cmdline utility to calculate date and time difference. If no
program arguments are specified it shows the current date, time and timezone.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}
sed -i '1s/env //' pdd

%install
mkdir -p %{buildroot}%{_datadir}/bash-completion/compilations/
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions/
mkdir -p %{buildroot}%{_datadir}/fish/vendor_completions.d/
%make_install PREFIX=%{_prefix}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
