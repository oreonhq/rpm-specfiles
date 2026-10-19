%global source0_hash 11b52f86c44d6cc26e9a4129e67c2589071dbe1b8ac1f8895761517491c6e44b
Summary:        PostgreSQL monitoring script
Name:       check_postgres
Version:    2.25.0
Release:        16%{?dist}
License:    LicenseRef-Callaway-BSD
URL:        https://bucardo.org/check_postgres/
BuildArch:  noarch
Source0:        https://github.com/bucardo/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Patch0:     0001-Update-doc-and-fix-missing-title-close-tag.patch
Patch1:     0002-Make-sure-our-temp-filehandles-are-doing-UTF-8.patch
Patch2:     0004-Fix-check_replication_slots-on-recently-promoted-ser.patch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Script for checking the state of one or more Postgres databases and reporting
back in a Nagios-friendly manner. It is also used for MRTG.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
chmod 755 %{buildroot}%{_bindir}/%{name}.pl
chmod 644 %{buildroot}%{_mandir}/man1/%{name}.*
mv %{buildroot}%{_mandir}/man1/%{name}.1p %{buildroot}%{_mandir}/man1/%{name}.pl.1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
