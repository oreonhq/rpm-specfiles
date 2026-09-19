%global source0_hash 0f7623e9d724760aa64040222da1d82f1188586791329261cc60dad1d60d6a92

Name:           perl-Symbol-Global-Name
Version:        0.05
Release:        36%{?dist}
Summary:        Finds name and type of a global variable
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Symbol-Global-Name
Source0:        https://cpan.metacpan.org/authors/id/A/AL/ALEXMV/Symbol-Global-Name-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__make}
BuildRequires:  perl-interpreter >= 1:5.8.0
BuildRequires:  perl-generators
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)

BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::ReadmeFromPod)

%description
Lookups symbol table to find an element by reference.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Symbol-Global-Name-%{version}
rm -rf inc/

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
