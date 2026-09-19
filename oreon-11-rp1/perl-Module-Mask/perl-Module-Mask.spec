%global source0_hash 2d73f81ff21c9fa28102791e546ff257164b3025f7832544c8223fb87c1e7e77

Name:           perl-Module-Mask
Version:        0.06
Release:        39%{?dist}
Summary:        Pretend certain modules are not installed
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Mask
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MATTLAW/Module-Mask-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build) >= 0.40
BuildRequires:  perl(Module::Build::Compat) >= 0.02
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Carp::Heavy)
BuildRequires:  perl(Module::Util) >= 1.00
BuildRequires:  perl(Scalar::Util) >= 1.01
# Tests
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
# Optional tests
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04

Requires:       perl(Module::Util) >= 1.00

# Filter duplicate unversioned requires
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Module::Util\\)$

%description
Sometimes you need to test what happens when a given module is not
installed. This module provides a way of temporarily hiding installed
modules from perl's require mechanism. The Module::Mask object adds itself
to @INC and blocks require calls to restricted modules.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Module-Mask-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
