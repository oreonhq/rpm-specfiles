%global source0_hash 8bc329920b9be12b2e68608e87b5eb817a368530a4eb60b56973dd9ad2f04775
Name:           pilotlog
Version:        11
Release:        1%{?dist}
Summary:        A pilot logbook for logging flight time
License:        AGPL-3.0-or-later
URL:            https://pilotlog.sourceforge.net
Source0:        https://download.stansoft.org/files/%{name}-%{version}.tar.bz2
ExclusiveArch:  x86_64 aarch64
Requires:       aubit4gl
Requires:       libpq
Requires:       postgresql-server
# oreon:deps
BuildRequires:  aubit4gl-devel
BuildRequires:  gcc
BuildRequires:  libpq-devel
BuildRequires:  postgresql-server
# /oreon:deps
%description
Pilot Log is a pilot logbook for logging flight time and calculating
aircraft weight & balance.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%if "%{getenv:AUBITDIR}" == ""
export AUBITDIR=%{_libdir}/aubit4gl
%endif
%configure
%make_build createdb
%make_build -j1
%install
rm -rf %{buildroot}%{_libdir}/%{name}
mkdir -p %{buildroot}%{_libdir}/%{name}
install -d %{buildroot}%{_mandir}/man1
install -p -m 0644 man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
%make_install
mkdir -p %{buildroot}%{_bindir}
ln -sf ../..%{_libdir}/%{name}/pl %{buildroot}%{_bindir}/%{name}
rm -f %{buildroot}%{_libdir}/%{name}/README
rm -f %{buildroot}%{_libdir}/%{name}/changelog
rm -f %{buildroot}%{_libdir}/%{name}/COPYING
%oreon_autofiles main

%check

make check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
