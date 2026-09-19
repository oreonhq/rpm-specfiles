%global source0_hash 005a8d19f7fb90939dec54d633d308850b2ecb69c6ba4443bfe65303167f8c0d

Name:           perl-SQL-Library
Version:        0.0.5
Release:        39%{?dist}
Summary:        Manage libraries of SQL easily 
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/SQL-Library
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHRISV/SQL-Library-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Test::More)

%description
This is a perl module for managing simple SQL libraries stored in
INI-like files.  It allows developers to maintain the SQL they require 
OUTSIDE of their perl code.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n SQL-Library-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# the better to doc it later...
cp t/sqltest.lib example.lib

%check
make test

%files
%license LICENSE
%doc Changes README example.lib
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
