%global source0_hash f3ff294097b1a4b02a4bae6dc3544ded744a08972e831c1d2741083403197f47

Name:		perl-Rose-Object
Version:	0.860
Release:	36%{?dist}
Summary:	Simple object base class
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Rose-Object
Source0:	https://cpan.metacpan.org/authors/id/J/JS/JSIRACUSA/Rose-Object-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(B)
BuildRequires:	perl(Carp)
BuildRequires:	perl(constant)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(lib)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Pod) >= 1.00
BuildRequires:	perl(warnings)
Requires:	perl(B)
Requires:	perl(Test::More)
Requires:	perl(Test::Simple)

%filter_from_requires /perl(Rose::DateTime::Util)/d
%filter_setup

%description
Rose::Object is a generic object base class. It provides very little
functionality, but a healthy dose of convention.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Rose-Object-%{version}
find . -type f -executable -exec chmod -x {} \;

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -delete
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/Rose/
%{_mandir}/man3/Rose*.3pm*

%changelog
%autochangelog
