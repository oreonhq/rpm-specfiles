%global source0_hash 09fe1415e16e49a69e13c0ef6e6a4a3fd8b856f389d3f3e624d7ab3b71719f78

Name:           perl-Contextual-Return
Version:        0.004014
Release:        27%{?dist}
Summary:        Create context-sensitive return values
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Contextual-Return
Source0:        https://cpan.metacpan.org/modules/by-module/Contextual/Contextual-Return-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Want)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(Test::More)
# Optional tests only
BuildRequires:  perl(Test::Pod) >= 1.14
# Dependencies
Requires:       perl(Data::Dumper)

%global __provides_exclude ^perl\\(DB\\)$

Provides:       perl(Contextual::Return)
Provides:       perl(Contextual::Return)
%description
This module allows you to define return values of a perl sub that are
appropriate given the calling context.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Contextual-Return-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Contextual/
%{_mandir}/man3/Contextual::Return.3*
%{_mandir}/man3/Contextual::Return::Failure.3*

%changelog
%autochangelog
