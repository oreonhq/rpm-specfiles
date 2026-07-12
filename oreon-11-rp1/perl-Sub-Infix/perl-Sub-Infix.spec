%global source0_hash 5caeaada66ab4afdfdae56c023e099880543a9a7c1f931f20a834d5881c15ecb

Name:           perl-Sub-Infix
Version:        0.004
Release:        27%{?dist}
Summary:        Create a fake infix operator
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Sub-Infix
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Sub-Infix-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__perl}
BuildRequires:  %{__make}

BuildRequires:  perl-interpreter >= 0:5.006
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.17
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.47
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

# optional
BuildRequires:  perl(Scalar::Util)
Recommends:     perl(Scalar::Util)


Provides:       perl(Sub::Infix)
%description
Sub::Infix creates fake infix operators using overloading. It doesn't use
source filters, or Devel::Declare, or any of that magic.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Sub-Infix-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README CREDITS
%license COPYRIGHT LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
