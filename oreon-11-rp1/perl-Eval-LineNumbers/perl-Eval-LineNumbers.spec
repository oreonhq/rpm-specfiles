%global source0_hash 79b7a0068d4a2419b9ed36c229edbcb9690977618a9032ee770616cb4071ce0a

Name:           perl-Eval-LineNumbers
Version:        0.35
Release:        14%{?dist}
Summary:        Add line numbers to hereis blocks that contain perl source code
# Automatically converted from old format: Artistic 2.0 or LGPLv2+ - review is highly recommended.
License:        Artistic-2.0 OR LicenseRef-Callaway-LGPLv2+
URL:            https://metacpan.org/release/Eval-LineNumbers
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Eval-LineNumbers-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

%description
This module adds a line number to hereis text that is going to be
eval'ed so that error messages will point back to the right place.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Eval-LineNumbers-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README
%{perl_vendorlib}/Eval
%{_mandir}/man3/Eval::LineNumbers.3pm.gz

%changelog
%autochangelog
