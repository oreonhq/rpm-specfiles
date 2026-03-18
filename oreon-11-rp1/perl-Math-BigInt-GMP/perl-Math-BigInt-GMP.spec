Name:           perl-Math-BigInt-GMP
Version:        1.7003
Release:        4%{?dist}
Summary:        Use the GMP library for Math::BigInt routines
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Math-BigInt-GMP
Source0:        https://cpan.metacpan.org/authors/id/P/PJ/PJACKLAM/Math-BigInt-GMP-%{version}.tar.gz
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Module Runtime
BuildRequires:  perl(Math::BigInt::Lib) >= 1.999801
BuildRequires:  perl(XSLoader) >= 0.02
# Test Suite
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Math::BigFloat) >= 1.994
BuildRequires:  perl(Math::BigInt) >= 2.005001
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(threads)
Requires:       perl(Math::BigInt) >= 2.005001

%{?perl_default_filter}

# Filter modules bundled for tests
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(.::t/.*.inc\\)
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}

%description
Provides support for big integer calculations by means of the GMP library, as
a replacement (drop-in) module for Math::BigInt's core, Math::BigInt::Calc.pm.
Math::BigInt::GMP does not use Math::GMP, but provides its own XS layer to
access the GMP library. This cuts out another (perl subroutine) layer and
also reduces the memory footprint by not loading Math::GMP and Carp at all.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Math::BigInt) >= 2.005001

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Math-BigInt-GMP-%{version}

# Remove bundled libraries
rm -r inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST
find -type f -exec chmod -x {} +

# Get rid of bogus exec permissions
chmod -c -x CHANGES lib/Math/BigInt/GMP.pm

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" \
  NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/00sig.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset TEST_SIGNATURE
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc BUGS CHANGES CREDITS README TODO
%{perl_vendorarch}/auto/Math/
%{perl_vendorarch}/Math/
%{_mandir}/man3/Math::BigInt::GMP.3*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.7003-4
- Prepare for Oreon 11 (RP1)
