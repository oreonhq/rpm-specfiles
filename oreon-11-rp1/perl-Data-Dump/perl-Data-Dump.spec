%global source0_hash a4aa6e0ddbf39d5ad49bddfe0f89d9da864e3bc00f627125d1bc580472f53fbd

Name:           perl-Data-Dump
Version:        1.25
Release:        14%{?dist}
Summary:        Pretty printing of data structures
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-Dump
Source0:        https://cpan.metacpan.org/modules/by-module/Data/Data-Dump-%{version}.tar.gz



BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(subs)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
# Really optional
Suggests:       perl(MIME::Base64)

Provides:       perl(Data::Dump)
%description
This module provides a single function called dump() that takes a list of
values as its argument and produces a string as its result. The string
contains Perl code that, when evaled, produces a deep copy of the original
arguments. The string is formatted for easy reading.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Data-Dump-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README.md
%{perl_vendorlib}/Data/
%{_mandir}/man3/Data::Dump.3*
%{_mandir}/man3/Data::Dump::Filtered.3*
%{_mandir}/man3/Data::Dump::Trace.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.25-14
- Prepare for Oreon 11 (RP1)
