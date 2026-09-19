%global source0_hash 06e08432a6b97705606c925709b99129ad926516e477d58e4461e4b3d9f30917

Name:           perl-Data-Stream-Bulk
Version:        0.11
Release:        38%{?dist}
Summary:        N at a time iteration API
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-Stream-Bulk
Source0:        https://cpan.metacpan.org/authors/id/D/DO/DOY/Data-Stream-Bulk-%{version}.tar.gz
BuildArch:      noarch
# build requirements
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# runtime requirements
BuildRequires:  perl(Carp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(namespace::clean) >= 0.08
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(DBD::Mock)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(DBIx::Class)
BuildRequires:  perl(DBIx::Class::Schema)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::TempDir)
BuildRequires:  perl(base)

%{?perl_default_filter}

%description
This module tries to find middle ground between one at a time and all at
once processing of data sets.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Data-Stream-Bulk-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
%{make_build} test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/Data*
%{_mandir}/man3/Data*

%changelog
%autochangelog
