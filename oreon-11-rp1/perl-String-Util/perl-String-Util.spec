%global source0_hash e089dc4aa714c4801b359df6546f265bad392ca2380309c8900e45b4668bb76e

Name:           perl-String-Util
Version:        1.35
Release:        4%{?dist}
Summary:        String processing utilities
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/String-Util
Source0:        https://cpan.metacpan.org/modules/by-module/String/String-Util-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.14
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(Test::More) >= 0.88
# Dependencies
# (none)

%description
String::Util provides a collection of small, handy utilities for
processing strings.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n String-Util-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README.md
%{perl_vendorlib}/String/
%{_mandir}/man3/String::Util.3*

%changelog
%autochangelog
