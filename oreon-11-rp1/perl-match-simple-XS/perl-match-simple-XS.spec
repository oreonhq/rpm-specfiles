%global source0_hash 59973e4849e46ff84484abd74f8ebf85f46fcfa8767b0183269d1907e35d1c41

Name:           perl-match-simple-XS
Version:        0.002
Release:        11%{?dist}
Summary:        XS backend for match::simple
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            http://search.cpan.org/dist/match-simple-XS/
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/match-simple-XS-%{version}.tar.gz
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(match::simple)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(XSLoader)

%description
XS backend for match::simple.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n match-simple-XS-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes COPYRIGHT CREDITS README
%license LICENSE
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/match*
%{_mandir}/man3/*

%changelog
%autochangelog
