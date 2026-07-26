%global source0_hash 3080375bf5f96cb15310d1870a75472dc1fd2371273c6a546b81401b6f674a28

Name:           perl-Roman
Version:        1.24
Release:        29%{?dist}
Summary:        Functions for converting between Roman and Arabic numerals
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Roman
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHORNY/Roman-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(warnings)
BuildRequires:  sed
Requires:       perl(Exporter) >= 5.57

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Exporter\\)$

%description
This package provides some functions which help conversion of numeric
notation between Roman and Arabic.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Roman-%{version}
sed -i -e 's/\r//' README Changes

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
