%global source0_hash 886ecbf85cfe94f4135ee5689c4847a9ae783ecb99e6759e12c734f2dd6116bc

Name:           perl-GDTextUtil
Version:        0.86
Release:        60%{?dist}
Summary:        Text utilities for use with GD
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/GDTextUtil
Source0:        https://cpan.metacpan.org/modules/by-module/GD/GDTextUtil-%{version}.tar.gz
BuildArch:      noarch

# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  %{__make}

BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
# Module Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Config)
BuildRequires:  perl(GD)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Test Suite
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
# Dependencies
Requires:       perl(Config)
Requires:       perl(POSIX)

%description
This package provides three modules that make it possible to work with
internal GD fonts as well as TrueType fonts, without having to worry
about different interface functions to call. Apart from an abstract
interface to all font types and strings for GD, this library also
provides some utility in aligning and wrapping your string.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n GDTextUtil-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
%{__make} test

%files
%doc Changes README demo/
%{perl_vendorlib}/GD/
%{_mandir}/man3/GD::Text.3*
%{_mandir}/man3/GD::Text::Align.3*
%{_mandir}/man3/GD::Text::Wrap.3*

%changelog
%autochangelog
