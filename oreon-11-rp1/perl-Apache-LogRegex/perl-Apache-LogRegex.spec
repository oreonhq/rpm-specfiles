%global source0_hash 683c4334f1496aed8fc5e4f69c1b08de8aa99eacd36a200a2ea43e651b9ca823

Name:           perl-Apache-LogRegex
Version:        1.71
Release:        29%{?dist}
Summary:        Parse a line from an Apache logfile into a hash
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Apache-LogRegex
Source0:        https://cpan.metacpan.org/authors/id/S/SP/SPACEBAT/Apache-LogRegex-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(Test::More)

%description
Designed as a simple class to parse Apache log files.  It will construct
a regex that will parse the given log file format and can then parse
lines from the log file line by line returning a hash of each line.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Apache-LogRegex-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
