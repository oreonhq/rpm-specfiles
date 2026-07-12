%global source0_hash cc719479836579d52b02bc328ed80a98f679df043a99b5710ab2c191669eb837

Name:           perl-List-Compare
Version:        0.55
Release:        15%{?dist}
Summary:        Compare elements of two or more lists
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/List-Compare
Source0:        https://cpan.metacpan.org/authors/id/J/JK/JKEENAN/List-Compare-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
Requires:       perl(Exporter)
Requires:       perl(warnings)

Provides:       perl(List::Compare)
%description
Advanced functionality to compare members of two or more lists.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n List-Compare-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes FAQ README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
