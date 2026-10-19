%global source0_hash 2d73f81ff21c9fa28102791e546ff257164b3025f7832544c8223fb87c1e7e77
Name:           perl-Module-Mask
Version:        0.06
Release:        1%{?dist}
Summary:        Pretend certain modules are not installed
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Mask
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MATTLAW/Module-Mask-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Module::Util) >= 1.00
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Module::Util\\)$
# oreon:deps
BuildRequires:  perl(Carp)
BuildRequires:  perl(Carp::Heavy)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Build::Compat)
BuildRequires:  perl(Module::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(lib)
BuildRequires:  perl-generators
# /oreon:deps
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
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
