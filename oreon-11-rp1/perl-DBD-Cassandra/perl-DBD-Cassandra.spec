%global source0_hash d3df170d06c3ae180868f7d81e000c0015634509489fb60fc7f49e626b1a4665

Name:           perl-DBD-Cassandra
Version:        0.57
Release:        2%{?dist}
Summary:        DBI database backend for Cassandra
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/DBD-Cassandra
Source0:        https://www.cpan.org/modules/by-module/DBD/DBD-Cassandra-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.0
BuildRequires:  perl(Cassandra::Client) >= 0.10
BuildRequires:  perl(DBI) >= 1.621
BuildRequires:  perl(Devel::GlobalDestruction)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Ref::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)

%description
DBD::Cassandra is a Perl5 Database Interface driver for Cassandra, using
the CQL3 query language.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DBD-Cassandra-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset AUTHOR_TESTING
unset CASSANDRA_HOS
make test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/DBD/
%{_mandir}/man3/DBD::Cassandra*.3pm*

%changelog
%autochangelog
