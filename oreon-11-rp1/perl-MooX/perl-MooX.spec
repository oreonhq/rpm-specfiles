%global source0_hash 2ff91a656e78aae0aca42293829d7a7e5acb9bf22b0401635b2ab6c870de32d5

Name:           perl-MooX
Version:        0.101
Release:        37%{?dist}
Summary:        Using Moo and MooX:: packages the most lazy way
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooX
Source0:        https://cpan.metacpan.org/authors/id/G/GE/GETTY/MooX-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__make}
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::OptList) >= 0.107
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Import::Into) >= 1.000003
BuildRequires:  perl(Module::Runtime) >= 0.013
BuildRequires:  perl(Moo) >= 0.091004
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

BuildRequires:  perl(Test::More) >= 0.96

%description
Using Moo and MooX:: packages the most lazy way

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooX-%{version}

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
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
