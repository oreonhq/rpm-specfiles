%global source0_hash b8fea0b09714bbadf202b9b3434cce6b59c282e7869268d0c08b85880fdbb446

Name:           dateutils
Version:        0.4.11
Release:        %autorelease
Summary:        Command-line date and time calculation, conversion, and comparison

License:        BSD-3-Clause
URL:            http://www.fresse.org/dateutils/
Source0:        https://github.com/hroptatyr/dateutils/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires: make
# for tests
BuildRequires: tzdata

# Tests won't pass woth older tzdata!
Requires: tzdata
Conflicts: tzdata < tzdata-2022g

%description
Tools which revolve around fiddling with dates and times on the command
line, with a strong focus on use cases that arise when dealing with large
amounts of financial data.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure --disable-silent-rules --without-old-links
# see note in configure script for why we're passing CFLAGS explicitly here
make %{?_smp_mflags} CFLAGS="$CFLAGS"

%install
%make_install

rm -f %{buildroot}%{_infodir}/dir
# this is duplicated otherwise
rm -f %{buildroot}%{_datadir}/doc/%{name}/LICENSE

%check
make check

%files
%license LICENSE
%doc README.md
%{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/%{name}*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.tzmcc
%{_datadir}/%{name}/locale

%changelog
%autochangelog
