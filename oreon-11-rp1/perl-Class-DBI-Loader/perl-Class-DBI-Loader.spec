%global source0_hash ea009afa64d575780e9f707ba9d95b13f8d618b5f6b288def6a8de28ad62c28e
Name:           perl-Class-DBI-Loader
Version:        0.34
Release:        1%{?dist}
Summary:        Dynamic definition of Class::DBI sub classes
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-DBI-Loader
Source0:        https://cpan.metacpan.org/authors/id/D/DM/DMAKI/Class-DBI-Loader-%{version}.tar.gz
BuildArch:      noarch
Requires:  perl(DBI) >= 1.3
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(DBI\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::DBI)
BuildRequires:  perl(Class::DBI::Pg)
BuildRequires:  perl(Class::DBI::SQLite)
BuildRequires:  perl(Class::DBI::mysql)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Lingua::EN::Inflect)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Text::Balanced)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-Pod-Perldoc
BuildRequires:  perl-doc
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Class-DBI-Loader-%{version}
perldoc -t perlartistic > Artistic
perldoc -t perlgpl > COPYING

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

TEST_POD=1 make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
