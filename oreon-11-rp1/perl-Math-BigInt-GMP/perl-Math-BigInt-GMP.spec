%global source0_hash a165628b277d1e833f5b657ca836db81bc44e04c107cfe9f5b8bd94755642ed5
Name:           perl-Math-BigInt-GMP
Version:        1.7003
Release:        1%{?dist}
Summary:        Use the GMP library for Math::BigInt routines
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Math-BigInt-GMP
Source0:        https://cpan.metacpan.org/authors/id/P/PJ/PJACKLAM/Math-BigInt-GMP-%{version}.tar.gz
Requires:       perl(Math::BigInt) >= 2.005001
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(.::t/.*.inc\\)
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
Provides:       perl(Math::BigInt::GMP)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  make
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Math::BigFloat)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Math::BigInt::Lib)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/00sig.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset TEST_SIGNATURE
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Math-BigInt-GMP-tests -f %{oreon_filedir}/perl-Math-BigInt-GMP-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.7003-4
- Prepare for Oreon 11 (RP1)
