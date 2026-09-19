%global source0_hash 16088a6420d4c1d4c628a9b7cdf7a7286de7dfdf6b408eb571846f6780bc74e6

Name:           perl-AnyEvent-XSPromises
Version:        0.006
Release:        3%{?dist}
Summary:        Another Promises library, this time implemented in XS for performance
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/AnyEvent-XSPromises
Source0:        http://www.cpan.org/modules/by-module/AnyEvent/AnyEvent-XSPromises-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.0
BuildRequires:  perl(AnyEvent) >= 7
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(XSLoader)
# Tests
BuildRequires:  perl(Test::More)

%description
This library provides a Promises interface, written in XS for performance,
conforming to the Promises/A+ specification.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n AnyEvent-XSPromises-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendorarch}/auto/AnyEvent/XSPromises/
%{perl_vendorarch}/AnyEvent/XSPromises*
%{_mandir}/man3/AnyEvent::XSPromises.3pm*

%changelog
%autochangelog
