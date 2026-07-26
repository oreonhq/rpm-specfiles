%global source0_hash 4d34571ad6e7c318ea0eee62685a09ec427e4376bd11a208da20cbee7cdcca68

Name:           perl-Class-DBI-Plugin-Type
Version:        0.02
Release:        59%{?dist}
Summary:        Determine type information for columns
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-DBI-Plugin-Type
Source0:        https://cpan.metacpan.org/authors/id/S/SI/SIMON/Class-DBI-Plugin-Type-%{version}.tar.gz
# Adapt to changes in DBD-SQLite-1.61_02, bug #1664030, CPAN RT#128135,
# proposed to the upstream
Patch0:         Class-DBI-Plugin-Type-0.02-Fix-compatibility-with-DBD-SQLite-1.61_02.patch
# Adapt tests to SQLite-3.37.0, bug #2066613, CPAN RT#140750
Patch1:         Class-DBI-Plugin-Type-0.02-SQLite-3.37.0.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-doc
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Class::DBI)
BuildRequires:  perl(Class::DBI::Plugin)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Pod::Perldoc)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
Requires:  perl(Class::DBI::Plugin)

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Class-DBI-Plugin-Type-%{version}
perldoc -t perlartistic > Artistic
perldoc -t perlgpl > COPYING

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license Artistic COPYING
%doc Changes
%{perl_vendorlib}/Class/DBI/Plugin/
%{_mandir}/man3/*.3*

%changelog
%autochangelog
