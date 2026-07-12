%global source0_hash 336918d56ac9482d248d2ca6e79ed7f2cc67403fbdecdd73a9c414a034adb3cf

Name:           perl-PPIx-Utils
Version:        0.004
Release:        2%{?dist}
Summary:        Utility functions for PPI
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/PPIx-Utils/
Source0:        https://cpan.metacpan.org/authors/id/D/DB/DBOOK/PPIx-Utils-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  %{__make}
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6

BuildRequires:  perl(B::Keywords) >= 1.09
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(PPI) >= 1.250
BuildRequires:  perl(PPI::Dumper)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More) >= 0.88

Requires:       perl(B::Keywords) >= 1.09
Requires:       perl(PPI) >= 1.250


# Filter duplicate unversioned requires
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(B::Keywords\\)$

Provides:       perl(PPIx::Utils)
Provides:       perl(PPIx::Utils::Traversal)
%description
PPIx::Utils is a collection of utility functions for working with PPI
documents. The functions are organized into submodules, and may be imported
from the appropriate submodule or via this module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n PPIx-Utils-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/PPIx
%{_mandir}/man3/PPIx::Utils*

%changelog
%autochangelog
