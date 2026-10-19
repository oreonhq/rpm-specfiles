%global source0_hash 95188d847aa13eb69fcd8169f16d25b5c427d010b7e6daa5bbea34ecde34e46a
Name:           servicelog
Version:        1.1.16
Release:        10%{?dist}
Summary:        Servicelog Tools
License:        GPL-2.0-only
URL:            https://github.com/power-ras/servicelog
Source0:        https://github.com/power-ras/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
ExclusiveArch: ppc %{power64}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  help2man
BuildRequires:  librtas-devel
BuildRequires:  libservicelog-devel
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
Command-line interfaces for viewing and manipulating the contents of
the servicelog database. Contains entries that are useful
for performing system service operations, and for providing a history
of service operations that have been performed on the system.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -fiv
%configure
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT
help2man -s 8 -N $RPM_BUILD_ROOT/%{_sbindir}/slog_common_event > $RPM_BUILD_ROOT/%{_mandir}/man8/slog_common_event.8
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
