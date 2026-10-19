%global source0_hash 9af790eb92d1c6330d33c6daa8decf8a9c5dcc87b81779d6b12e14b931c3b87b
Name:           perl-Math-Random-ISAAC-XS
Version:        1.004
Release:        1%{?dist}
Summary:        C implementation of the ISAAC PRNG algorithm
License:        LicenseRef-Callaway-MIT OR GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Math-Random-ISAAC-XS
Source0:        https://cpan.metacpan.org/authors/id/J/JA/JAWNSY/Math-Random-ISAAC-XS-%{version}.tar.gz
Requires:       perl(Math::Random::ISAAC)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::ParseXS)
BuildRequires:  perl(Math::Random::ISAAC)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::LeakTrace)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
# /oreon:deps
%description
This module implements the same interface as Math::Random::ISAAC in C and can
be used as a drop-in replacement. This is the recommended implementation of the
module, based on Bob Jenkins' reference implementation in C.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Math-Random-ISAAC-XS-%{version}
# rm -f weaver.ini dist.ini
sed -i 's/\r//' examples/*.pl

%build

%{__perl} Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build
%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
