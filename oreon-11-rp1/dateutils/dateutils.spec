%global source0_hash 1e0593116e1a229242255cf890f210cbe120e6f05e9d877faf8d85da675ade1a
Name:           dateutils
Version:        0.4.12
Release:        1%{?dist}
Summary:        Command-line date and time calculation, conversion, and comparison
License:        BSD-3-Clause
URL:            http://www.fresse.org/dateutils/
Source0:        https://github.com/hroptatyr/dateutils/releases/download/v%{version}/%{name}-%{version}.tar.xz
Requires: tzdata
Conflicts: tzdata < tzdata-2022g
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  tzdata
# /oreon:deps
%description
Tools which revolve around fiddling with dates and times on the command
line, with a strong focus on use cases that arise when dealing with large
amounts of financial data.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-silent-rules --without-old-links
make %{?_smp_mflags} CFLAGS="$CFLAGS"
%install
%make_install
rm -f %{buildroot}%{_infodir}/dir
rm -f %{buildroot}%{_datadir}/doc/%{name}/LICENSE
%oreon_autofiles main

%check

make check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
