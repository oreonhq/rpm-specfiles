%global source0_hash 11b52f86c44d6cc26e9a4129e67c2589071dbe1b8ac1f8895761517491c6e44b

Summary:    PostgreSQL monitoring script
Name:       check_postgres
Version:    2.25.0
Release:    16%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:    LicenseRef-Callaway-BSD
URL:        https://bucardo.org/check_postgres/
BuildArch:  noarch

Source0:    https://github.com/bucardo/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz

Patch0:     0001-Update-doc-and-fix-missing-title-close-tag.patch
Patch1:     0002-Make-sure-our-temp-filehandles-are-doing-UTF-8.patch
Patch2:     0004-Fix-check_replication_slots-on-recently-promoted-ser.patch

BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6.1
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%description
Script for checking the state of one or more Postgres databases and reporting
back in a Nagios-friendly manner. It is also used for MRTG.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}

%if 0%{?rhel} == 7
# When building noarch on Koji you have no guaranteed how _libdir expands:
rm -fr %{buildroot}%{_prefix}/lib*
# Not happening automatically:
sed -i -e 's|^#!/usr/bin/env perl|#!/usr/bin/perl|g' %{buildroot}%{_bindir}/%{name}.pl
%endif

# Fix permissions
chmod 755 %{buildroot}%{_bindir}/%{name}.pl
chmod 644 %{buildroot}%{_mandir}/man1/%{name}.*

# Fix man page filename
mv %{buildroot}%{_mandir}/man1/%{name}.1p %{buildroot}%{_mandir}/man1/%{name}.pl.1

%files
%license LICENSE
%doc %{name}.pl.html README.md TODO
%{_mandir}/man1/%{name}.pl.1*
%{_bindir}/%{name}.pl

%changelog
%autochangelog
